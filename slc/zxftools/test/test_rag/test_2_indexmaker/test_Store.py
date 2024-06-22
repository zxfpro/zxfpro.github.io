import unittest
import timeit


from zxftools.rag import IndexMaker,IndexType


class DocStoreFactoryTests(unittest.TestCase):

    def test_SimpleDocStore(self):
        docstore = DocStoreFactory('Simple')
        self.assertIsInstance(docstore, SimpleDocumentStore)

    def test_ElasticsearchDocStore(self):
        docstore = DocStoreFactory('Elasticsearch')
        self.assertIsInstance(docstore, ElasticsearchDocumentStore)

    def test_FirestoreDocStore(self):
        docstore = DocStoreFactory('Firestore')
        self.assertIsInstance(docstore, FirestoreDocumentStore)


class IndexStoreFactoryTests(unittest.TestCase):
    def test_SimpleIndexStore(self):
        index_store = IndexStoreFactory('Simple')
        self.assertIsInstance(index_store, SimpleIndexStore)

    def test_ElasticsearchIndexStore(self):
        index_store = IndexStoreFactory('Elasticsearch')
        self.assertIsInstance(index_store, ElasticsearchIndexStore)

    def test_FirestoreIndexStore(self):
        index_store = IndexStoreFactory('Firestore')
        self.assertIsInstance(index_store, FirestoreIndexStore)

    def test_CustomIndexStore(self):
        index_store = IndexStoreFactory('Custom')
        self.assertIsNone(index_store)

class VectorStoreFactoryTests(unittest.TestCase):

    def test_SimpleVectorStore(self):
        vector_store = VectorStoreFactory('Simple', data='data_path')
        self.assertIsNotNone(vector_store)

    def test_ChromaVectorStore(self):
        vector_store = VectorStoreFactory('Chroma', nodes=5, llm='llm_path')
        self.assertIsNotNone(vector_store)

    def test_ElasticsearchStore(self):
        vector_store = VectorStoreFactory('Elasticsearch', index_name='index_name', es_client='es_client')
        self.assertIsNotNone(vector_store)

    def test_PineconeVectorStore(self):
        vector_store = VectorStoreFactory('Pinecone', pinecone_index='pinecone_index', api_key='api_key')
        self.assertIsNotNone(vector_store)

    def test_InvalidVectorStoreType(self):
        vector_store = VectorStoreFactory('InvalidType')
        self.assertIsNone(vector_store)

class ChatStoreFactoryTests(unittest.TestCase):

    def test_use_chat_store(self):
        chat_store = ChatStoreFactory.use_chat_store('Simple')
        self.assertIsNotNone(chat_store)

    def test_persist(self):
        chat_store = ChatStoreFactory.use_chat_store('Simple')
        ChatStoreFactory.persist(chat_store, persist_path="chat_store.json")
        loaded_chat_store = ChatStoreFactory.load(persist_path="chat_store.json")
        self.assertIsNotNone(loaded_chat_store)

    def test_to_json(self):
        chat_store = ChatStoreFactory.use_chat_store('Simple')
        chat_store_string = ChatStoreFactory.to_json(chat_store)
        self.assertIsInstance(chat_store_string, str)

    def test_build_from_json(self):
        chat_store = ChatStoreFactory.use_chat_store('Simple')
        chat_store_string = ChatStoreFactory.to_json(chat_store)
        loaded_chat_store = ChatStoreFactory.build_from_json(chat_store_string)
        self.assertIsNotNone(loaded_chat_store)


