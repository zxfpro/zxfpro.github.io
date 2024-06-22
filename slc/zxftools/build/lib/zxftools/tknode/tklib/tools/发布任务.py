import requests
import json
from .base import BaseTools

class IssueAssignments(BaseTools):
    register_default = ['issue_sweeping_assignments',
                        'issue_coding_assignments',
                        'issue_environment_building_assignments',
                        'issue_information_collection_assignments',
                        'issue_writing_assignments']

    def __init__(self, register=[], human_supervision=True):
        super().__init__(register, self.register_default)
        self.human_supervision = human_supervision

    def issue_sweeping_assignments(self,text:str)->str:
        """
        您可以通过此工具来发布一个扫地任务,  例如 10:30 打扫客厅 强力模式
        您将会快速的接到回应,将这个回应反馈给用户,即代表你完成了任务, 例如 机器人收到任务: 10:30 打扫客厅 强力模式 预计花费: 30分钟
        你应该告诉用户,这件事情正在处理,大概多久会给反馈
        """
        data = {"text": text,
                "token": "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"}
        json_data = json.dumps(data)
        r = requests.post('http://127.0.0.1:9000/sweep',data=json_data)
        return json.loads(r.text).get('msg')

    def issue_coding_assignments(self,text:str)->str:
        """
        您可以通过此工具来发布一个代码生成任务,  例如 编写一个hello world程序
        您将会快速的接到回应,将这个回应反馈给用户,即代表你完成了任务.
        你应该告诉用户,这件事情正在处理,大概多久会给反馈
        """
        data = {"text": text,
                "token": "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"}
        json_data = json.dumps(data)
        r = requests.post('http://127.0.0.1:9000/code',data=json_data)
        return json.loads(r.text).get('msg')

    def issue_environment_building_assignments(self,text:str)->str:
        """
        您可以通过此工具来发布一个环境构建任务,  例如 帮我新建一个项目环境
        您将会快速的接到回应,将这个回应反馈给用户,即代表你完成了任务.
        你应该告诉用户,这件事情正在处理,大概多久会给反馈
        """
        data = {"text": text,
                "token": "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"}
        json_data = json.dumps(data)
        r = requests.post('http://127.0.0.1:9000/environment',data=json_data)
        return json.loads(r.text).get('msg')

    def issue_information_collection_assignments(self,topic:str)->str:
        """
        您可以通过此工具来发布一个信息收集任务,  例如 帮我收集 铷磁铁的相关信息
        您将会快速的接到回应,将这个回应反馈给用户,即代表你完成了任务.
        你应该告诉用户,这件事情正在处理,大概多久会给反馈
        """
        data = {"text": topic,
                "token": "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"}
        json_data = json.dumps(data)
        r = requests.post('http://127.0.0.1:9000/information',data=json_data)
        return json.loads(r.text).get('msg')

    def issue_writing_assignments(self,topic:str,infos:str)->str:
        """
        您可以通过此工具来发布一个写作任务,  例如 帮我编写一个软著,编写一篇论文,编写一篇作文等
        您将会快速的接到回应,将这个回应反馈给用户,即代表你完成了任务.
        你应该告诉用户,这件事情正在处理,大概多久会给反馈
        """
        data = {"text": topic,
                "token": "57d3d17868206f5e181fd27d0cbdde89d9739b0538b27ddd"}
        json_data = json.dumps(data)
        r = requests.post('http://127.0.0.1:9000/information',data=json_data)
        return json.loads(r.text).get('msg')