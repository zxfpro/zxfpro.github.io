import unittest
from .enginemaker import *
from .utils import convert_kb_to_mb_gb
# 执行时间、内存使用、CPU使用率
# 正向测试
# 反向测试(无)

import timeit
import resource

class NodePostprocessorsTests(unittest.TestCase):
    def test_pro(self):
        NodePostprocessorsFactory



class NodePostprocessorsFactoryTests(unittest.TestCase):

    def test_SimilarityPostprocessor(self):
        postprocessor = NodePostprocessorsFactory('SimilarityPostprocessor', similarity_cutoff=0.75)
        self.assertIsNotNone(postprocessor)

    def test_KeywordNodePostprocessor(self):
        postprocessor = NodePostprocessorsFactory('Keyword', required_keywords=["Combinator"], exclude_keywords=["Italy"])
        self.assertIsNotNone(postprocessor)

    def test_MetadataReplacementPostProcessor(self):
        postprocessor = NodePostprocessorsFactory('metadata_replacement', target_metadata_key="window")
        self.assertIsNotNone(postprocessor)

    def test_LongContextReorder(self):
        postprocessor = NodePostprocessorsFactory('long_context_reorder')
        self.assertIsNotNone(postprocessor)

    def test_FixedRecencyPostprocessor(self):
        postprocessor = NodePostprocessorsFactory('fixed_recency')
        self.assertIsNotNone(postprocessor)

    def test_EmbeddingRecencyPostprocessor(self):
        postprocessor = NodePostprocessorsFactory('embedding_recency', date_key="date", similarity_cutoff=0.7)
        self.assertIsNotNone(postprocessor)

    def test_TimeWeightedPostprocessor(self):
        postprocessor = NodePostprocessorsFactory('time_weighted', top_k=1)
        self.assertIsNotNone(postprocessor)

    def test_SentenceEmbeddingOptimizer(self):
        postprocessor = NodePostprocessorsFactory('sentence_embedding_optimizer', threshold_cutoff=0.7)
        self.assertIsNotNone(postprocessor)

    def test_LLMRerank(self):
        postprocessor = NodePostprocessorsFactory('llm_rerank', choice_batch_size=5, top_n=2)
        self.assertIsNotNone(postprocessor)

    def test_SentenceTransformerRerank(self):
        postprocessor = NodePostprocessorsFactory('sentence_transformer_rerank', model="cross-encoder/ms-marco-MiniLM-L-2-v2", top_n=1)
        self.assertIsNotNone(postprocessor)

    def test_InvalidPostprocessor(self):
        with self.assertRaises(ValueError):
            postprocessor = NodePostprocessorsFactory('invalid_postprocessor')


class RetrieverFactoryTests(unittest.TestCase):

    def test_RetrieverFactory(self):
        # Test sample retriever
        index = Index()
        retriever = RetrieverFactory(RetrieverType.SAMPLE, index=index)
        self.assertIsInstance(retriever, SampleRetriever)

        # Test BM25 retriever
        retriever = RetrieverFactory(RetrieverType.BM25, index=index)
        self.assertIsInstance(retriever, BM25Retriever)

        # Test CharacterMatchRetriever
        retriever = RetrieverFactory(RetrieverType.CHARACTER_MATCH, index=index)
        self.assertIsInstance(retriever, CharacterMatchRetriever)

        # Test VideoDBRetriever
        retriever = RetrieverFactory(RetrieverType.VIDEO_DB)
        self.assertIsInstance(retriever, VideoDBRetriever)

        # Test VectaraAutoRetriever
        retriever = RetrieverFactory(RetrieverType.VECTARA_AUTO, index=index)
        self.assertIsInstance(retriever, VectaraAutoRetriever)

        # Test RecursiveRetriever
        retriever = RetrieverFactory(RetrieverType.RECURSIVE)
        self.assertIsInstance(retriever, RecursiveRetriever)

    def test_RetrieverFactory_create_by_retrievers(self):
        # Test QueryFusionRetriever
        retrievers = [Retriever1(), Retriever2(), Retriever3()]
        retriever = RetrieverFactory.create_by_retrievers(RetrieverType.QUERY_FUNCTION, retrievers=retrievers)
        self.assertIsInstance(retriever, QueryFusionRetriever)

        # Test AutoMergingRetriever
        retriever = RetrieverFactory.create_by_retrievers(RetrieverType.AUTO_MERGING, retrievers=retrievers)
        self.assertIsInstance(retriever, AutoMergingRetriever)

        # Test RouterRetriever
        selector = PydanticMultiSelector()
        tools = [Tool1(), Tool2(), Tool3()]
        retriever = RetrieverFactory.create_by_retrievers(RetrieverType.ROUTE, llm=selector, tools=tools)
        self.assertIsInstance(retriever, RouterRetriever)


class EngineMakerTests(unittest.TestCase):

    def test_create_engine_by_index(self):
        engine_maker = EngineMaker()
        index = MockIndex()
        engine = engine_maker.create_engine_by_index(index)
        self.assertIsNotNone(engine)

    def test_create_engine_by_retriever(self):
        engine_maker = EngineMaker()
        retriever = MockRetriever()
        response_synthesizer = MockResponseSynthesizer()
        node_postprocessors = [MockNodePostprocessor()]
        engine = engine_maker.create_engine_by_retriever(retriever, response_synthesizer, node_postprocessors)
        self.assertIsNotNone(engine)

    def test_create_engine_by_tools(self):
        engine_maker = EngineMaker()
        engine_tools_map = [{'obj': MockEngineTool, 'des': 'This is a mock engine tool'}]
        selectors = MockSelector()
        engine = engine_maker.create_engine_by_tools(engine_tools_map, selectors)
        self.assertIsNotNone(engine)

    def test_get_nodes_from_index(self):
        engine_maker = EngineMaker()
        index = MockIndex()
        nodes = engine_maker.get_nodes_from_index(index)
        self.assertIsNotNone(nodes)


class EngineMakerTests(unittest.TestCase):
    def test_NodePostprocessorsFactory(self):
        pass

    def test_ResponseSynthesizerFactory(self):
        pass

    def test_RetrieverFactory(self):
        pass

    def test_EngineMaker(self):
        pass




# 运行所有测试
if __name__ == '__main__':
    unittest.main()