from zxftools.rag.enginemaker import EngineMaker, EngineType
from zxftools.rag.enginemaker import EngineMaker, EngineType
from llama_index.core.chat_engine.types import ChatMode
from zxftools.rag.load_data import load_data
from zxftools.rag.indexmaker import IndexMaker, IndexType, SplitterType, SplitterFactory
from zxftools.rag.indexmaker import ExtractorFactory, ExtractorType
from zxftools.rag.enginemaker import ResponseSynthesizerFactory, ResponseSynthesizerType
from zxftools.rag.enginemaker import NodePostprocessorsFactory, NodePostprocessorsType
from zxftools.tknode.agentmaker import ReactAgentMaker
from zxftools.rag.utils import display_node
from zxftools.rag.utils import display_response
from zxftools.tknode.tklib.utils import CodeExtractor
from qet import get_llm
from llama_hub.tools.arxiv import ArxivToolSpec
from llama_index.core.chat_engine.types import ChatMode
from zxftools.rag.utils import display_response

from llama_index.core import Document

from zxftools.rag import load_data

from llama_index.core import Document
from tqdm.auto import tqdm

from llama_index.core.schema import Node, NodeWithScore



import os
def datacentre(file:str,verbose=False)->str:
    if verbose:
        print(os.listdir(os.environ.get('datacentre')))
    return os.path.join(os.environ.get('datacentre'),file)
# 人为指定或者机器自主

class Library_manager():
    # dataset 原版数据 相当于周易
    # notes 给书作注 相当于孔子做的易经
    # chat_memory 指的是短期记忆
    # memory 指的是长期记忆 experience
    # thought 思维

    def 数据库相关(self):
        #
        pass

    def synchronize_kb(self):
        documents = load_data(datacentre(''))
        splitter = SplitterFactory(SplitterType.MARK, mark='\n')
        indexmaker = IndexMaker(index_type=IndexType.VectorStoreIndex, splitter=splitter)
        index = indexmaker.create_index(documents)
        IndexMaker.save_index(index, 'data/vector_db_index')
        print('同步成功')

    def make_notes(self, data=datacentre('项目管理.csv'), index_name='data/study/项目管理'):
        llm = get_llm()
        documents_study = load_data(data)  # 指定一个内容
        extras = [ExtractorFactory(ExtractorType.STUDY, llm=llm)]
        splitter = SplitterFactory(SplitterType.MARK, mark='\n')
        indexmaker2 = IndexMaker(index_type=IndexType.VectorStoreIndex, splitter=splitter, extractors=extras)
        index2 = indexmaker2.create_index(documents_study)
        IndexMaker.save_index(index2, index_name)

    def get_notes_list(self):
        pass

    def get_notes_by_id(self):
        pass

    def limits_of_authority_to_notes(self):
        pass



class IndexManager():
    def __init__(self, index_path='data/know_index'):
        self.index = IndexMaker.load_index(index_path)

    def get_nodes(self):
        return IndexMaker.get_nodes_from_index(self.index)

    def insert(self, nodes):
        self.index.insert_nodes(nodes)

    def delete(self, id='e721d635-e6ee-4383-8714-c30054e12776'):
        self.index.docstore.delete_document(id)

    def retriever(self):
        return self.index.as_retriever()




class Thought():
    def __init__(self,llm):
        self.retriver,self.dics = self.thought_content()
        self.llm = llm
    def thought_content(self):
        maker = IndexMaker()
        doc = Document(text='要求给予消息')
        doc.metadata['prompt_id'] = 0
        doc2 = Document(text='要求接收消息')
        doc2.metadata['prompt_id'] = 1

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
        index = maker.create_index([doc, doc2])
        retriver = index.as_retriever()  # kk
        return retriver, dics

    def run(self, text='你知道龙的传人是什么意思吗?', verbose=True):
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

    #     self.reactmaker = ReactAgentMaker()
    #
    # reactmaker.create_agent()
    #
    # return agent(text='你知道龙的传人是什么意思吗')
