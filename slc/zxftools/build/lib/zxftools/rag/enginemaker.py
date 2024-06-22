from llama_index.core.postprocessor import (
    MetadataReplacementPostProcessor,
    LLMRerank,
    SentenceTransformerRerank,
    LongContextReorder,
    FixedRecencyPostprocessor,
    EmbeddingRecencyPostprocessor,
    SentenceEmbeddingOptimizer,
    TimeWeightedPostprocessor,
    SimilarityPostprocessor,
    KeywordNodePostprocessor,
)

from llama_index.core.question_gen import LLMQuestionGenerator
from llama_index.core.question_gen.prompts import DEFAULT_SUB_QUESTION_PROMPT_TMPL
from llama_index.core.retrievers import QueryFusionRetriever, AutoMergingRetriever
from llama_index.core.query_engine import SubQuestionQueryEngine,RouterQueryEngine,RetrieverQueryEngine
from llama_index.core.selectors import (
    LLMSingleSelector,
    LLMMultiSelector,
    PydanticMultiSelector,
    PydanticSingleSelector,
)
from llama_index.core.retrievers import VectorIndexRetriever, QueryFusionRetriever,RouterRetriever,BaseRetriever
from llama_index.indices.managed.vectara import VectaraAutoRetriever
from llama_index.retrievers.videodb import VideoDBRetriever
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.retrievers import KeywordTableSimpleRetriever

from llama_index.core.response_synthesizers import Refine,Accumulate,BaseSynthesizer,CompactAndRefine,Generation,SimpleSummarize,TreeSummarize
from llama_index.core.retrievers import RecursiveRetriever

from llama_index.core.chat_engine.types import ChatMode
from llama_index.core.tools import QueryEngineTool
import os
from enum import Enum
from typing import List,Dict


# Retriever
from .libs import CharacterMatchRetriever

# NodePostprocessors

class NodePostprocessorsType(Enum):
    SimilarityPostprocessor = 'SimilarityPostprocessor'
    KeywordNodePostprocessor = 'Keyword'
    MetadataReplacementPostProcessor = 'metadata_replacement'
    LongContextReorder = 'long_context_reorder'
    FixedRecencyPostprocessor = 'fixed_recency'
    EmbeddingRecencyPostprocessor = 'embedding_recency'
    TimeWeightedPostprocessor = 'time_weighted'
    SentenceEmbeddingOptimizer = 'sentence_embedding_optimizer'
    LLMRerank = 'llm_rerank'
    CohereRerank = 'CohereRerank'
    SentenceTransformerRerank = 'sentence_transformer_rerank'
    # colbert_reranker = 'colbert_reranker'
"""
from llama_index.core.postprocessor import SentenceTransformerRerank

postprocessor = SentenceTransformerRerank(
    model="mixedbread-ai/mxbai-rerank-base-v1", top_n=2
)
"""
# engine = reactagent
class NodePostprocessorsFactory:
    def __new__(cls, postprocessor:NodePostprocessorsType, **kwargs):
        """
        from llama_index.postprocessor.rankgpt_rerank import RankGPTRerank
        from llama_index.postprocessor.colbert_rerank import ColbertRerank
        """
        if postprocessor.value == 'SimilarityPostprocessor':
            postprocessor = SimilarityPostprocessor(similarity_cutoff=kwargs.get('similarity_cutoff',0.75)) # 过滤低分
        elif postprocessor.value == 'Keyword': # 用于确保某些关键字被排除或包含。
            postprocessor = KeywordNodePostprocessor(
                required_keywords=kwargs.get('required_keywords',["Combinator"]),
                exclude_keywords = kwargs.get('exclude_keywords',["Italy"]),
            )
        elif postprocessor.value == 'metadata_replacement': # 使用metadata 中的数据替换text 文本数据
            postprocessor = MetadataReplacementPostProcessor(target_metadata_key=kwargs.get('target_metadata_key',"window"))
        elif postprocessor.value == 'long_context_reorder': # 文本重排 将重点的放到开始和结尾
            postprocessor = LongContextReorder()
        elif postprocessor.value == 'fixed_recency': #按照日期排序的rerank检索
            postprocessor = FixedRecencyPostprocessor()
        elif postprocessor.value == 'embedding_recency': #按照日期排序的rerank检索 同时
            postprocessor = EmbeddingRecencyPostprocessor(date_key="date", similarity_cutoff=0.7)
        elif postprocessor.value == 'time_weighted': # 对每个节点应用时间加权重新排名的前K个节点
            postprocessor = TimeWeightedPostprocessor(time_decay=0.5, time_access_refresh=False, top_k=kwargs.get('top_k', 1))
        elif postprocessor.value == 'sentence_embedding_optimizer':
            postprocessor = SentenceEmbeddingOptimizer(threshold_cutoff=kwargs.get('threshold_cutoff', 0.7))

        # elif postprocessor.value == 'CohereRerank':
        #     reranker = CohereRerank(api_key="<COHERE_API_KEY>", top_n=2)
        elif postprocessor.value == 'llm_rerank':
            postprocessor = LLMRerank(choice_batch_size=5, top_n=2)
            # JinaRerank  #
        elif postprocessor.value == 'sentence_transformer_rerank':
            postprocessor = SentenceTransformerRerank(model=kwargs.get('model', "cross-encoder/ms-marco-MiniLM-L-2-v2"),
                                                      top_n=kwargs.get('top_k', 1))
            # SentenceTransformerRerank(top_n=4, model="BAAI/bge-reranker-base")

        else:
            raise ValueError("Invalid postprocessor name")

        return postprocessor



# ResponseSynthesizer

class ResponseSynthesizerType(Enum):
    Refine = 'Refine'
    Accumulate = 'Accumulate'
    BaseSynthesizer = 'BaseSynthesizer'
    CompactAndRefine = 'CompactAndRefine'
    TreeSummarize = 'TreeSummarize'

class ResponseSynthesizerFactory:
    def __new__(cls, resp_syn_type: ResponseSynthesizerType=ResponseSynthesizerType.Refine,**kwargs):
        if resp_syn_type.value == 'Refine':
            syn = Refine()
        elif resp_syn_type.value == 'Accumulate':
            syn = Accumulate()
        elif resp_syn_type.value == 'BaseSynthesizer':
            syn = BaseSynthesizer()
        elif resp_syn_type.value == 'CompactAndRefine':
            syn = CompactAndRefine()
        elif resp_syn_type.value == 'TreeSummarize':
            syn = TreeSummarize()
        else:
            raise Exception('不支持')
        return syn


class RetrieverType(Enum):
    route = 'route'
    bm25 = 'bm25'
    HIERARCHICAL_NODE_PARSER = 'hierarchical'
    VideoDB = 'videoDB'
    VectaraAuto = 'VectaraAuto'
    Recursive = 'Recursive'
    CharacterMatchRetriever = 'CharacterMatchRetriever'
class RetrieverFactory:
    def __new__(cls, retriver_type: RetrieverType, index=None, **kwargs):

        """
        small-to-big retrieval
        sentence window retrieval
        recursive retrieval
        Basic retrieval from each index
        Advanced retrieval and search
        Auto-Retrieval
        Knowledge Graph Retrievers
        Composed/Hierarchical Retrievers
        # base retriver
        """
        if retriver_type.value == 'sample':
            assert index is not None
            retriever = index.as_retriever(**kwargs)
        elif retriver_type.value == 'bm25':
            assert index is not None
            retriever = BM25Retriever.from_defaults(index=index,**kwargs)
        elif retriver_type.value == 'CharacterMatchRetriever':
            assert index is not None
            retriever = CharacterMatchRetriever.from_defaults(index=index, **kwargs)

        elif retriver_type.value == 'videoDB':
            retriever = VideoDBRetriever(os.environ.get('Video_Token'))
        elif retriver_type.value == 'VectaraAuto':
            retriever = VectaraAutoRetriever(
                index,
                filter="doc.rating > 8",
                vectara_query_mode="mmr",
                mmr_k=50,
                mmr_diversity_bias=1,
            )
        elif retriver_type.value == 'Recursive':
            retriever = RecursiveRetriever("vector", retriever_dict={"vector": vector_retriever_chunk},
                                           node_dict=all_nodes_dict, verbose=True, )
        return retriever

    @staticmethod
    def create_by_retrivers(retriver_type: RetrieverType,retrievers:List[BaseRetriever],**kwargs):
        if retriver_type.value == 'queryFunction':
            retriever = QueryFusionRetriever(retrievers, num_queries=4,mode="reciprocal_rerank", use_async=True, verbose=True)
        elif retriver_type.value == 'AutoMerging':
            retriever = AutoMergingRetriever(retrievers, verbose=True)

        elif retriver_type.value == 'route':
            retriever = RouterRetriever(
                selector=PydanticMultiSelector.from_defaults(llm=kwargs.get('llm')),
                retriever_tools=kwargs.get('tools'),
            )



class SelectorType(Enum):
    PydanticSingleSelector = 'PydanticSingleSelector'
    PydanticMultiSelector = 'PydanticMultiSelector'
    LLMSingleSelector = 'LLMSingleSelector'
    LLMMultiSelector = 'LLMMultiSelector'



def get_QueryEngineTool(vector_query_engine,description):
    vector_tool = QueryEngineTool.from_defaults(
            query_engine=vector_query_engine,
            description=description,
        )
    return vector_tool




class EngineType(Enum):
    QUERY_ENGINE = 'query_engine'
    CHAT_ENGINE = 'chat_engine'
    RETRIEVER_ENGINE = "retriever_query_engine"
    ROUTE_ENGINE = "route_query_engine"
    SubQuestionQueryEngine = 'SubQuestionQueryEngine'

class EngineMaker():
    def __init__(self,llm=None):
        # chat_engine.chat('',tool_choice="query_engine_tool")
        self.llm = llm

    def create_engine_by_index(self,index,engine_type:EngineType=EngineType.QUERY_ENGINE, **kwargs):
        if engine_type.value == 'query_engine':
            # from llama_index.core.indices.vector_store.retrievers import VectorIndexRetriever
            query_engine = index.as_query_engine(**kwargs)  # VectorIndexRetriever??
            return query_engine
        elif engine_type.value == 'chat_engine':
            print("""
            CHAT_ENGINE 有特殊的传入参数 chat_mode 类型为 ChatMode
            from llama_index.core.chat_engine.types import ChatMode
            模式简介:
                best - 将查询引擎变成一个工具，与ReAct数据代理或OpenAI数据代理一起使用，具体取决于您的LLM支持的内容。OpenAI数据代理需要gpt - 3.5 - turbo或gpt - 4，因为它们使用从OpenAI调用API的函数。
                condense_question - 查看聊天历史记录，并重写用户消息作为索引的查询。从查询引擎读取响应后返回响应。
                context - 使用每条用户消息从索引中检索节点。检索到的文本被插入到系统提示符中，以便聊天引擎可以自然响应或使用查询引擎的上下文。
                condense_plus_context - condense_question和context的组合。查看聊天历史记录，并重写用户消息作为索引的检索查询。检索到的文本被插入到系统提示符中，以便聊天引擎可以自然响应或使用查询引擎的上下文。
                simple - 直接与LLM进行简单聊天，不涉及查询引擎。
                react - 与best相同，但强制使用ReAct数据代理。
                openai - 与best相同，但强制使用OpenAI数据代理。
                        """)
            chat_mode = kwargs.get('chat_mode') or ChatMode.BEST
            query_engine = index.as_chat_engine(**kwargs)  # VectorIndexRetriever??
            return query_engine
        else:
            print(f'{engine_type} 无法在此函数下使用')

    def create_engine_by_retriver(self,retriever=None,response_synthesizer=None,node_postprocessors:List[NodePostprocessorsFactory]=None,
                                  engine_type:EngineType=EngineType.QUERY_ENGINE):
        if engine_type.value == 'retriever_query_engine':
            query_engine = RetrieverQueryEngine.from_args(
                llm=self.llm,
                retriever=retriever,
                response_synthesizer=response_synthesizer,
                node_postprocessors=node_postprocessors,
                # response_mode
            )
            return query_engine
        else:
            print(f'{engine_type} 无法在此函数下使用')

    def create_engine_by_tools(self,engine_tools_map: List[Dict['obj','des']], selectors: SelectorType=SelectorType.PydanticSingleSelector,
                               engine_type:EngineType=EngineType.QUERY_ENGINE):
        # initialize router query engine (single selection, pydantic)

        """
        :param engine_tools_map:  [Dict['obj':'vector_query_engine','des':str]   for example : [{'obj':engine, 'des':'这是一个可以获取之前记忆的工具'}]
        :param selectors:
        :return:
        """
        if selectors.value == 'PydanticSingleSelector':
            # pydantic selectors feed in pydantic objects to a function calling API
            selector = PydanticSingleSelector.from_defaults()  # single selector (pydantic)
        elif selectors.value == 'PydanticMultiSelector':
            selector = PydanticMultiSelector.from_defaults()  # multi selector (pydantic)
        elif selectors.value == 'LLMSingleSelector':
            # LLM selectors use text completion endpoints
            selector = LLMSingleSelector.from_defaults()  # single selector (LLM)
        elif selectors.value == 'LLMMultiSelector':
            selector = LLMMultiSelector.from_defaults()  # multi selector (LLM)
        else:
            selector = LLMMultiSelector.from_defaults()  # multi selector (LLM)

        tools = [get_QueryEngineTool(tools_info['obj'], tools_info['des']) for tools_info in engine_tools_map]

        if engine_type.value == 'route_query_engine':
            query_engine = RouterQueryEngine.from_defaults(
                selector=selector,
                query_engine_tools=tools,
                llm = self.llm,
                verbose = False,
                select_multi = False,
                summarizer = None,
            )
            return query_engine

        elif engine_type.value == 'SubQuestionQueryEngine':
            question_gen = LLMQuestionGenerator.from_defaults(prompt_template_str="""
Follow the example, but instead of giving a question, always prefix the question 
with: 'By first identifying and quoting the most relevant sources, '. 
"""+ DEFAULT_SUB_QUESTION_PROMPT_TMPL)

            query_engine = SubQuestionQueryEngine.from_defaults(
                question_gen=question_gen,
                llm = self.llm,
                query_engine_tools=tools,
                response_synthesizer = None,
                verbose = True,
                use_async=False,
            )
            return query_engine
        else:
            print(f'{engine_type} 无法在此函数下使用')

    @staticmethod
    def get_nodes_from_index(index):
        node_ids_list = []
        for info in index.docstore.get_all_ref_doc_info().values():
            node_ids_list += info.node_ids
        nodes = index.docstore.get_nodes(node_ids_list)
        return nodes






