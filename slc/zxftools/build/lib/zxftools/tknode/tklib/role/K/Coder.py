class Coder():
    def __init__(self):
        pass

    def writer(self, text: str) -> str:
        """
        更具要求写代码的工具
        """
        prompt = f"""
    {text}
    please write a piece of code as requested above

    """
        resp = llm.complete(prompt).text
        return resp

    def rewrite(self, code: str) -> str:
        """
        这是一个代码重写工具,可以将代码在原有基础上修改的更好
        """

        maker = ReactAgentMaker()

        maker.add_tool_class(ShellTools, register=['vim_open', 'vim_write', 'localhost_terminal'])

        maker.add_tool_class(CoderTools, register=['code_interpreter'])

        agent = maker.create_agent()

        result = agent.chat(f"""
        please step by step
        step 1: 运行代码,查看结果
        step 2: 若运行良好不报错,就结束并输出给用户完整可运行的代码
        step 3: 若运行报错,分析是环境问题引起(包版本老旧,包未安装等) ,还是代码错误(bug 逻辑错误)
        step 4: 针对对应问题就行修改
        step 5: 修改完毕再次返回step1

        -----------------------
        输入的代码:
        {code}
        ----------------
        **如果发生异常情况,尝试两次,如果仍异常就快速上报.**
        """)
        # display_response(result)
        return result
        代码测试

    def code_testing(self, code: str) -> str:
        """
        对代码进行测试的工具
        """
        maker2 = ReactAgentMaker()
        maker2.add_tool_class(CoderTools, register=['run_test_code', 'write_test_code', 'rewrite_test_code'])
        agent2 = maker2.create_agent()
        result = agent2.chat(f"""
        对这段代码进行系统的单元测试:
        code:
        {code}
        """)
        return result.text

    def put_in_storage(self, code, text_code):
        """
        1入库 测试写到测试  代码写到代码
        2根据动作 修改版本和提交
        3 github提交 提交人信息
        """
        maker = ReactAgentMaker()
        maker.add_tool_class(FileTools, register=['save_py'])
        agent = maker.create_agent()
        result = agent.chat(f"""
        将下列代码存放到 ./xx/code.py 
        将其对应的测试代码存放到 ./xx/test_code.py
        ---------------------
        {rewrite_code}
        {text_code}
        """)
        result2 = agent.chat(f"""
        为下列的代码编写功能简介,并将简介存放到 ./xx/introduction.py
        ----------------
        code:
        {rewrite_code}
        """)

    def review(self, code):
        viewers = [BaiduLLM(model_name='llama3'),
                   get_llm(type='claude', max_tokens=2048), ]
        # rag() # 以至于new bing gptcpt
        results = []
        for viewer in viewers:
            result = viewer.complete(f"""
帮我做code review,只需要给出优化意见和指出不足,
不需要修改代码, 请使用中文回复
---------------
{code}
""").text
            results.append(result)

        # 整合分析
        suggest = '\n\n'.join(results)
        llm2 = get_llm()
        result = llm2.complete(f"""        
{suggest}
-------------
帮我将以上的信息进行整理
整理后的内容 :""")
        return result

    def debugers(code: str, bug: str: info

    )->str:
    pass





#
# 1目前来看 单纯的让一个大模型处理中等难度甚至复杂任务,其实是不适合的,单一的思维难度对人类也很大
#
# 2所以重要的是思维模式,也就是说 对任务的分解,理解,把控 ,记忆,回忆等问题
# 作者希望获取https://github.com/jerichosiahaya/RELP 阅读这个仓库的信息,安装必要的环境,并确认仓库可以成功运行/




# 根据README.md文件的内容,我可以回答以下问题:
#
# 1. 这个项目的主要目的是什么?
# 这个项目旨在通过利用RAG(Retrieval Augmented Generation)增强技术来提高基于语言模型的文本分类性能。当语言模型缺乏足够的上下文信息时,可能无法产生最佳结果。该项目提出了两种相互增强的方法,RAG提供基于上下文相似性的知识库,而语言模型则基于获取的知识进行上下文预测。
#
# 2. 该模型使用了哪些技术?
# 该模型使用了两种上下文文本嵌入技术:IndoBERT和OpenAI的ADA-002,并采用了3-shot学习的方式,利用GPT-3.5-Turbo版本进行上下文预测。
#
# 3. 模型的验证结果如何?
# 模型在50个测试数据点上进行了验证,结果如下:
# - IndoBERT (3-shot): f1-score为0.859,准确率为0.860
# - ADA-002 (3-shot): f1-score为0.816,准确率为0.820
#
# 4. 这个项目的动机和目标是什么?
# 该项目的动机是解决语言模型在缺乏足够上下文信息时可能无法产生最佳结果的问题。目标是通过RAG增强技术为语言模型提供更多上下文知识,从而提高文本分类的性能和准确性。
#
# 总的来说,这个项目提出了一种新颖的方法,结合了RAG和语言模型的优势,旨在提高基于语言模型的文本分类任务的性能。


from zxftools_dev.tknode.agentmaker import *
from zxftools_dev.tknode.agentmaker import ReactAgentMaker
from zxftools_dev.tknode.tklib.tools.sheller import ShellTools
from llama_index.core.response.notebook_utils import display_response
from llama_hub.tools.code_interpreter import CodeInterpreterToolSpec
from zxftools_dev.tknode.tklib.tools.coder import CoderTools
from zxftools_dev.tknode.tklib.tools.files import FileTools

from qet_dev import get_llm
from qet.baidu_engine import baidu_chat
from qet_dev.baidu_engine import BaiduLLM

from qet import get_llm

maker = ReactAgentMaker()

maker.add_tool_class(ShellTools, register=['localhost_terminal'])

agent = maker.create_agent(system_content=f"""
please step by step
step 1:如果是一个新的项目,就创建一个新conda环境,并在新环境中进行操作 默认使用python3.10
step 2:如果是已经存在的项目,则切换到对应环境中进行操作
step 3:安装项目的依赖包,你应该有限寻找一下是否有requirement.txt 或者environment.yml 等环境包文件
""")


def create_conda_env():
    pass


def run(self):
    def chat(demand):
        return agent.chat(f"""
    please step by step:
    step 1: 对于用户的需求,使用 interpret_demand 来明确需求。也可以使用 gather_required_info 来向用户求证,访问当前已有进展等
    step 2: 开始使用 writer 工具编写原始代码.
    step 3: 使用rewrite 的工具对代码进行单元测试和优化
    -------
    demand:{demand}

        """)


from zxftools_dev.tknode.agentmaker import *
from zxftools_dev.tknode.agentmaker import ReactAgentMaker
from zxftools_dev.tknode.tklib.tools.sheller import ShellTools
from llama_index.core.response.notebook_utils import display_response
from llama_hub.tools.code_interpreter import CodeInterpreterToolSpec
from zxftools_dev.tknode.tklib.tools.coder import CoderTools
from zxftools_dev.tknode.tklib.tools.files import FileTools

from qet_dev import get_llm
from qet.baidu_engine import baidu_chat
from qet_dev.baidu_engine import BaiduLLM

from qet import get_llm

maker = ReactAgentMaker()



def interpret_demand(demand: str) -> str:
    """
    根据给定的需求,和背景信息来完善用户真正的意图。
    """
    result = input(demand)
    return result


def gather_required_info(ask: str) -> str:
    """
    可以根据这个函数来向用户索要相关的信息
    """
    result = input(ask)
    return result


def writer(demand: str, detail_description: str) -> str:
    """
    根据需求编写原型代码的工具
    """
    prompt = f"""
{demand}

{detail_description}
please write a piece of code as requested above
"""
    llm = get_llm()
    resp = llm.complete(prompt).text

    with open('temp_code.py', 'w') as f:
        f.write(resp)

    return f"code write in 'temp_code.py'"


def rewrite(code_path: str) -> str:
    """
    这是一个代码重写工具,可以将代码在原有基础上修改的更好
    """
    with open('temp_code.py', 'r') as f:
        code = f.read()

    maker = ReactAgentMaker()

    maker.add_tool_class(ShellTools, register=['vim_open', 'vim_write', 'localhost_terminal'], human_supervision=True)

    maker.add_tool_class(CoderTools, register=['code_interpreter'])

    agent = maker.create_agent()

    result = agent.chat(f"""
    please step by step
    step 1: 运行代码,查看结果
    step 2: 若运行良好不报错,就结束并输出给用户完整可运行的代码
    step 3: 若运行报错,分析是环境问题引起(包版本老旧,包未安装等) ,还是代码错误(bug 逻辑错误)
    step 4: 针对对应问题就行修改
    step 5: 修改完毕再次返回step1

    -----------------------
    代码所在路径:{code_path}
    ----------------
    **如果发生异常情况,尝试两次,如果仍异常就快速上报.**
    """)
    # display_response(result)
    return result


maker.add_tools([interpret_demand, writer, rewrite, gather_required_info])

agent = maker.create_agent()


def chat(demand):
    return agent.chat(f"""
please step by step:
step 1: 对于用户的需求,使用 interpret_demand 来明确需求。也可以使用 gather_required_info 来向用户求证,访问当前已有进展等
step 2: 开始使用 writer 工具编写原始代码.
step 3: 使用rewrite 的工具对代码进行单元测试和优化
-------
demand:{demand}

    """)