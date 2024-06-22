from llama_index.core.schema import NodeWithScore
from llama_index.retrievers.bm25 import BM25Retriever

class CharacterMatchRetriever(BM25Retriever):
    def _get_scored_nodes(self, query: str):
        nodes = []
        for i, node in enumerate(self._nodes):
            if query == node.text:
                nodes.append(NodeWithScore(node=node, score=1.0))
            else:
                if query in node.text:
                    nodes.append(NodeWithScore(node=node, score=0.9))
                else:
                    nodes.append(NodeWithScore(node=node, score=0.1))
        return nodes



##### Demo #####
from llama_index.core.retrievers import BaseRetriever
class HybridRetriever(BaseRetriever):
    def __init__(self, vector_retriever, bm25_retriever):
        self.vector_retriever = vector_retriever
        self.bm25_retriever = bm25_retriever
        super().__init__()

    def _retrieve(self, query, **kwargs):
        bm25_nodes = self.bm25_retriever.retrieve(query, **kwargs)
        vector_nodes = self.vector_retriever.retrieve(query, **kwargs)

        # combine the two lists of nodes
        all_nodes = []
        node_ids = set()
        for n in bm25_nodes + vector_nodes:
            if n.node.node_id not in node_ids:
                all_nodes.append(n)
                node_ids.add(n.node.node_id)
        return all_nodes
