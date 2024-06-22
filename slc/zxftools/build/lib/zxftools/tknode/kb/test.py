import unittest
from .load_data import *
from .indexmaker import *
from .enginemaker import *
from .utils import convert_kb_to_mb_gb
# 执行时间、内存使用、CPU使用率
# 正向测试
# 反向测试(无)

import timeit
import resource

class LoadDataTests(unittest.TestCase):
    data_path  = '/Users/zhaoxuefeng/GitHub/zxftools/zxftools/tknode/rag/data/'
    def test_is_url(self):
        result = is_url('https://docs.llamaindex.ai/')
        self.assertTrue(result)

    def test_Reader(self):

        #PDFUrlReader
        reader = DirectoryRecursiveReader(self.data_path)
        assert len(reader.load_data()) > 3
        reader = DirectoryReader(self.data_path)
        assert len(reader.load_data()) > 3
        reader = SampleFireReader(os.path.join(self.data_path,'paul_graham_essay.txt'))
        assert len(reader.load_data()) ==1
        reader = PDFUrlReader('https://arxiv.org/pdf/1705.07552')
        assert len(reader.load_data()) > 3

    def test_ReaderTime_Memory(self):
        def work1():
            reader = DirectoryRecursiveReader(self.data_path)
            assert len(reader.load_data()) > 3

        mem_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        execution_time = timeit.timeit(work1, number=1)
        mem_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        size, unit = convert_kb_to_mb_gb(mem_after - mem_before)
        print(f"内存使用：{size} {unit}")
        print(f"执行时间：{execution_time} 秒")
        self.assertLess(execution_time, 7)

    def test_JsonReader(self):
        reader = JsonReader(os.path.join(self.data_path, 'test.json'))
        result = reader.load_data()
        self.assertIsNotNone(result)

    def test_StrReader(self):
        reader = StrReader("This is a test string")
        result = reader.load_data()
        self.assertIsNotNone(result)

    def test_DictReader(self):
        reader = DictReader({1: "Document 1", 2: "Document 2"})
        result = reader.load_data()
        self.assertEqual(len(result), 2)

    def test_GithubReader(self):
        # 未通过
        reader = GithubReader("ymcui/Chinese-Mixtral/main")
        result = reader.load_data()
        self.assertIsNotNone(result)

    def test_WebReader(self):
        reader = WebReader("https://docs.llamaindex.ai/")
        result = reader.load_data()
        self.assertIsNotNone(result)

    def test_ObsidianlReader(self):
        # 笔记
        reader = ObsidianlReader()
        result = reader.load_data()
        self.assertIsNotNone(result)

    def test_ImageTabularReader(self):
        reader = ImageTabularReader(os.path.join(self.data_path, 'marine_chart.png'))
        result = reader.load_data()
        self.assertIsNotNone(result)

    def test_route(self):
        result = automatic_route_selection(self.data_path)
        self.assertEqual(result,'directory','信息1')

        result = automatic_route_selection(os.path.join(self.data_path, 'test.json'))
        self.assertEqual(result, 'json')

        data = '/path/to/file.txt'
        result = automatic_route_selection(os.path.join(self.data_path, 'chat_stream.py'))
        self.assertEqual(result, 'file')


        data = 'https://arxiv.org/pdf/1705.07552'
        result = automatic_route_selection(data)
        self.assertEqual(result, 'pdfs')


        data = 'https://docs.llamaindex.ai/'
        result = automatic_route_selection(data)
        self.assertEqual(result, 'web')


        data = 'This is a string'
        result = automatic_route_selection(data)
        self.assertEqual(result, 'str')


        data = {'key': 'value'}
        result = automatic_route_selection(data)
        self.assertEqual(result, 'dict')

        data = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        result = automatic_route_selection(data)
        self.assertEqual(result, 'DataFrame')

        data = 'https://github.com/username/repo'
        result = automatic_route_selection(data)
        self.assertEqual(result, 'github')

    # 测试异常
    def test_add_type_error(self):
        with self.assertRaises(TypeError):
            pass
            # add(1, "two")

class SplitterTests(unittest.TestCase):
    data_path = '/Users/zhaoxuefeng/GitHub/zxftools/zxftools/tknode/rag/data/paul_graham_essay.txt'
    documents = load_data(data_path)

    def test_sentence(self):
        splitter = SplitterFactory(SplitterType.SENTENCE)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_sentence_window(self):
        splitter = SplitterFactory(SplitterType.SENTENCE_WINDOW)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_token_text(self):
        splitter = SplitterFactory(SplitterType.TOKEN_TEXT)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_mark(self):
        splitter = SplitterFactory(SplitterType.MARK)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_semantic(self):
        splitter = SplitterFactory(SplitterType.SEMANTIC)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_hierarchical(self):
        splitter = SplitterFactory(SplitterType.HIERARCHICAL)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_code(self):
        splitter = SplitterFactory(SplitterType.CODE)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_markdown(self):
        splitter = SplitterFactory(SplitterType.MARKDOWN)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_json(self):
        splitter = SplitterFactory(SplitterType.JSON)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_html(self):
        splitter = SplitterFactory(SplitterType.HTML)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)

    def test_langchain(self):
        splitter = SplitterFactory(SplitterType.LANGCHAIN)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)


from llama_index.core.schema import Node

class ExtractorTests(unittest.TestCase):
    nodes = [Node(text='这是一个测试'), Node(text='这是一个demo')]

    def test_title(self):
        extra = ExtractorFactory(ExtractorType.Title)
        result = extra.extract(self.nodes)
        self.assertIn('document_title', result[0].keys())

    def test_qad(self):
        extra = ExtractorFactory(ExtractorType.QUESTIONS_ANSWERED)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_summary(self):
        extra = ExtractorFactory(ExtractorType.SUMMARY)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_keyword(self):
        extra = ExtractorFactory(ExtractorType.KEYWORD)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_study(self):
        extra = ExtractorFactory(ExtractorType.STUDY)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_human(self):
        extra = ExtractorFactory(ExtractorType.CUSTOM_EXTRACTOR)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_PProgram(self):
        extra = ExtractorFactory(ExtractorType.PPROGRAM_EXTRACTOR)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)


class EmbeddingTests(unittest.TestCase):
    # Embedding Factory
    def test_EmbeddingFactory(self):
        pass

    def test_IndexMaker(self):
        pass



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



class IndexMaker(unittest.TestCase):
    def test_NodePostprocessorsFactory(self):
        pass




# 运行所有测试
if __name__ == '__main__':
    unittest.main()