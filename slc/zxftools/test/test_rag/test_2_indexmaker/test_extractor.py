import unittest
import timeit
from zxftools.rag import ExtractorFactory,ExtractorType
from llama_index.core.schema import Node
from qet import get_llm

class ExtractorTests(unittest.TestCase):
    nodes = [Node(text='这是一个测试'), Node(text='这是一个demo')]
    llm = get_llm()
    def test_title(self):

        extra = ExtractorFactory(ExtractorType.TITLE,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIn('document_title', result[0].keys())

    def test_qad(self):
        extra = ExtractorFactory(ExtractorType.QUESTIONS_ANSWERED,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_summary(self):
        extra = ExtractorFactory(ExtractorType.SUMMARY,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_keyword(self):
        extra = ExtractorFactory(ExtractorType.KEYWORD,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_study(self):
        extra = ExtractorFactory(ExtractorType.STUDY,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_human(self):
        # TODO
        extra = ExtractorFactory(ExtractorType.CUSTOM_EXTRACTOR,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_PProgram(self):
        # TODO
        extra = ExtractorFactory(ExtractorType.PPROGRAM_EXTRACTOR,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)

    def test_Entity(self):
        extra = ExtractorFactory(ExtractorType.ENTITY,llm=self.llm)
        result = extra.extract(self.nodes)
        self.assertIsNotNone(result)