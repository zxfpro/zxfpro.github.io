from zxftools.rag.indexmaker import IndexMaker, IndexType, SplitterType, SplitterFactory
from zxftools.tknode.agentmaker import ReactAgentMaker
from qet import get_llm
from llama_index.core import Document
import copy
from .agentmaker import get_tools,ToolsType

class Thought():
    llm = get_llm()
    def __init__(self):
        self.reactmaker = ReactAgentMaker(llm=self.llm)
        self.retriver,self.dics = self.get_prompt_retriver()
        self.agent = None

    def get_prompt_retriver(self):
        dics = {0: """please step by step
        step 1 检索你的记忆,查看与问题相关的信息
        step 2 如果没有查询到相关信息,那么你应该向用户提问
        ---------------------
        {text}""",
                1: """please step by step
        step 1 接收消息,并表示你已经接收到了
        step 2 如果你希望获取更多的信息,你应该向用户提问来得到信息
        ---------------------
        {text}
                    """}
        maker = IndexMaker()
        doc = Document(text='要求给予消息', )
        doc2 = Document(text='要求接收消息')
        doc.metadata['prompt_id'] = 0
        doc2.metadata['prompt_id'] = 1

        index = maker.create_index([doc, doc2])
        retriver = index.as_retriever()  # kk
        return retriver, dics

    def select_prompt(self, text='你知道龙的传人是什么意思吗?', verbose=True):
        result = self.llm.complete(f'''
        输入一句话,你来判断这个问题,是需要你给予消息,还是接收消息
        一般疑问句是要求给予消息
        肯定句是要求接收消息
        ---------------
        for example:
            文本:老唐是一个脱口秀演员 输出: 要求接收消息
            文本:唐宇者是一个智者 输出: 要求接收消息
            文本:老唐是谁 输出: 要求给予消息
        --------------
        文本:{text} 输出:
        ''').text
        resu = self.retriver.retrieve(result)  # kk
        if verbose:
            print("类型判断: ", resu[0].text)
        prompt = self.dics[resu[0].metadata['prompt_id']]
        prompt_1 = prompt.format(text=text)
        return prompt_1


    def add_tool(self,tool_type = ToolsType.search_SearchAPI):
        tools,types = get_tools(tool_type)
        if types == 'single':
            self.reactmaker.add_tool(tools)
        elif types == 'class':
            self.reactmaker.add_tool_class(tools)
        elif types == 'origin':
            self.reactmaker.add_tools_origin(tools)

    def load(self,engine):
        def search_memory(inputs: str) -> str:
            """
            获取之前的上下文信息,
            """
            result = engine.query(f'{inputs} 如果没有信息,就回答没有找到相关信息')
            return result.response
        # self.reactmaker.add_tool(search_memory)

        self.add_tool(ToolsType.search_SearchAPI)
        self.add_tool(ToolsType.search_tavily)
        self.add_tool(ToolsType.search_brave)

    def create_agent(self,system_content=''):
        self.agent = self.reactmaker.create_agent(system_content=system_content)

    def chat(self,text):
        prompt = self.select_prompt(text)
        return self.agent.chat(message=prompt)


from llama_index.core.chat_engine import SimpleChatEngine
from zxftools.rag.enginemaker import NodePostprocessorsFactory,NodePostprocessorsType
"""
reactAgent 权重比例  system 0.1 chat_history 0.2  tools =0.7 
chat_engine 权重比例  system 0.3 chat_history 0.3 

chat_history 协同好
route 
react or chat

"""
class Thought1():
    def __int__(self):
        pass



#
# class Thought2():
#     def __init__(self):
#         pass
#         result = self.select_chat_engine.chat(words).response
#
#     def chat(self,words):
#
#
#         pass
#
#     from llama_index.core.chat_engine.types import ChatMode
#
#     # ChatMode.
#
#     chats = k.exp.knowledge_index.as_chat_engine(chat_mode=ChatMode.BEST)
#
#     chats.chat('你好', tool_choice='query_engine_tool')  # 强制工具选择,只有openai 有效果? 好像也不是



from .tklib.prompt.intention_recognition import intention_recognition2,intention_recognition_example
from qet.llms import get_llm
class ThoughtRoute():
    def __init__(self):

        # self.select_chat_engine = SimpleChatEngine.from_defaults(system_prompt='''你是一个意图判断器,你会对用户的每个输入进行判断,并归类到,分享信息,索要信息. 这两类中
        # for example:
        # 王成宇是谁?  索要信息
        # 桑文是谁?   索要信息
        # ''')


        system_prompt = '''你是一个意图判断器,你会对用户的每个输入进行判断,并归类到,闲聊,深入思考,信息交换. 这三类中'''

        self.select_chat_engine = SimpleChatEngine.from_defaults(system_prompt=system_prompt)

        self.select_doc = {0: 'react', 1: 'caht'}

        self.NodePost = NodePostprocessorsFactory(NodePostprocessorsType.SimilarityPostprocessor)

        self.retriver = IndexMaker().create_index(
            [self.wrap_document('索要信息', 0), self.wrap_document('分享信息', 1)]).as_retriever()

    def chat(self, words):
        self.select_auto(words)

        result = self.thought.chat(words)
        return result.response

    def wrap_document(self, text='索要信息', id=0):
        doc = Document(text=text)
        doc.metadata['prompt_id'] = id
        return doc

    def select_auto1(self,words):
        llm = get_llm()
        def get_prompt_id(resu):
            if resu == []:
                return None
            else:
                return resu[0].metadata['prompt_id']

        result = llm.complete(intention_recognition2.format(input=words, example=intention_recognition_example)).text
        resu = self.retriver.retrieve(result)
        resu = self.NodePost.postprocess_nodes(resu)
        thought = self.select_doc.get(get_prompt_id(resu))
        return thought

    def select_human(self, id):
        thought = self.thought_dict.get(id)
        return thought

    def select_auto(self, words):
        def get_prompt_id(resu):
            if resu == []:
                return None
            else:
                return resu[0].metadata['prompt_id']

        result = self.select_chat_engine.chat(words).response
        resu = self.retriver.retrieve(result)
        resu = self.NodePost.postprocess_nodes(resu)
        prompt = self.select_doc.get(get_prompt_id(resu))
        # prompt or other
        return prompt



    def pop_chat_history(self):
        chat_history = copy.deepcopy(self.thought.agent.chat_history)
        self.thought.agent.chat_history.clear()
        return chat_history

    def get_chat_history(self):
        chat_history = copy.deepcopy(self.thought.agent.chat_history)
        return chat_history

    def clear_history(self):
        self.thought.agent.chat_history.clear()
