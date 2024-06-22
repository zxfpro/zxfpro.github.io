import unittest


from zxftools.rag import SplitterFactory,SplitterType
from zxftools.rag import load_data


class SplitterTests(unittest.TestCase):
    data_path = './paul_graham_essay.txt'
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


    def test_hierarchical(self):
        splitter = SplitterFactory(SplitterType.HIERARCHICAL)
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

    def test_code(self):
        data_path = './chat_stream.py'
        doc = load_data(data_path)
        splitter = SplitterFactory(SplitterType.CODE)
        nodes = splitter.get_nodes_from_documents(doc)
        self.assertIsNotNone(nodes)

    def test_semantic(self):
        #欠费了
        splitter = SplitterFactory(SplitterType.SEMANTIC)
        nodes = splitter.get_nodes_from_documents(self.documents)
        self.assertIsNotNone(nodes)