from llama_index.core.indices.keyword_table import (
    SimpleKeywordTableIndex,
    KeywordTableIndex,
    RAKEKeywordTableIndex
)
from llama_index.core.indices import (
    TreeIndex,
    VectorStoreIndex,
    DocumentSummaryIndex,
    KnowledgeGraphIndex,
    GPTTreeIndex,
    GPTDocumentSummaryIndex,
    GPTEmptyIndex,
    GPTKeywordTableIndex,
    GPTPandasIndex
)
from llama_index.core.ingestion import (
    IngestionPipeline,
    IngestionCache,
    DocstoreStrategy
)
from llama_index.core.vector_stores import MetadataFilters, ExactMatchFilter
from llama_index.core.objects import ObjectIndex
from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.core import load_index_from_storage,StorageContext
from llama_index.core import Settings
from enum import Enum
from typing import List
from .splitter import SplitterFactory,SplitterType
from .embedding import EmbeddingFactory
from .extractor import ExtractorFactory
from .utils import pop_get

class IndexType(Enum):
    VectorStoreIndex = 'VectorStoreIndex'
    DocumentSummaryIndex = 'DocumentSummaryIndex' #可用 需要大模型
    KnowledgeGraphIndex = 'KnowledgeGraphIndex'
    RAKEKeywordTableIndex = 'RAKEKeywordTableIndex'
    SimpleKeywordTableIndex = 'SimpleKeywordTableIndex'
    GPTTreeIndex = 'GPTTreeIndex'
    TreeIndex = 'TreeIndex'
    SummaryIndex = 'SummaryIndex'

class IndexMaker:
    """
    print(
        index.as_query_engine(
            text_qa_template=text_qa_template,
            refine_template=refine_template,
            llm=llm,
        ).query("Who is Joe Biden?")
    )

    """
    def __init__(self,index_type:IndexType=IndexType.VectorStoreIndex,
                      splitter:SplitterFactory=None,
                      embedding: EmbeddingFactory = None,
                      extractors:List[ExtractorFactory]=[],
                      docstore=None,
                 vector_store=None):
        assert isinstance(extractors, list)
        # project_name = type if isinstance(type, str) else type.value

        self.splitter = [splitter] if splitter else [SplitterFactory(type=SplitterType.TOKEN_TEXT)]
        self.embedding = [embedding] if embedding else []
        self.extractors = extractors or []
        self.transformations = self.splitter + self.extractors + self.embedding
        self.index_type = index_type
        self.pipeline = IngestionPipeline(transformations=self.transformations,
                                          vector_store=vector_store,
                                          docstore=docstore,
                                          cache = None,
                                          )

    def set_global(self,llm,embed_model):
        Settings.llm = llm
        Settings.embed_model = embed_model

    def ingestion(self,documents,num_workers=4,show_progress=False):
        return self.pipeline.run(documents=documents,
                                 show_progress = show_progress,
                                 num_workers=num_workers,)

    def aingestion(self,documents,num_workers=4,show_progress=False):
        return self.pipeline.arun(documents=documents,
                                 show_progress = show_progress,
                                 num_workers=num_workers,)

    @staticmethod
    def load_index(persist_dir='aa'):
        # rebuild storage context
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
        return index

    @staticmethod
    def save_index(index, persist_dir='aa'):
        index.storage_context.persist(persist_dir=persist_dir)
        return 'success'

    def save_ingestion(self, path):
        self.pipeline.persist(path)

    def load_ingestion(self, path):
        self.pipeline.load(path)

    def create_index(self,input_data,type='documents',llm = None,show_progress = False,objects=None,
                     index_struct = None,storage_context = None,service_context = None):
        if type == 'documents':
            nodes = self.ingestion(documents=input_data)
        elif type == 'nodes':
            nodes = input_data
        else:
            raise('error')
        self.nodes = nodes
        # nodes[0].metadata['human_des'] = '是目录,主要解释了本篇文章主要说了什么'
        print(len(nodes),'len_nodes node-X ')
        for idx, node in enumerate(nodes):
            node.id_ = f"node-{idx}"
        if self.index_type.value == 'VectorStoreIndex':
            index = VectorStoreIndex(nodes=nodes,
                                     llm=llm,
                                     show_progress=show_progress,
                                     objects =objects,
                                     index_struct = index_struct,
                                     storage_context=storage_context, #定义或者否
                                     service_context = service_context,
                            )
        elif self.index_type.value == 'TreeIndex':
            index = TreeIndex(nodes=nodes,
                              llm = llm,
                              show_progress = show_progress,
                              objects=objects,
                              index_struct=index_struct,
                              storage_context=storage_context,
                              service_context=service_context,
                            )

        elif self.index_type.value == 'DocumentSummaryIndex':
            index = DocumentSummaryIndex(nodes=nodes,
                                         llm=llm,
                                         show_progress=show_progress,
                                         objects=objects,
                                         index_struct=index_struct,
                                         storage_context=storage_context,
                                         service_context=service_context,
                            )

        elif self.index_type.value == 'KnowledgeGraphIndex':
            index = KnowledgeGraphIndex(nodes=nodes,
                                        llm=llm,
                                        show_progress=show_progress,
                                        objects=objects,
                                        index_struct=index_struct,
                                        storage_context=storage_context,
                                        service_context=service_context,
                            )
        elif self.index_type.value == 'RAKEKeywordTableIndex':
            index = RAKEKeywordTableIndex(nodes=nodes,
                                          llm=llm,
                                          show_progress=show_progress,
                                          objects=objects,
                                          index_struct=index_struct,
                                          storage_context=storage_context,
                                          service_context=service_context,
                            )
        elif self.index_type.value == 'SimpleKeywordTableIndex':
            index = SimpleKeywordTableIndex(nodes=nodes,
                                            llm=llm,
                                            show_progress=show_progress,
                                            objects=objects,
                                            index_struct=index_struct,
                                            storage_context=storage_context,
                                            service_context=service_context,
                            )
        elif self.index_type.value == 'GPTTreeIndex':
            index = GPTTreeIndex(nodes=nodes,
                                 llm=llm,
                                 show_progress=show_progress,
                                 objects=objects,
                                 index_struct=index_struct,
                                 storage_context=storage_context,
                                 service_context=service_context,
                            )
        elif self.index_type.value == 'SummaryIndex':
            index = SummaryIndex(nodes=nodes,
                                 llm=llm,
                                 show_progress=show_progress,
                                 objects=objects,
                                 index_struct=index_struct,
                                 storage_context=storage_context,
                                 service_context=service_context,
                            )
        else:
            print(1)

        return index

    def create_object_index(self,all_tools):

        index = ObjectIndex.from_objects(
            all_tools,
            index_cls=VectorStoreIndex,
        )
        return index

    @staticmethod
    def get_nodes_from_index(index):
        node_ids_list = []
        for info in index.docstore.get_all_ref_doc_info().values():
            node_ids_list += info.node_ids
        nodes = index.docstore.get_nodes(node_ids_list)
        return nodes

    @staticmethod
    def Muiti_Tenancy(index):
        # 确保之前的metadata 中有user 的类型

        # For Jerry
        jerry_query_engine = index.as_query_engine(
            filters=MetadataFilters(
                filters=[
                    ExactMatchFilter(
                        key="user",
                        value="Jerry",
                    )
                ]
            ),
            similarity_top_k=3,
        )


"""

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(),
        embed_model,
    ],
    docstore=RedisDocumentStore.from_host_and_port(
        "localhost", 6379, namespace="document_store"
    ),
    vector_store=RedisVectorStore(
        schema=custom_schema,
        redis_url="redis://localhost:6379",
    ),
    cache=IngestionCache(
        cache=RedisCache.from_host_and_port("localhost", 6379),
        collection="redis_cache",
    ),
    docstore_strategy=DocstoreStrategy.UPSERTS,
)

"""



"""

from llama_index.core.ingestion.cache import RedisCache
from llama_index.core.ingestion import IngestionCache

ingest_cache = IngestionCache(
    cache=RedisCache.from_host_and_port(host="127.0.0.1", port=6379),
    collection="my_test_cache",
)

import weaviate

auth_config = weaviate.AuthApiKey(api_key="...")

client = weaviate.Client(url="https://...", auth_client_secret=auth_config)

from llama_index.vector_stores.weaviate import WeaviateVectorStore

vector_store = WeaviateVectorStore(
    weaviate_client=client, index_name="CachingTest"
)

from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(
    transformations=[
        TextCleaner(),
        text_splitter,
        embed_model,
        TitleExtractor(),
    ],
    vector_store=vector_store,
    cache=ingest_cache,
)

ingest_cache.clear()

"""

