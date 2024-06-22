from llama_hub.tools.code_interpreter import CodeInterpreterToolSpec
from urllib.parse import urljoin
from .base import BaseTools
from .utils import EnvBase
import requests
import json
import os
import time
from zxftools.project import Logger
import paramiko
from bs4 import BeautifulSoup
from exa_py import Exa





class CoderTools(BaseTools):
    register_default = ['code_interpreter', 'write_test_code', 'run_test_code', 'rewrite_test_code', 'code_writer']
    def __init__(self, register=[],llm=None):
        super().__init__(register,self.register_default)
        self.llm = llm
        self.inter = CodeInterpreterToolSpec()

    def code_interpreter(self,code_path:str)->str:
        """
        A function to execute python code, and return the stdout and stderr

        You should import any libraries that you wish to use. You have access to any libraries the user has installed.

        The code passed to this functuon is executed in isolation. It should be complete at the time it is passed to this function.

        You should interpret the output and errors returned from this function, and attempt to fix any problems.
        If you cannot fix the error, show the code to the user and ask for help

        It is not possible to return graphics or other complicated data from this function. If the user cannot see the output, save it to a file and tell the user.
        """
        with open(code_path,'r') as f:
            code = f.read()

        return self.inter.code_interpreter(code)

    def write_test_code(self,code: str) -> str:
        """
        This is a tool for writing complete test code for a given piece of code
        """
        result = self.llm.complete(f"""
Write test code for this code, which should be as complete as possible to cover all parameter combinations
code:
{code}
-----------
text_code:
""").text
        return result

    def run_test_code(self,code: str) -> str:
        """
        This tool helps you execute your test code locally
        """
        return self.inter.code_interpreter(code)

    def rewrite_test_code(self,test_code:str,demand:str)->str:
        """
        This is a tool that allows you to rewrite test code according to guidance and requirements
        """
        result = self.llm.complete(f"""
Modify the existing test code as required.
require: {demand}
test_code:
{test_code}
-----------
new_text_code:
""").text
        return result

    def code_writer(self, text: str) -> str:
        return self.llm.complete(
            f'You are a Python code expert and can write code according to requirements. Requirement: {text}').text



class FileTools(BaseTools):
    register_default = ['delay', 'save_py', 'read_py']
    def __init__(self, llm, register=[]):

        super().__init__(register,self.register_default)
        self.llm = llm

    def delay(self,time_later: int) -> str:
        """
        the tool can be used to jump over [time_later] second
        """
        import time
        time.sleep(time_later)
        return f'{time_later} second later'

    def save_py(self,code: str, save_path: str) -> str:
        """
        This is a code review tool that saves your code to a local file so that you can use shell_tool to validate your code in a local dockerfiles.
        for example:
            save_path = temp.py
        """
        with open(save_path, 'w') as f:
            f.write(code)
        return f'saved your code in {save_path}'

    def read_py(self,path: str) -> str:
        """
        这个工具可以用来读py文件 输入文件路径 就能得到文件中的内容
        """
        try:
            with open(path, 'r') as f:
                text = f.read()
        except Exception as e:
            return f'Error {e}'
        return text


class HumanIOTools(BaseTools):
    register_default = ['human_reviewer', 'demand_confirmation', 'question_rewriter']
    def __init__(self, llm, register=[]):

        super().__init__(register,self.register_default)
        self.llm = llm

    def human_reviewer(text: str) -> str:
        """
        Use it before the final submission to verify if your work meets the requirements.
        """
        print('***********check************')
        result = input(text)
        if result == 'q':
            raise Exception('终止任务')
        return result

    def demand_confirmation(self,question: str) -> str:
        """
        If you feel that the requirements are unclear, you can use the tool to ask the user questions to clarify the requirements
        """
        result = input(question)
        return result

    def question_rewriter(self, question: str) -> str:
        """
        If the user's question is not clear enough, you can use this tool to get a clearer question description.
        """
        background = """

        """
        result = self.llm.complete(f"""
        Please provide a more specific and complete description of the user's question based on the background:
        {background}
        -------------------
        and the question asked by the user:
        {question}

        -------------------
        Make the user's problem more specific and complete
        """)
        return result.text


class ShellTools(BaseTools):
    register_default = ['vim_open', 'vim_write', 'localhost_terminal',
                        'remotehost_terminal', 'remotehost_logout', 'remotehost_login']
    def __init__(self,human_supervision=True, register=[],log_path = '~/.zxf_file/cache/ai_shell.log'):

        super().__init__(register,self.register_default)
        self.logger = Logger(log_path)
        self.ssh = None
        self.channel = None
        self.human_supervision = human_supervision
        self.env = EnvBase()

    def _guard(self,command:str)->None:
        for order in ['rm ','mv ','ln ']:
            if order in command:
                k = input(f'ask for : {command}  y/n')
                if k == 'n':
                    raise "退出"
        if self.human_supervision:
            k = input(f'ask for : {command}  y/n')
            if k == 'n':
                raise "退出"

    def _get_result(self,interval=1):
        result_all = ''
        while True:
            time.sleep(interval)
            if self.channel.recv_ready():
                output = self.channel.recv(65535)  # 读取数据
                result = output.decode('utf-8')
                result_all += result
            else:
                break
        return result_all

    def vim_open(self,file:str)->str:
        """
        Tools that mimic vim can open files and view their contents
        """
        self._guard(file)
        with open(file,'r') as f:
            content = f.read()
        return content
    def vim_write(self,content:str,file:str)->str:
        """
        Tools that mimic vim can overwrite new content to a specified file
        """
        k = input(f'{content} want to write : {file}  y/n')
        if k == 'n':
            raise "退出"
        with open(file,'w') as f:
            f.write(content)
        return 'write success'

    def localhost_terminal(self,shell_command: str) -> str:
        """
        A tool can manipulate the local terminal with continuous multistep
        """
        self._guard(shell_command)
        if not shell_command.startswith('rm'):

            self._guard(shell_command)
            self.logger.info(f"localhost: {shell_command}")
            shell_commands = shell_command.split('&&')

            commands = [i.strip() for i in shell_commands]
            end = self.env.works(commands, run=True)
            return end

            # if len(commands) > 1:
            #     end = self.env.works(shell_command, run=True)
            #     return end
            # if shell_command
            #
            # end = self.env.work(shell_command, run=True)
            # return end
        else:
            return "you can not to use rm order"

    # TODO 尽可能避免异步命令
    def remotehost_terminal(self,shell_command: str) -> str:
        """
        the tool to use remote server terminal
        """
        self._guard(shell_command)

        self.logger.info(f"remotehost: {shell_command}")
        # 发送命令
        self.channel.send(f'{shell_command}\n')
        result = self._get_result(1)

        if len(result)>1000:
            result_all = result[:500] + '......' + result[-500:]
        else:
            result_all = result

        # # 等待命令执行
        # time.sleep(wait_time)

        # 获取结果
        # while not self.channel.recv_ready():  # 等待直到有数据可以接收
        #     time.sleep(1)
        #
        # output = self.channel.recv(65535)  # 读取数据
        return result_all

    def remotehost_logout(self) -> str:
        """
        the tool logout remote server
        """
        # 关闭通道
        self.channel.close()
        # global ssh
        self.ssh.close()

        return "logout success"

    def remotehost_login(self,ip: str, username: str, password: str) -> str:
        """
        the tool to login remote server
        """
        # 创建SSH对象 #TODO 不安全
        self.ssh = paramiko.SSHClient()
        # 自动接受不在known_hosts文件的主机密钥
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        self.ssh.connect(ip, port=22, username=username, password=password)
        # 创建一个交互式的shell会话
        trans = self.ssh.get_transport()
        self.channel = trans.open_channel("session")
        self.channel.get_pty()
        self.channel.invoke_shell()

        # 等待通道准备好
        time.sleep(1)
        return "login success"



class MathTools(BaseTools):
    register_default = ['multiply', 'minus', 'plus']
    def __init__(self, register=[]):
        super().__init__(register,self.register_default)

    def multiply(self ,a: int, b: int) -> int:
        """Multiple two integers and returns the result integer"""
        return a * b

    def minus(self ,a: int, b: int) -> int:
        """minus two integers and returns the result integer"""
        return a - b

    def plus(self ,a: int, b: int) -> int:
        """plus two integers and returns the result integer"""
        return a + b


class WebTools(BaseTools):
    register_default = ['get_all_links', 'get_content']
    def __init__(self, register=[]):
        super().__init__(register, self.register_default)

    def get_all_links(self, url):
        """Retrieve all links from a given URL and return a list of tuples containing the link text and the absolute URL"""
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page: {url}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")

        links = [
            (a.text, urljoin(url, a["href"]))
            for a in soup.find_all("a", href=True)
            if a["href"]
        ]

        return links

    def get_content(self, url):
        """Retrieve the text content from a given URL and return it as a string"""
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the page: {url}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        text_content = soup.get_text()

        return text_content


class ExaTools(BaseTools):
    register_default = ['search', 'find_similar', 'get_contents']

    def __init__(self, register=[]):
        super().__init__(register, self.register_default)
        self.exa = Exa(api_key=os.environ["EXA_API_KEY"])

    def search(self, query: str):
        """Search for a webpage based on the query."""
        return self.exa.search(f"{query}", use_autoprompt=True, num_results=5)

    def find_similar(self, url: str):
        """Search for webpages similar to a given URL.
        The url passed in should be a URL returned from `search`.
        """
        return self.exa.find_similar(url, num_results=5)

    def get_contents(self, ids: list[str]):
        """Get the contents of a webpage.
        The ids passed in should be a list of ids returned from `search`.
        """
        return self.exa.get_contents(ids)



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