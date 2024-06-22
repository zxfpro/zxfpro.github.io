from llama_index.core.chat_engine.types import ChatMode
from llama_index.core.tools import QueryEngineTool
from llama_index.core.question_gen import LLMQuestionGenerator
from llama_index.core.question_gen.prompts import DEFAULT_SUB_QUESTION_PROMPT_TMPL
from llama_index.core.query_engine import SubQuestionQueryEngine,RouterQueryEngine,RetrieverQueryEngine
from llama_index.core.selectors import (
    LLMSingleSelector,
    LLMMultiSelector,
    PydanticMultiSelector,
    PydanticSingleSelector,
)

from enum import Enum
from typing import List,Dict
from .postprocessor import NodePostprocessorsFactory

def get_QueryEngineTool(vector_query_engine,description):
    vector_tool = QueryEngineTool.from_defaults(
            query_engine=vector_query_engine,
            description=description,
        )
    return vector_tool


class SelectorType(Enum):
    PydanticSingleSelector = 'PydanticSingleSelector'
    PydanticMultiSelector = 'PydanticMultiSelector'
    LLMSingleSelector = 'LLMSingleSelector'
    LLMMultiSelector = 'LLMMultiSelector'


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






