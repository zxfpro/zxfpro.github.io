from typing import Any, Dict, List, Optional, Sequence, cast
from llama_index.core import QueryBundle
from llama_index.core.postprocessor.types import BaseNodePostprocessor
from llama_index.core.schema import NodeWithScore

#### demo ####
class DummyNodePostprocessor(BaseNodePostprocessor):
    def _postprocess_nodes(self, nodes: List[NodeWithScore], query_bundle: Optional[QueryBundle]) -> List[NodeWithScore]:
        # subtracts 1 from the score
        for n in nodes:
            n.score -= 1
        return nodes