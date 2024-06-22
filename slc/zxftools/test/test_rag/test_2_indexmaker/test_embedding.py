import unittest
import timeit

from zxftools.rag import EmbeddingFactory,EmbeddingType


class EmbeddingTests(unittest.TestCase):
    # Embedding Factory
    def test_OpenaiEmbedding(self):
        ebd = EmbeddingFactory(EmbeddingType.openai)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)


    def test_FastEmbedding(self):
        ebd = EmbeddingFactory(EmbeddingType.FastEmbedEmbedding)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)

    def test_TextEmbeddingInference(self):
        ebd = EmbeddingFactory(EmbeddingType.TextEmbeddingsInference)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)

    def test_InstructorEmbedding(self):
        ebd = EmbeddingFactory(EmbeddingType.InstructorEmbedding)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)


    def test_InstructorEmbedding(self):
        ebd = EmbeddingFactory(EmbeddingType.InstructorEmbedding)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)

    def test_ollama_embeding(self):
        ebd = EmbeddingFactory(EmbeddingType.ollama_embeding)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)

    def test_HuggingfaceEmbedding(self):
        ebd = EmbeddingFactory(EmbeddingType.HuggingFaceEmbedding)
        result = ebd.get_text_embedding('hello')
        self.assertIsNotNone(result)