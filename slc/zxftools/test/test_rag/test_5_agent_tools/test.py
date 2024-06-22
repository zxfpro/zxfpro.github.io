import unittest
import itertools
# pipeline QChain
from langchain.agents import AgentOutputParser
from langchain.schema import AgentAction, AgentFinish
import re
from typing import List, Tuple, Any, Union
from zxftools.agent_helper.pipeline import QChain


class TestParams(unittest.TestCase):

    def __init__(self):
        pass

    def test_p(self):
        pass


class TestStringMethods(unittest.TestCase):

    def test_params(self):
        # 定义参数列表
        use_memory = [True, False]
        verbose = [True, False]
        flows = [True, False]
        stream = [True, False]
        # 遍历参数组合
        for u,v,f,s in itertools.product(use_memory, verbose, flows, stream):
            print(f'use_memory:{u},verbose:{v},flows:{f},stream:{s}')
            qchatbox = QChain(use_memory=u,verbose=v,flows=f,stream=s)[0]
            print(qchatbox('hello'))

    def test_params2(self):
        qchatbox = QChain(template='Here is a question',)[0]
        print(qchatbox('hello'))

    def test_params3(self):
        conver = QChain(template='Here is a question {aaa}', )[1]
        print(conver.predict(human_input='hello',aaa=12))


class CustomOutputParser1(AgentOutputParser):
    def parse(self, llm_output: str) -> Union[AgentAction, AgentFinish]:
        # Check if tknode should finish
        if "Final Answer:" in llm_output:
            return AgentFinish(
                # Return values is generally always a dictionary with a single `output` key
                # It is not recommended to try anything else at the moment :)
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        # Parse out the action and action input
        regex = r"Action\s*\d*\s*:(.*?)\nAction\s*\d*\s*Input\s*\d*\s*:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        # Return the action and action input
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

#
# qchatbox = QChain(verbose=False)[0]
# print(qchatbox('hello'))
#
# qchatbox = QChain(stream=False)[0]
# print(qchatbox('hello'))
#
# qchatbox = QChain(stream=False)[0]
# print(qchatbox('hello'))


# qchatbox = QChain(flows=False)[0]
# print(qchatbox('hello'))

# qchatbox = QChain()[0]
# print(qchatbox('hello'))

#################


#
#
# chatbox = Agent.llm('你是一个聊天机器人')
#
# chatbox('你好')
#
# @Agent.tools('测试工具','会给出周杰伦是谁的信息')
# def test(x):
#     return '周杰伦是一个著名的歌唱家'
#
# tools = [test()]
#
# ag = Agent(tools)
#
# ag('谁是周杰伦')
#
#
#
# ####################
#
# # Tool
#
# import pandas as pd
#
#
# @agents.Tools.tool
# def plot(path:str)->str:
#     """
#     传入一个csv 文件路径 绘制对应的折线图
#     """
#     pd.read_csv(path).plot()
#     return 'success'
#
#
# """
# for example:
#     @tools(name='tool_name', description='tools description')
#     def do_house(text='11'):
#         return '我做好了'
#     tools = [do_house(), do_house()]
#
# """
#
#
#
#
# import zxftools
#
# from zxftools.tknode.agents import Agent
#
# from zxftools.tknode.pipeline import QuickChain,MemoryChain,MemoryChain2
#
# from zxftools.tknode.memory import Memory
#
# from zxftools.tknode.prompt_template import Templates
#
#
#
#
# memory = Memory('Buffer',window=True,n=3)
#
# chat = MemoryChain(memory = memory)
#
#
#
    # gpt-3.5-turbo-0301
    # gpt-3.5-turbo-0613
    # gpt-3.5-turbo-16k
    # gpt-3.5-turbo-16k-0613
#
