
import copy
import datetime

from zxftools.rag.enginemaker import EngineMaker, EngineType
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
from zxftools.rag.utils import display_response

from llama_index.core import Document

from llama_hub.tools.arxiv import ArxivToolSpec
from llama_index.core.chat_engine.types import ChatMode
from zxftools.rag import load_data

from llama_index.core import Document
from tqdm.auto import tqdm

from llama_index.core.schema import Node, NodeWithScore
import copy
import os
def datacentre(file:str,verbose=False)->str:
    if verbose:
        print(os.listdir(os.environ.get('datacentre')))
    return os.path.join(os.environ.get('datacentre'),file)
# 人为指定或者机器自主


# class_level IndexManager():
#     def __init__(self, index_path='data/know_index'):
#         self.index = IndexMaker.load_index(index_path)
#
#     def get_nodes(self):
#         return IndexMaker.get_nodes_from_index(self.index)
#
#     def insert(self, nodes):
#         self.index.insert_nodes(nodes)
#
#     def delete(self, id='e721d635-e6ee-4383-8714-c30054e12776'):
#         self.index.docstore.delete_document(id)
#
#     def retriever(self):
#         return self.index.as_retriever()


# class_level Library_manager():
#     def __init__(self,llm=None):
#         # dataset 原版数据 相当于周易
#         # notes 给书作注 相当于孔子做的易经
#         # chat_memory 指的是短期记忆
#         # memory 指的是长期记忆 experience
#         # thought 思维
#         self.llm = llm or get_llm()
#         self.indexmaker = IndexMaker(index_type=IndexType.VectorStoreIndex,
#                                  splitter=SplitterFactory(SplitterType.MARK, mark='\n'),
#                                  extractors=[ExtractorFactory(ExtractorType.STUDY, llm=self.llm)])
#
#     def 数据库相关(self):
#         #
#         pass
#
#     def synchronize_kb(self):
#         documents = load_data(datacentre(''))
#         splitter = SplitterFactory(SplitterType.MARK, mark='\n')
#         indexmaker = IndexMaker(index_type=IndexType.VectorStoreIndex, splitter=splitter)
#         index = indexmaker.create_index(documents)
#         IndexMaker.save_index(index, 'data/vector_db_index')
#         print('同步成功')
#
#     def make_notes(self, data='项目管理.csv', index_path='data/study/项目管理'):
#         data_path = datacentre(data)
#         documents_study = load_data(data_path)  # 指定一个内容
#         index2 = self.indexmaker.create_index(documents_study)
#         IndexMaker.save_index(index2, index_path)
#
#     def get_notes_id_list(self):
#         pass
#
#     def get_notes_by_id(self,notes_id)->'notes':
#
#         return None
#
#     def Authentication_analysis(self,role,notes_id):
#         # 鉴权分析
#         return True

#
# from traceloop.sdk import Traceloop
# from traceloop.sdk.decorators import workflow
from .agentmaker import get_tools,ToolsType

from .thought_route import ThoughtRoute

class Experience():
    # 负责管理Role 的长期记忆,也就是经验模块
    def __init__(self, role_exp_path,llm=None):
        self.role_exp_path = role_exp_path
        os.makedirs(role_exp_path, exist_ok=True)
        knowledgeindexPath = os.path.join(role_exp_path, 'know_index')
        conceptsindexPath = os.path.join(role_exp_path, 'concepts_index')
        self.knowledgeindexPath = knowledgeindexPath
        self.conceptsindexPath = conceptsindexPath
        self.knowledge_index = self._init_index(knowledgeindexPath)
        self.concepts_index = self._init_index(conceptsindexPath)
        self.llm = llm

    def _init_index(self,indexPath):
        if not os.path.exists(indexPath):
            _index = IndexMaker().create_index(load_data('初始化'))
            IndexMaker.save_index(_index, indexPath)
        else:
            _index = IndexMaker.load_index(persist_dir=indexPath)
        return _index

    def get_engine(self):
        enginemaker = EngineMaker()
        know_engine = enginemaker.create_engine_by_retriver(retriever=self.knowledge_index.as_retriever(),
                                                                 response_synthesizer=ResponseSynthesizerFactory(ResponseSynthesizerType.Refine),
                                                                 node_postprocessors=[NodePostprocessorsFactory(NodePostprocessorsType.SimilarityPostprocessor,
                                                                                        similarity_cutoff=0.75)],
                                                                 engine_type=EngineType.RETRIEVER_ENGINE,
                                                                 )
        concepts_engine = enginemaker.create_engine_by_retriver(retriever=self.concepts_index.as_retriever(),
                                                                     response_synthesizer=ResponseSynthesizerFactory(ResponseSynthesizerType.Refine),
                                                                     node_postprocessors=[NodePostprocessorsFactory(NodePostprocessorsType.SimilarityPostprocessor,
                                                                                        similarity_cutoff=0.75)],
                                                                     engine_type=EngineType.RETRIEVER_ENGINE,
                                                                     )
        engine = enginemaker.create_engine_by_tools(
                            engine_tools_map=[{'obj': know_engine, 'des': '这是一个可以获取之前记忆的工具'},
                                              {'obj': concepts_engine, 'des': '这是一个可以获取之前记忆的工具'}, ],
                            engine_type=EngineType.SubQuestionQueryEngine)
        return engine

    def extract_from_note(self,notes, key='concept')->list['node']:  # knowledge
        nodes_ = copy.deepcopy(notes)

        def node2NodeWithScore(nodes, score=0.7):
            return [NodeWithScore(node=node, score=score) for node in nodes]

        def nodeWithScore2Node(nodewithscores):
            return [nodewithscore.node for nodewithscore in nodewithscores]

        postprocess = NodePostprocessorsFactory(NodePostprocessorsType.MetadataReplacementPostProcessor,
                                                target_metadata_key=key)

        splitter = SplitterFactory(SplitterType.MARK, mark='\n')


        nods2 = node2NodeWithScore(nodes_)
        nodes2 = postprocess.postprocess_nodes(nods2)
        postnodes = nodeWithScore2Node(nodes2)
        for node in postnodes:
            node.metadata.pop('knowledge')
            node.metadata.pop('concept')
        return splitter.get_nodes_from_documents(postnodes)

    def extract_knowledge_and_concepts(self,notes)->None:
        concept_nodes = self.extract_from_note(notes,key='concept')
        knowledge_nodes = self.extract_from_note(notes,key='knowledge')
        return knowledge_nodes,concept_nodes

    def _merge_node(self,node, retriever)->'node':

        __prompt = """
{aa}
{bb}
----------------
对于以上概念,如果有重复和相似的,互作补充和印证,融合成新的概念. 保留不相似的
"""
        nodespo = NodePostprocessorsFactory(NodePostprocessorsType.SimilarityPostprocessor, similarity_cutoff=0.80)
        result = retriever.retrieve(node.text)
        result_po = nodespo.postprocess_nodes(result)

        if result_po:
            concat_text = [i.text for i in result_po]
            result_po_ids = [i.id_ for i in result_po]
            result_llm = self.llm.complete(__prompt.format(aa=concat_text, bb=node.text)).text

            creation_date = str(datetime.datetime.now())[:10]
            new_node = Node(text=result_llm, extra_info={'file_name': 'merge',
                                                         'origin_node': result_po_ids,
                                                         'creation_date': creation_date})

            return new_node
        else:
            return node

    def merge_nodes(self,nodes:list,retriever)->list['node']:
        # concept_nodes
        new_nodes = []
        nodes = [node for node in nodes if node.text]
        for node in tqdm(nodes):
            newnode = self._merge_node(node,retriever=retriever)
            new_nodes.append(newnode)
        return [node for node in new_nodes if node.text]

    def save_index(self):
        IndexMaker.save_index(self.knowledge_index,self.knowledgeindexPath)
        IndexMaker.save_index(self.concepts_index,self.conceptsindexPath)



    def get_notes_from_chat_history(self,chat_history):
        index_maker = IndexMaker(splitter=SplitterFactory(SplitterType.MARK, mark='\n'),
                                 extractors=[ExtractorFactory(ExtractorType.STUDY)])
        history_summary = '\n'.join([history.content for history in chat_history])
        document = load_data(history_summary)
        index = index_maker.create_index(document)
        notes = IndexMaker.get_nodes_from_index(index)
        return notes

    def get_notes_from_nodes(self,nodes):
        extra = ExtractorFactory(ExtractorType.STUDY)
        notes = extra.extract(nodes)
        return notes

    def learning_from_notes(self,notes):
        print('extract_knowledge_and_concepts')
        knowledge_nodes,concept_nodes = self.extract_knowledge_and_concepts(notes)
        print('merge_nodes')
        knowledge_merge_nodes = self.merge_nodes(knowledge_nodes,self.knowledge_index.as_retriever())
        concept_merge_nodes = self.merge_nodes(concept_nodes, self.concepts_index.as_retriever())
        print('insert_nodes')
        self.knowledge_index.insert_nodes(knowledge_merge_nodes)
        self.concepts_index.insert_nodes(concept_merge_nodes)
        # save
        self.save_index()

    def learning_from_chat_history(self,chat_history):
        notes = self.get_notes_from_chat_history(chat_history)
        self.notes = notes
        self.learning_from_notes(notes)

    def learning_from_nodes(self,nodes):
        notes = self.get_notes_from_nodes(nodes)
        self.learning_from_notes(notes)

class Librarys():
    def __init__(self):
        pass

    def get_notes_by_id(self,notes_id):
        #请求
        pass

# 对于原始知识库的检索做成工具

class RoleBase():  # IndexManager
    # 纸上得来终觉浅 绝知此事要躬行
    role_exp_path = ''
    def __init__(self):
        self.llm = get_llm()
        self.exp = Experience(role_exp_path=self.role_exp_path,llm=self.llm)
        # get_engine  learning_from_notes    learning_from_chat_history
        engine = self.exp.get_engine()
        self.engine = engine
        self.library = Librarys()
        self.tRoute = ThoughtRoute(engine=engine)
        # Traceloop.init(disable_batch=True,
        #                api_key="ab0ae62b7b82304dbbad13dccbc0387e87c5ae46e4c5d865cacc9d0dda3244f78992d4a8aed94c1f81e643638effbc8a")

    def chat(self,words):
        result = self.tRoute.chat(words)
        return result

    def study(self,notes_id):
        notes = self.library.get_notes_by_id(notes_id)
        self.exp.learning_from_notes(notes)

    def sleep(self):
        chat_history = self.tRoute.get_chat_history()
        self.exp.learning_from_chat_history(chat_history)
        self.tRoute.clear_history()


