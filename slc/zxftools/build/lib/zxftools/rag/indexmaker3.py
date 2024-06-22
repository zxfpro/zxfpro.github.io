from llama_index.embeddings.openai import OpenAIEmbedding
from enum import Enum
import os

def pop_get(dicts,key,default=None):
    if dicts.get(key):
        key_ = dicts.pop(key)
    else:
        key_ = default
    return key_


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

