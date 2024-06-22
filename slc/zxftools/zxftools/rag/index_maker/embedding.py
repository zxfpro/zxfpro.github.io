from llama_index.embeddings.openai import OpenAIEmbedding
from enum import Enum
from .utils import pop_get
import os

# 有一批效果可能更好的付费embedding
class EmbeddingType(Enum):
    openai = 'openai'
    FastEmbedEmbedding = 'FastEmbedEmbedding'
    TextEmbeddingsInference = 'TextEmbeddingsInference'
    InstructorEmbedding = 'InstructorEmbedding'
    HuggingFaceEmbedding = 'HuggingFaceEmbedding'

class EmbeddingFactory:
    def __new__(cls, type: EmbeddingType, verbose=False, **kwargs):
        # "sentence-transformers/all-mpnet-base-v2"
        # TODO API制作

        project_name = type if isinstance(type, str) else type.value

        if project_name == 'openai':
            api_key = pop_get(kwargs, 'api_key', os.environ.get('WildCard_API_KEY'))
            api_base = pop_get(kwargs, 'api_base', "https://api.gptsapi.net/v1")
            return OpenAIEmbedding(api_base=api_base, api_key=api_key, **kwargs)

        elif project_name == 'FastEmbedEmbedding':
            try:
                from llama_index.embeddings.fastembed import FastEmbedEmbedding
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-embeddings-fastembed"')

            model_name = kwargs.get('model_name', "BAAI/bge-small-en-v1.5")
            return FastEmbedEmbedding(model_name=model_name)

        elif project_name == 'TextEmbeddingsInference':
            try:
                from llama_index.embeddings.text_embeddings_inference import TextEmbeddingsInference
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-embeddings-text-embeddings-inference"')

            model_name = kwargs.get('model_name', "BAAI/bge-small-en-v1.5")
            timeout = kwargs.get('timeout', 60)  # timeout in seconds
            embed_batch_size = kwargs.get('embed_batch_size', 10)  # batch size for embedding
            return TextEmbeddingsInference(model_name=model_name, timeout=timeout, embed_batch_size=embed_batch_size)

        elif project_name == 'InstructorEmbedding':
            try:
                from llama_index.embeddings.instructor import InstructorEmbedding
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-embeddings-instructor"')

            model_name = kwargs.get('model_name', "hkunlp/instructor-base")
            return InstructorEmbedding(model_name=model_name)

        elif project_name == 'OptimumEmbedding':
            try:
                from llama_index.embeddings.huggingface_optimum import OptimumEmbedding
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-embeddings-huggingface-optimum"')

            model_name = kwargs.get('model_name', "BAAI/bge-small-en-v1.5")
            folder_name = kwargs.get('folder_name', "./bge_onnx")
            OptimumEmbedding.create_and_save_optimum_model(model_name, folder_name)
            return OptimumEmbedding(folder_name=folder_name)

        elif project_name == 'ollama_embeding':
            try:
                from llama_index.embeddings.ollama import OllamaEmbedding
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-embeddings-ollama"')

            model_name = kwargs.get('model_name', "llama2")
            base_url = kwargs.get('base_url', "http://localhost:11434")
            ollama_additional_kwargs = kwargs.get('ollama_additional_kwargs', {"mirostat": 0})
            return OllamaEmbedding(model_name=model_name, base_url=base_url, ollama_additional_kwargs=ollama_additional_kwargs)

        elif project_name == 'HuggingFaceEmbedding':
            try:
                from llama_index.embeddings.huggingface import HuggingFaceEmbedding
            except ModuleNotFoundError as e:
                raise Exception(
                    f'{e} please install use "pip install llama-index-embeddings-huggingface"')

            model_name = kwargs.get('model_name', "BAAI/bge-base-en-v1.5")
            max_length = kwargs.get('max_length', 1000)
            return HuggingFaceEmbedding(model_name=model_name, max_length=max_length)

        else:
            raise ValueError(f"Unknown embedding type: {project_name}")

