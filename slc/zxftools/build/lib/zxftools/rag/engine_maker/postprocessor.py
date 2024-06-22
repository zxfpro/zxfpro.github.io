from llama_index.core.postprocessor import (
    MetadataReplacementPostProcessor,
    LLMRerank,
    SentenceTransformerRerank,
    LongContextReorder,
    FixedRecencyPostprocessor,
    EmbeddingRecencyPostprocessor,
    SentenceEmbeddingOptimizer,
    TimeWeightedPostprocessor,
    SimilarityPostprocessor,
    KeywordNodePostprocessor,
)

from enum import Enum

class NodePostprocessorsType(Enum):
    SimilarityPostprocessor = 'SimilarityPostprocessor'
    KeywordNodePostprocessor = 'Keyword'
    MetadataReplacementPostProcessor = 'metadata_replacement'
    LongContextReorder = 'long_context_reorder'
    FixedRecencyPostprocessor = 'fixed_recency'
    EmbeddingRecencyPostprocessor = 'embedding_recency'
    TimeWeightedPostprocessor = 'time_weighted'
    SentenceEmbeddingOptimizer = 'sentence_embedding_optimizer'
    LLMRerank = 'llm_rerank'
    CohereRerank = 'CohereRerank'
    SentenceTransformerRerank = 'sentence_transformer_rerank'
    # colbert_reranker = 'colbert_reranker'
"""
from llama_index.core.postprocessor import SentenceTransformerRerank

postprocessor = SentenceTransformerRerank(
    model="mixedbread-ai/mxbai-rerank-base-v1", top_n=2
)
"""
# engine = reactagent
class NodePostprocessorsFactory:
    def __new__(cls, postprocessor:NodePostprocessorsType, **kwargs):
        """
        from llama_index.postprocessor.rankgpt_rerank import RankGPTRerank
        from llama_index.postprocessor.colbert_rerank import ColbertRerank
        """
        if postprocessor.value == 'SimilarityPostprocessor':
            postprocessor = SimilarityPostprocessor(similarity_cutoff=kwargs.get('similarity_cutoff',0.75)) # 过滤低分
        elif postprocessor.value == 'Keyword': # 用于确保某些关键字被排除或包含。
            postprocessor = KeywordNodePostprocessor(
                required_keywords=kwargs.get('required_keywords',["Combinator"]),
                exclude_keywords = kwargs.get('exclude_keywords',["Italy"]),
            )
        elif postprocessor.value == 'metadata_replacement': # 使用metadata 中的数据替换text 文本数据
            postprocessor = MetadataReplacementPostProcessor(target_metadata_key=kwargs.get('target_metadata_key',"window"))
        elif postprocessor.value == 'long_context_reorder': # 文本重排 将重点的放到开始和结尾
            postprocessor = LongContextReorder()
        elif postprocessor.value == 'fixed_recency': #按照日期排序的rerank检索
            postprocessor = FixedRecencyPostprocessor()
        elif postprocessor.value == 'embedding_recency': #按照日期排序的rerank检索 同时
            postprocessor = EmbeddingRecencyPostprocessor(date_key="date", similarity_cutoff=0.7)
        elif postprocessor.value == 'time_weighted': # 对每个节点应用时间加权重新排名的前K个节点
            postprocessor = TimeWeightedPostprocessor(time_decay=0.5, time_access_refresh=False, top_k=kwargs.get('top_k', 1))
        elif postprocessor.value == 'sentence_embedding_optimizer':
            postprocessor = SentenceEmbeddingOptimizer(threshold_cutoff=kwargs.get('threshold_cutoff', 0.7))

        # elif postprocessor.value == 'CohereRerank':
        #     reranker = CohereRerank(api_key="<COHERE_API_KEY>", top_n=2)
        elif postprocessor.value == 'llm_rerank':
            postprocessor = LLMRerank(choice_batch_size=5, top_n=2)
            # JinaRerank  #
        elif postprocessor.value == 'sentence_transformer_rerank':
            postprocessor = SentenceTransformerRerank(model=kwargs.get('model', "cross-encoder/ms-marco-MiniLM-L-2-v2"),
                                                      top_n=kwargs.get('top_k', 1))
            # SentenceTransformerRerank(top_n=4, model="BAAI/bge-reranker-base")

        else:
            raise ValueError("Invalid postprocessor name")

        return postprocessor


