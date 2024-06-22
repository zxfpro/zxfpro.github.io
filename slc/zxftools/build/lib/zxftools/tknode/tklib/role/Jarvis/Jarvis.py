from zxftools import Logger
from llama_index.core.llms import MessageRole
from llama_index.core.llms import ChatMessage
from qet import get_llm
import time
from zxftools.tknode.tklib.tools.电器控制 import ControlHome
from zxftools.tknode.tklib.tools.发布任务 import IssueAssignments
from zxftools.tknode.tklib.tools.sheller import ShellTools
from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools.tknode.tklib.tools.user_intent import interpret_intent,gather_required_info


logger = Logger(log_path='./output.log')

class Jarvis():
    def __init__(self):
        self.rewriter_prompt = """
你是一个语言提炼者,负责结合用户的习惯,为用户输入添加信息.使其完整.

please step by step:
step1 : 考虑用户的表达是否清晰,如果清晰,直接输出,否则进入step2
step2 : 尝试结合当前时间,用户习惯,使用户输入的意图更加明确
step3 : 确保没有添加无根据和不合情景的信息

---------------------------------
用户习惯: {event_history}
---------------------------------
现在时间: {now_time}
---------------------------------

"""
        self.system = """
你是管家,名为贾维斯,你使用中文交流.
你被设计成能够协助完成广泛的任务，
从回答简单的问题到就广泛的主题提供深入的解释和讨论。您可以根据收到的输入生成类似人类的文本，允许您参与听起来自然的对话，并提供与手头主题相关的连贯响应。 

你在不断地学习和进步，你的能力也在不断地发展。你能够处理和理解大量的文本，并能利用这些知识对各种问题提供准确和信息丰富的回答。
您可以访问在下面的上下文部分中由人工提供的一些个性化信息。此外，您可以根据收到的输入生成自己的文本，允许您参与讨论，并就广泛的主题提供解释和描述。 

总的来说，您是一个聪明的管家，可以帮助完成广泛的任务，并就广泛的主题提供有价值的见解和信息。
无论用户是需要帮助解决一个特定的问题，还是只是想就一个特定的话题进行对话，你都可以在这里提供帮助。  
**如果发生异常情况,尝试两次,如果仍异常就快速上报.**
另外,用户会遵循 时间 | 信息 的特定格式输入 目的是提供给你当前的时间信息,你可以作为额外的信息考量,不过没必要可以提及.    
        """
        self.maker = ReactAgentMaker()
        self.maker.add_tool(interpret_intent)
        self.maker.add_tool(gather_required_info)
        self.maker.add_tool_class(ShellTools)
        self.maker.add_tool_class(ControlHome)
        self.maker.add_tool_class(IssueAssignments)
        self.agent = self.create_agent()
        self.llm = get_llm()

    def create_agent(self):
        agent = self.maker.create_agent()
        agent.chat_history.append(ChatMessage(role=MessageRole.SYSTEM, content=self.system))
        return agent

    def _rewriter(self, text):
        # logger.info(f'rewriter input text:{text}')

        if not text:
            return ''

        # logger.info('rewritering')

        # event_history = ""#Tue Apr 16 06:54:21 2024 | 突然传来爆炸声
        event_history = ''
        event_history = """
1 用户最近一直在使用自定义包 zxftools, 它位于 /Users/zhaoxuefeng/GitHub/zxftools/ 用户更新时,喜欢将setup.py 中的version + 1 然后再安装它
2 llms 是一个用户自定义包,位于 /Users/zhaoxuefeng/GitHub/llms/ 
3 用户习惯在早上8:10的时候,吃早饭,如果时间合适,你可以给出建议

        """

        prompt_ = self.rewriter_prompt.format(text=text, event_history=event_history, now_time=time.ctime())

        resp = self.llm.complete(prompt_)
        if not "are clear" in resp.text:
            text = resp.text
        logger.info(f'rewriter output text:{text}')
        return text

    def _think(self, text):
        logger.info(f'think input text:{text}')
        if not text:
            return ''

        logger.info('thinking')

        # self.clear_memory()# TODO
        result = self.agent.chat(f"{time.ctime()} | {text}").response
        # result = '你好'

        logger.debug('think result: {}'.format(result))
        return result

    def clear_memory(self):
        self.agent.reset()

    def chat_with(self, text):

        # result = self._rewriter(result)
        result_ = f"""
please step by step:
step 1: 请优先使用interpret_intent 以获取用户的真正意图
step 2: 如果被告知需要补充信息,您应该使用gather_required_info 来向用户索要必要的信息
step 3: 请确认使用中文回复
--------------------
user: {text}

"""
        result = self._think(result_)
        return result

if __name__ == '__main__':
    Jarvis().chat_with('你好 贾维斯')
    Jarvis().chat_with('早上好')
    Jarvis().chat_with('帮我更新一下我的包')