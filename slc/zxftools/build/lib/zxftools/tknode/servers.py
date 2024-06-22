from fastapi import FastAPI
import random
import time
from fastapi import Request
import threading
import uvicorn
import requests
from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools.project.external_interaction import DDMessage

class Mission:
    def __init__(self, priority, content,mission_id,release_ip):
        self.priority = priority
        self.content = content
        self.mission_id = mission_id
        self.task_id = ''
        self.is_last = False
        self.recall = False
        self.recall_message = None
        self.release_ip = release_ip

    def __lt__(self, other):
        # This ensures that the PriorityQueue will sort the missions by their priority
        return self.priority < other.priority

class AgentAPIService:
    def __init__(self,_tools=[],host = "localhost",port=8000,verbose=False,callback_human=False):
        self.verbose = verbose
        self.hang_missions = {}
        self.missions = []
        self.registry = {'weather_expert':'http://localhost:8001'}
        self._tools= _tools
        self.host = host
        self.port = port
        self.callback_human=callback_human
        
    def add_mission(self, priority, content,mission_id,release_ip):#2 加入列表
        mission = Mission(priority, content,mission_id,release_ip)
        
        self.missions.append(mission)
        self.missions.sort(reverse=True)
        
    def recall_mission(self,result,mission_id):
        # 定义
        mission = self.hang_missions.pop(mission_id)
        mission.recall_message = result
        
        self.missions.append(mission)
        self.missions.sort(reverse=True)
        
    def release_mission(self,priority,content,expert='weather_expert'):
        expert_url = self.registry.get(expert)
        url = f"{expert_url}/add_mission"
        self.release_mission_id = random.randint(1,100000)
        payload = {
            "priority": priority,
            "content": content,
            "mission_id": self.release_mission_id,
            "release_ip": f"http://{self.host}:{self.port}"
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = "await"
        else:
            result = "fair"
        return result
    
    def run(self):# 3任务循环
        maker = ReactAgentMaker()
        
        def release_mission(priority:int, mission_definition:str,expert:str)->str:
            """
            expert 可用 weather_expert
            You can use this tool to send out a request for assistance to help you complete the mission,
            mission_definition enter the content of the mission and priority is the priority of the mission
            """
            result = self.release_mission(priority,mission_definition,expert)
            return result

        def get_mission_result()->str:
            """
            The tool to get mission result
            """
            return self.mission.recall_message
        
        maker.add_tools([release_mission,get_mission_result]+self._tools)
        agent = maker.create_agent()
        
        while True:    
            if self.missions:
                # 有任务了
                mission = self.missions.pop()
                self.mission = mission
                
                mission = self.handle_mission(mission,agent)#4执行任务

                if mission.is_last:
                    self.callback(mission,human=self.callback_human,parents_url=mission.release_ip)#5完成通知
                else:
                    
                    self.hang_missions[self.release_mission_id] = mission
                    
                    #self.wait_task
                    
                if self.verbose:
                    print("*******************************")
                    print(self.missions,'missions')
                    print("*******************************")
                    print(self.hang_missions,'hang_missions')
                    print("*******************************")
                    print(mission.mission_id,'mission_id')
                    print("*******************************")
                    print(mission.task_id,'task_id')
                    print("*******************************")
                    print(mission.is_last,'is_last')
                    print("*******************************")
                    print(mission.content,'content')
                    print("*******************************")
                    print(mission.priority,'priority')
                    print("*******************************")
                    print(list(agent.state.task_dict.keys()),'agent.task_ids****')


            else:
                # 没有任务
                # print('任务列表为空')
                time.sleep(1)


    def handle_mission(self,mission,agent):#4执行任务
        """
        执行函数
        """
        inputs = f"""
        你是一个管家助手,如果必要,你可以发布任务来获得帮助,
        所以如果得到mission added successfully的提示就代表发布成功
        --------------
        user: {mission.content}
        """
        
        if not mission.recall:
            task = agent.create_task(inputs)
            mission.task_id = task.task_id
            
            taskid = task.task_id
        else:
            taskid = mission.task_id
        
        while True:
            result = agent.run_step(task_id = taskid)
            
            if result.output.response.endswith('await'):
                mission.recall = True
                return mission
            
            if result.is_last:
                agent.delete_task(task_id = taskid)
                mission.is_last = True
                mission.result = result.output.response
                return mission
  

        return mission

        


    def callback(self,mission,human=False,parents_url='http://localhost:7999'):#5任务完成反馈
        if human:
            result = mission.result
            DDMessage().send(f'完成 ,{result}')
        else:
            url = f"{parents_url}/get_result"  # 替换为正确的URL
            result = mission.result
            payload = {
                "result": result,
                "mission_id":mission.mission_id,
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("notice success")
            else:
                print("Failed to notice")

    def start(self):
        app = FastAPI()
        @app.post("/add_mission")
        async def add_mission(request: Request):#1添加任务
            # priority: str, content: str
            data = await request.json()
            priority,content,mission_id = data['priority'],data['content'],data['mission_id']
            release_ip = data.get('release_ip')
            assert isinstance(priority,int) and isinstance(content,str)    
            self.add_mission(priority, content,mission_id,release_ip)
            return {"message": "mission added successfully"}


        
        @app.post("/get_result")
        async def get_mission_result(request: Request):
            data = await request.json()
            result,mission_id = data['result'],data['mission_id']
            self.recall_mission(result,mission_id)
            return {"message": "mission added successfully"}

        def run_api_service():
            self.run()

        thread = threading.Thread(target=run_api_service)
        thread.start()

        uvicorn.run(app, host=self.host, port=self.port) 