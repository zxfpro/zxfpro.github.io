from typing import Any, Dict, List, Optional, Sequence, cast
from llama_index.core.schema import BaseNode, TextNode
from llama_index.core.extractors import BaseExtractor
from llama_index.core.extractors import SummaryExtractor
from tqdm.auto import tqdm
from llama_index.core.async_utils import run_jobs

class StudyExtractor(SummaryExtractor):
    def __init__(self, llm,**kwargs):
        super().__init__(llm=llm,**kwargs,)
    def extract(self, nodes):
        metadata_list = [
            {
                "concept": self.llm.complete(f"{node.text}\n\n  ----------- \n 提炼以上内容中出现的概念,并尝试做出理解"),
                "knowledge": self.llm.complete(f"{node.text}\n\n  ----------- \n 提炼以上内容中的知识"),
            } for node in tqdm(nodes)
        ]
        return metadata_list

    async def _agenerate_node_knowledge(self, node: BaseNode) -> str:
        """Generate a summary for a node."""
        if self.is_text_node_only and not isinstance(node, TextNode):
            return ""

        context_str = node.text
        concept =  await self.llm.acomplete(f"{context_str}\n\n  ----------- \n 提炼以上内容中出现的概念,并尝试做出理解")
        knowledge = await self.llm.acomplete(f"{context_str}\n\n  ----------- \n 提炼以上内容中的知识")

        result = {
            "concept": concept.text,
            "knowledge": knowledge.text,
        }
        return result


    async def aextract(self, nodes) -> List[Dict]:
        keyword_jobs = []
        for node in nodes:
            keyword_jobs.append(self._agenerate_node_knowledge(node))
        metadata_list = await run_jobs(keyword_jobs, show_progress=self.show_progress, workers=self.num_workers)
        return metadata_list


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



#### other ####
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
    def __new__(cls, llm):
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