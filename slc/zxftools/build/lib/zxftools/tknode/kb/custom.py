# 1
from llama_index.core.schema import TransformComponent
import re
class TextCleaner(TransformComponent):
    def __call__(self, nodes, **kwargs):
        for node in nodes:
            node.text = re.sub(r"[^0-9A-Za-z ]", "", node.text)
        return nodes


#####################
from llama_index.core.extractors import BaseExtractor

class HumanExtractor(BaseExtractor):
    def extract(self, nodes):
        metadata_list = [
            {
                "human_describe": input('text:\n' + node.text + '\nhuman_describe:\n')
            } for node in nodes
        ]
        return metadata_list

    def aextract(self, nodes):
        metadata_list = [
            {
                "human_describe": input('text:\n' + node.text + '\nhuman_describe:\n')
            } for node in nodes
        ]
        return metadata_list


from pydantic import BaseModel, Field
from typing import List
from llama_index.program.openai import OpenAIPydanticProgram
from llama_index.core.extractors import PydanticProgramExtractor

class NodeMetadata(BaseModel):
    """Node metadata."""

    entities: List[str] = Field(
        ..., description="Unique entities in this text chunk."
    )
    summary: str = Field(
        ..., description="A concise summary of this text chunk."
    )
    contains_number: bool = Field(
        ...,
        description=(
            "Whether the text chunk contains any numbers (ints, floats, etc.)"
        ),
    )
    chinese: bool = Field(
        ...,
        description=(
            "Whether it is Chinese or not"
        ),
    )

class PProgramExtractor:
    def __new__(cls, NodeMetadata,llm):
        openai_program = OpenAIPydanticProgram.from_defaults(
            output_cls=NodeMetadata,
            prompt_template_str="{input}",
            llm = llm
        )
        program_extractor = PydanticProgramExtractor(
            program=openai_program, input_key="input", show_progress=True
        )
        return program_extractor


# program_extractor = PProgramExtractor(NodeMetadata)

# Extractor up up **************************

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

from llama_index.core.retrievers import RouterRetriever
from llama_index.core.tools import RetrieverTool
class RouterRetrievers():
    def __init__(self, retriever_list, description_list, llm):
        self.retriever_list = retriever_list
        self.description_list = description_list
        self.llm = llm
        assert len(retriever_list) == len(description_list)

    def get(self, selector=None, select_multi=True):
        retriever_tools = []
        for retriever, description in zip(self.retriever_list, self.description_list):
            retriever_tools.append(RetrieverTool.from_defaults(
                retriever=retriever,
                description=description
            ))
        retriever = RouterRetriever.from_defaults(
            selector=selector or PydanticMultiSelector.from_defaults(llm=self.llm),
            retriever_tools=retriever_tools,
            llm=self.llm,
            select_multi=select_multi,
        )
        return retriever

        self.retriever_chunk = RecursiveRetriever(
            "vector",
            retriever_dict={"vector": vector_retriever_chunk},
            node_dict=all_nodes_dict,
            verbose=True,
        )