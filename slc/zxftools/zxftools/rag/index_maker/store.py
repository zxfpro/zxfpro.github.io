from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.vector_stores.simple import SimpleVectorStore
from llama_index.core.storage.index_store.simple_index_store import SimpleIndexStore
from llama_index.core.storage.chat_store import SimpleChatStore
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core import load_index_from_storage,StorageContext
from .utils import pop_get
from enum import Enum

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
            try:
                from llama_index.storage.kvstore.elasticsearch import ElasticsearchKVStore
                from llama_index.storage.docstore.elasticsearch import ElasticsearchDocumentStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-storage-docstore-elasticsearch  or pip install llama-index-storage-kvstore-elasticsearch "')
            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            kvstore = ElasticsearchKVStore()
            docstore = ElasticsearchDocumentStore(kvstore)
            return docstore

        elif project_name == 'Firestore':
            try:
                from llama_index.storage.kvstore.firestore import FirestoreKVStore
                from llama_index.storage.docstore.firestore import FirestoreDocumentStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-storage-docstore-firestore  or pip install llama-index-storage-kvstore-firestore "')

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

            try:
                from llama_index.storage.kvstore.elasticsearch import ElasticsearchKVStore
                from llama_index.storage.index_store.elasticsearch import ElasticsearchIndexStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-storage-index-store-elasticsearch  or pip install llama-index-storage-kvstore-elasticsearch "')

            nodes = pop_get(kwargs, 'nodes', 5)
            llm = pop_get(kwargs, 'llm', None)
            if verbose:
                print(f'''Params : [ nodes={nodes} 
                                     llm={llm} ]''')
            kvstore = ElasticsearchKVStore()
            index_store = ElasticsearchIndexStore(kvstore)
            return index_store

        elif project_name == 'Firestore':
            try:
                from llama_index.storage.kvstore.firestore import FirestoreKVStore
                from llama_index.storage.index_store.firestore import FirestoreIndexStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-storage-index-store-firestore  or pip install llama-index-storage-kvstore-firestore "')

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
            try:
                from llama_index.vector_stores.chroma import ChromaVectorStore
                import chromadb
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-vector-stores-chroma"')

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
            try:
                from llama_index.vector_stores.elasticsearch import ElasticsearchStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-vector-stores-elasticsearch"')

            index_name = pop_get(kwargs, 'index_name', None)
            es_client = pop_get(kwargs, 'es_client', None)
            if verbose:
                print(f'''Params : [ index_name={index_name} 
                                     es_client={es_client} ]''')

            vector_store = ElasticsearchStore(index_name=index_name,es_client=es_client,**kwargs)

            return vector_store

        elif project_name == 'Pinecone':
            try:
                from llama_index.vector_stores.pinecone import PineconeVectorStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-vector-stores-pinecone"')

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
            try:
                from llama_index.storage.chat_store.redis import RedisChatStore
            except ModuleNotFoundError as e:
                raise Exception(f'{e} please install use "pip install llama-index-storage-chat-store-redis"')

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

