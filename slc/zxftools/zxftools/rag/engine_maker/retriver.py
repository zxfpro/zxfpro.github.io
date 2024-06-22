from llama_index.core.selectors import (
    LLMSingleSelector,
    LLMMultiSelector,
    PydanticMultiSelector,
    PydanticSingleSelector,
)
from llama_index.core.retrievers import (
    VectorIndexRetriever,
    QueryFusionRetriever,
    RouterRetriever,
    BaseRetriever,
    RecursiveRetriever,
    AutoMergingRetriever)

import os
from enum import Enum
from typing import List,Dict
from .libs import CharacterMatchRetriever



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
            from llama_index.retrievers.bm25 import BM25Retriever
            retriever = BM25Retriever.from_defaults(index=index,**kwargs)
        elif retriver_type.value == 'CharacterMatchRetriever':
            assert index is not None
            retriever = CharacterMatchRetriever.from_defaults(index=index, **kwargs)

        elif retriver_type.value == 'videoDB':
            try:
                from llama_index.retrievers.videodb import VideoDBRetriever
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-retrievers-videodb"')

            retriever = VideoDBRetriever(os.environ.get('Video_Token'))
        elif retriver_type.value == 'VectaraAuto':
            try:
                from llama_index.indices.managed.vectara import VectaraAutoRetriever
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-indices-managed-vectara"')


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

