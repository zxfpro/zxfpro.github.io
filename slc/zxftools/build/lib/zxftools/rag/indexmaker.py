from llama_index.core.node_parser import (
    HierarchicalNodeParser,
    SemanticSplitterNodeParser,
    SentenceWindowNodeParser,
    SentenceSplitter,
    TokenTextSplitter,
    MarkdownNodeParser,
    JSONNodeParser,
    LangchainNodeParser,
    CodeSplitter
)
from llama_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor
)
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
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.core import ComposableGraph
from llama_index.core.graph_stores.types import GraphStore
from llama_index.storage.kvstore.redis import RedisKVStore
from llama_index.storage.docstore.redis import RedisDocumentStore
from llama_index.storage.index_store.redis import RedisIndexStore
from llama_index.storage.chat_store.redis import RedisChatStore
from llama_index.core.graph_stores import SimpleGraphStore
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.vector_stores.simple import SimpleVectorStore
from llama_index.core.storage.index_store.simple_index_store import SimpleIndexStore
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.storage.kvstore.firestore import FirestoreKVStore
from llama_index.storage.docstore.firestore import FirestoreDocumentStore
from llama_index.storage.index_store.firestore import FirestoreIndexStore
from llama_index.vector_stores.elasticsearch import ElasticsearchStore
from llama_index.storage.kvstore.elasticsearch import ElasticsearchKVStore
from llama_index.storage.docstore.elasticsearch import ElasticsearchDocumentStore
from llama_index.storage.index_store.elasticsearch import ElasticsearchIndexStore
from langchain.agents import (
    ConversationalAgent,
    ConversationalChatAgent,
    AgentExecutor,
    ZeroShotAgent
)
from .libs import MarkSplitter, HumanExtractor, PProgramExtractor, StudyExtractor
from enum import Enum
from typing import List
from llama_index.core import load_index_from_storage,StorageContext

from llama_index.core.node_parser import HTMLNodeParser
from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter

from llama_index.core.node_parser import SimpleFileNodeParser,MarkdownElementNodeParser,HTMLNodeParser,NodeParser,UnstructuredElementNodeParser,LlamaParseJsonNodeParser,SimpleNodeParser



from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import json
from llama_index.core.multi_modal_llms.generic_utils import load_image_urls
from llama_index.core import SimpleDirectoryReader, Document
from llama_index.core.indices import MultiModalVectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter


from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.core.schema import ImageDocument
import tqdm


# asl_index = MultiModalVectorStoreIndex(image_nodes + text_nodes)
# is_image_to_text=True


from llama_index.extractors.entity import EntityExtractor


from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.vector_stores.pinecone import PineconeVectorStore
import chromadb
import os

def pop_get(dicts,key,default=None):
    if dicts.get(key):
        key_ = dicts.pop(key)
    else:
        key_ = default
    return key_


class SplitterType(Enum):
    SENTENCE = 'sentence'
    SENTENCE_WINDOW = 'sentence_window'
    TOKEN_TEXT = 'token_text'
    MARK = 'mark_custom'
    SEMANTIC = 'semantic'
    HIERARCHICAL = 'hierarchical'
    CODE = 'code'
    MARKDOWN = 'markdown'
    JSON = 'json'
    HTML = 'html'
    LANGCHAIN = 'langchain'

    HELP = f"""
Sentence : 切分
SentenceWindow : 切分 (包含上下文)
TokenText : token 切分
Mark : 按照 特定符号切分

        sentence : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        sentence_window : kwargs [window_size 3, window_metadata_key window   original_text_metadata_key  original_sentence]
        token_text : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        mark : "mark","##"
        semantic : buffer_size 1   breakpoint_percentile_threshold 95
        hierarchical: chunk_sizes [2048, 512, 128]
        code : language','python'  'chunk_lines',80) 'chunk_lines_overlap',15) 'max_chars',4000)


other:
     semantic   # 主要适用于英语句子
     # from llama_index.core.node_parser import SimpleFileNodeParser
     # splitter = SimpleFileNodeParser()
"""

class SplitterFactory:
    def __new__(cls, type:SplitterType or str,verbose=False, **kwargs):
        """

        sentence : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        sentence_window : kwargs [window_size 3, window_metadata_key window   original_text_metadata_key  original_sentence]
        token_text : kwargs [chunk_size 404, chunk_overlap 20   separator  ' ']
        mark : "mark","##"
        semantic : buffer_size 1   breakpoint_percentile_threshold 95
        hierarchical: chunk_sizes [2048, 512, 128]
        code : language','python'  'chunk_lines',80) 'chunk_lines_overlap',15) 'max_chars',4000)

        :param splitter_type:
        :param verbose:
        :param kwargs:
        """
        project_name = type if isinstance(type, str) else type.value


        if project_name == 'sentence':
            chunk_size = pop_get(kwargs, 'chunk_size', 404)
            chunk_overlap = pop_get(kwargs, 'chunk_overlap', 20)
            separator = pop_get(kwargs, 'separator', ' ')
            if verbose:
                print(f'''Params : [ chunk_size={chunk_size} 
                                     chunk_overlap={chunk_overlap} 
                                     separator={separator} ]''')
            splitter = SentenceSplitter.from_defaults(chunk_size=chunk_size, chunk_overlap=chunk_overlap,
                                                      separator=separator, **kwargs)

        elif project_name == 'sentence_window':
            window_size = kwargs.get("window_size", 3)
            window_metadata_key = kwargs.get("window_metadata_key", "window")
            original_text_metadata_key = kwargs.get("original_text_metadata_key", "original_sentence")
            if verbose:
                print(f'''Params : [ window_size={window_size} window_metadata_key={window_metadata_key} original_text_metadata_key={original_text_metadata_key} ]''')
            # 这对于生成具有非常特定范围的嵌入最有用。然后，结合MetadataReplacementNodePostProcessor，您可以在将节点发送到LLM之前将句子替换为周围的上下文。
            splitter = SentenceWindowNodeParser.from_defaults(
                window_size=window_size,# how many sentences on either side to capture
                window_metadata_key=window_metadata_key,# the metadata key that holds the window of surrounding sentences
                original_text_metadata_key=original_text_metadata_key,# the metadata key that holds the original sentence
            )

        elif project_name == 'token_text':
            chunk_size = pop_get(kwargs,'chunk_size',404)
            chunk_overlap = pop_get(kwargs, 'chunk_overlap', 20)
            separator = pop_get(kwargs, 'separator', ' ')
            if verbose:
                print(f'''Params : [ chunk_size={chunk_size} 
                                     chunk_overlap={chunk_overlap} 
                                     separator={separator} ]''')
            splitter = TokenTextSplitter.from_defaults(chunk_size=chunk_size, chunk_overlap=chunk_overlap, separator=separator, **kwargs)

        elif project_name == 'mark_custom':
            if verbose:
                print(f'Params : [ mark={kwargs.get("mark","##")} ]')
            splitter = MarkSplitter(mark=kwargs.get('mark','##'))

        elif project_name == 'hierarchical':
            splitter = HierarchicalNodeParser.from_defaults(chunk_sizes=kwargs.get('chunk_sizes',[2048, 512, 128]))


        elif project_name == 'code':
            # code
            language = kwargs.get('language','python')
            chunk_lines = kwargs.get('chunk_lines',80)
            chunk_lines_overlap = kwargs.get('chunk_lines_overlap',15)
            max_chars = kwargs.get('max_chars',4000)
            splitter = CodeSplitter(
                language=language,
                chunk_lines=chunk_lines,  # lines per chunk
                chunk_lines_overlap=chunk_lines_overlap,  # lines overlap between chunks
                max_chars=max_chars,  # max chars per chunk
                **kwargs
            )

        elif project_name == 'markdown':
            splitter = MarkdownNodeParser.from_defaults(include_metadata = kwargs.get('include_metadata', True),
                                                        include_prev_next_rel = kwargs.get('include_prev_next_rel', True),
                                                        callback_manager = kwargs.get('callback_manager', None))

        elif project_name == 'json':
            splitter = JSONNodeParser.from_defaults(include_metadata = kwargs.get('include_metadata', True),
                                                    include_prev_next_rel = kwargs.get('include_prev_next_rel', True),
                                                    callback_manager = kwargs.get('callback_manager', None),)

        elif project_name == 'html':
            splitter = HTMLNodeParser(tags=kwargs.get('tags', ["p", "h1"]))  # optional list of tags
            # 默认标签是：["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "b", "i", "u", "section"]
        elif project_name == 'langchain':
            # langchain
            langchain_splitter = kwargs.get('langchain_splitter',None)
            langchain_splitter = langchain_splitter or RecursiveCharacterTextSplitter
            issubclass(langchain_splitter, TextSplitter)
            splitter = LangchainNodeParser(langchain_splitter())

        # TODO ####################
        # from llama_index.core.node_parser import # 有十几个吧
        elif project_name == 'semantic':



            buffer_size = kwargs.get('buffer_size', 1)
            breakpoint_percentile_threshold = kwargs.get('breakpoint_percentile_threshold', 95)
            embedd = OpenAIEmbedding()# TODO
            splitter = SemanticSplitterNodeParser(buffer_size=buffer_size,
                                                  breakpoint_percentile_threshold=breakpoint_percentile_threshold,
                                                  embed_model=embedd)


        else:
            raise ValueError("Invalid splitter name")
        return splitter


class ExtractorType(Enum):
    TITLE = 'title'
    QUESTIONS_ANSWERED = 'qad'
    SUMMARY = 'summary'
    KEYWORD = 'keyword'
    STUDY = 'study'

    CUSTOM_EXTRACTOR = 'human_custom'
    PPROGRAM_EXTRACTOR = 'PProgram_custom'
    ENTITY = 'entity'

    HELP = f"""
TITLE_EXTRACTOR = 'Title'
QUESTIONS_ANSWERED_EXTRACTOR = 'QuestionsAnswered'
SUMMARY_EXTRACTOR = 'Summary'

TT
    #TODO 做一个实体提取 
    # marven 测试不通 Entity
    # metadata_mode=MetadataMode.EMBED, num_workers=8
    # list of summaries to extract: 'self', 'prev', 'next'
"""

class ExtractorFactory:
    def __new__(cls, type:ExtractorType or str, verbose=False,**kwargs):
        project_name = type if isinstance(type, str) else type.value

        if project_name == 'title':
            nodes = pop_get(kwargs,'nodes',5)
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')

            return TitleExtractor(nodes=nodes, llm=llm,**kwargs)
        elif project_name == 'qad':
            questions = pop_get(kwargs,'questions',3)
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ questions={questions} 
                                     llm={llm} ]''')
            return QuestionsAnsweredExtractor(questions=questions, llm=llm)
        elif project_name == 'summary':
            summaries = pop_get(kwargs,'summaries',["prev", "self"])
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ summaries={summaries} 
                                     llm={llm} ]''')
            return SummaryExtractor(summaries=summaries, llm=llm)
        elif project_name == 'keyword':
            keywords = pop_get(kwargs,'keywords',10)
            llm = pop_get(kwargs,'llm',None)
            if verbose:
                print(f'''Params : [ keywords={keywords} 
                                     llm={llm} ]''')
            return KeywordExtractor(keywords=keywords, llm=llm)
        elif project_name == 'study':
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ llm={llm} ]''')
            return StudyExtractor(llm=llm)

        elif project_name == 'human_custom':
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ llm={llm} ]''')
            return HumanExtractor()

        elif project_name == 'PProgram_custom':
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ llm={llm} ]''')
            return PProgramExtractor(llm=llm)
        elif project_name == 'entity':
            return  EntityExtractor(
                prediction_threshold=0.5,
                label_entities=False,  # include the entity label in the metadata (can be erroneous)
                device="cpu",  # set to "cuda" if you have a GPU
            )
        else:
            raise ValueError(f'Invalid extractor type: {project_name}')


# 有一批效果可能更好的付费embedding

class EmbeddingType(Enum):
    openai = 'openai'
    FastEmbedEmbedding = 'FastEmbedEmbedding'
    TextEmbeddingsInference = 'TextEmbeddingsInference'
    InstructorEmbedding = 'InstructorEmbedding'
    HuggingFaceEmbedding = 'HuggingFaceEmbedding'
class EmbeddingFactory:
    def __new__(cls, type:EmbeddingType,verbose=False,**kwargs):
        # "sentence-transformers/all-mpnet-base-v2"
        # TODO API制作

        project_name = type if isinstance(type, str) else type.value

        if project_name == 'openai':
            api_key = pop_get(kwargs,'apt_key',os.environ.get('WildCard_API_KEY'))
            api_base = pop_get(kwargs,'api_base',"https://api.gptsapi.net/v1")
            return OpenAIEmbedding(api_base=api_base,api_key=api_key,**kwargs)

        elif project_name == 'FastEmbedEmbedding':
            from llama_index.embeddings.fastembed import FastEmbedEmbedding
            embed_model = FastEmbedEmbedding(model_name=kwargs.get('model_name',"BAAI/bge-small-en-v1.5"))
            return embed_model

        elif project_name == 'TextEmbeddingsInference':
            # TextEmbeddingsInference(model_name="BAAI/bge-large-en-v1.5")
            from llama_index.embeddings.text_embeddings_inference import TextEmbeddingsInference

            embed_model = TextEmbeddingsInference(
                model_name=kwargs.get('model_name',"BAAI/bge-small-en-v1.5"),
                timeout=kwargs.get('timeout',60),  # timeout in seconds
                embed_batch_size=kwargs.get('embed_batch_size',10),  # batch size for embedding
            )
            return embed_model



        elif project_name == 'InstructorEmbedding':
            """
            InstructorEmbedding
            讲师嵌入是一类经过专门训练以根据指令增强其嵌入的嵌入。默认情况下，查询为query_instruction="表示用于检索支持文档的问题:"，文本为text_instruction="表示用于检索的文档:"。
            它们依赖于Instructor和SentenceTransformers(2.2.2版本)pip包，您可以使用pip install InstructorEmbedding和pip install -U sentence-transformers==2.2.2来安装它们。
            """

            from llama_index.embeddings.instructor import InstructorEmbedding
            from llama_index.embeddings.huggingface_optimum import OptimumEmbedding
            embed_model = InstructorEmbedding(model_name="hkunlp/instructor-base")

        elif project_name == 'OptimumEmbedding':
            """
            OptimumEmbedding  使用 onnx 格式对模型进行提速
            最优的HuggingFace库导出和运行HuggingFace模型在ONNX格式。
            您可以使用pip install transformer optimum[exports]安装依赖项。
            首先，我们需要创建ONNX模型。ONNX模型提供了改进的推理速度，并且可以跨平台使用(例如在TransformersJS中)。
            """
            from llama_index.embeddings.huggingface import HuggingFaceEmbedding
            from llama_index.embeddings.instructor import InstructorEmbedding
            from llama_index.embeddings.huggingface_optimum import OptimumEmbedding
            OptimumEmbedding.create_and_save_optimum_model(
                "BAAI/bge-small-en-v1.5", "./bge_onnx"
            )
            embed_model = OptimumEmbedding(folder_name="./bge_onnx")


        elif project_name == 'ollama_embeding':
            from llama_index.embeddings.ollama import OllamaEmbedding

            ollama_embedding = OllamaEmbedding(
                model_name="llama2",
                base_url="http://localhost:11434",
                ollama_additional_kwargs={"mirostat": 0},
            )
            return ollama_embedding


        elif project_name == 'HuggingFaceEmbedding':
            from llama_index.embeddings.huggingface import HuggingFaceEmbedding
            return HuggingFaceEmbedding(model_name=kwargs.get('model_name',"BAAI/bge-base-en-v1.5"),
                                        max_length=kwargs.get('max_length','1000'))


class DocStoreType(Enum):
    Simple = 'Simple'
    Elasticsearch = 'Elasticsearch'
    Firestore = 'Firestore'


class DocStoreFactory:
    def __new__(cls, type:DocStoreType,verbose=False,**kwargs):
        project_name = type if isinstance(type, str) else type.value

        if project_name == 'Simple':
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            docstore = SimpleDocumentStore()
            return docstore
        elif project_name == 'Elasticsearch':
            # 要做成API
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            kvstore = ElasticsearchKVStore()
            docstore = ElasticsearchDocumentStore(kvstore)
            return docstore

        elif project_name == 'Firestore':
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            kvstore = FirestoreKVStore()
            docstore = FirestoreDocumentStore(kvstore)
            return docstore


class IndexStoreType(Enum):
    Simple = 'Simple'
    Elasticsearch = 'Elasticsearch'
    Firestore = 'Firestore'


class IndexStoreFactory:
    def __new__(cls, type: IndexStoreType, verbose=False, **kwargs):
        project_name = type if isinstance(type, str) else type.value

        if project_name == 'Simple':
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            index_store = SimpleIndexStore()
            return index_store
        elif project_name == 'Elasticsearch':
            # 要做成API
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            kvstore = ElasticsearchKVStore()
            index_store = ElasticsearchIndexStore(kvstore)
            return index_store

        elif project_name == 'Firestore':
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            kvstore = FirestoreKVStore()
            index_store = FirestoreIndexStore(kvstore)
            return index_store


#####################

class VectorStoreType(Enum):
    Simple = 'Simple'
    Chroma = 'Chroma'
    Elasticsearch = 'Elasticsearch'
    Pinecone = 'Pinecone'

class VectorStoreFactory:
    def __new__(cls, type: VectorStoreType, verbose=False, **kwargs):
        project_name = type if isinstance(type, str) else type.value

        if project_name == 'Simple':
            data = pop_get(kwargs, 'data', None)
            if verbose:
                print(f'''Params : [ data={data} 
                                     ]''')
            vector_store = SimpleVectorStore(data=data,**kwargs)
            return vector_store

        elif project_name == 'Chroma':
            # 要做成API
            # TOOD

            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            db = chromadb.PersistentClient(path="./chroma_db")

            # get collection
            chroma_collection = db.get_or_create_collection("quickstart")

            # assign chroma as the vector_store to the context
            vector_store = ChromaVectorStore(chroma_collection=chroma_collection,**kwargs)
            return vector_store

        elif project_name == 'Elasticsearch':
            # 要做成API
            index_name = pop_get(kwargs, 'index_name', None)
            es_client = pop_get(kwargs, 'es_client', None)
            if verbose:
                print(f'''Params : [ index_name={index_name} 
                                     es_client={es_client} ]''')

            vector_store = ElasticsearchStore(index_name=index_name,es_client=es_client,**kwargs)

            return vector_store

        elif project_name == 'Pinecone':
            pinecone_index = pop_get(kwargs, 'pinecone_index', None)
            api_key = pop_get(kwargs, 'api_key', None)
            if verbose:
                print(f'''Params : [ pinecone_index={pinecone_index} 
                                     api_key={api_key} ]''')
            vector_store = PineconeVectorStore(pinecone_index=pinecone_index,api_key=api_key,**kwargs)
            return vector_store
        else:
            pass

class StorageContextFactory():
    def __new__(cls, docstore=None, index_store=None, vector_stores=None, graph_store=None,persist_dir=None, **kwargs):

        storage_context = StorageContext.from_defaults(docstore=docstore,
                                                       index_store=index_store,
                                                       vector_stores=vector_stores,
                                                       graph_store=graph_store,
                                                       persist_dir=persist_dir,
                                                       **kwargs)
        return storage_context
    @staticmethod
    def build_index_from_storage(storage_context,**kwargs):
        index = load_index_from_storage(storage_context,**kwargs)
        return index

# graph.root_index.storage_context.persist(persist_dir="<persist_dir>")




# from llama_index.core.memory import ChatMemoryBuffer
#
# memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
# chat_engine = index.as_chat_engine(chat_mode="openai",memory=memory)# chat_mode="best",

class ChatStoreType(Enum):
    Simple = 'Simple'
    Redis = 'Redis'

class ChatStoreFactory:
    def __new__(cls, chatstore_type: ChatStoreType, verbose=False, **kwargs):
        project_name = type if isinstance(type, str) else type.value

        if chatstore_type == 'Simple':
            chat_store = SimpleChatStore()
        elif chatstore_type == 'Redis':
            # 要做成API
            redis_url = pop_get(kwargs, 'redis_url', "redis://localhost:6379")
            ttl = pop_get(kwargs, 'ttl', 300)
            if verbose:
                print(f'''Params : [ redis_url={redis_url}  ttl={ttl} ]''')
            chat_store = RedisChatStore(redis_url=redis_url, ttl=ttl, **kwargs)
        else:
            chat_store = SimpleChatStore()
        return chat_store



    @staticmethod
    def use_chat_store(chat_store,token_limit=3000,chat_store_key="user1"):
        chat_memory = ChatMemoryBuffer.from_defaults(
            token_limit=token_limit,
            chat_store=chat_store,
            chat_store_key=chat_store_key,
        )
        return chat_memory

    @staticmethod
    def persist(chat_store,persist_path="chat_store.json"):
        chat_store.persist(persist_path=persist_path)

    @staticmethod
    def load(persist_path="chat_store.json"):
        loaded_chat_store = SimpleChatStore.from_persist_path(
            persist_path=persist_path
        )
        return loaded_chat_store

    @staticmethod
    def to_json(chat_store):
        chat_store_string = chat_store.json()
        return chat_store_string

    @staticmethod
    def build_from_json(self,chat_store_string):
        return SimpleChatStore.parse_raw(chat_store_string)



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
        from llama_index.core.objects import ObjectIndex
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
        from llama_index.core.vector_stores import MetadataFilters, ExactMatchFilter
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
