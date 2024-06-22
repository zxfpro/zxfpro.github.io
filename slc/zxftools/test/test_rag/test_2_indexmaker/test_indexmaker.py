import unittest
import timeit

from zxftools.rag import



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



