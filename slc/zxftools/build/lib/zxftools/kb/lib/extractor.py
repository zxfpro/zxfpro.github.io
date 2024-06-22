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
# marvin

"""

%pip install llama-index-extractors-marvin

from llama_index.core import SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.extractors.marvin import MarvinMetadataExtractor

from zxftools_dev.rag.load_data import load_data

documents = load_data('ai-bill-of-rights.pdf')


# limit document text length
documents[0].text = documents[0].text[:10000]

import marvin
from marvin import ai_model

from llama_index.core.bridge.pydantic import BaseModel, Field

marvin.settings.openai.api_key = os.environ["OPENAI_API_KEY"]


@ai_model
class SportsSupplement(BaseModel):
    name: str = Field(..., description="The name of the sports supplement")
    description: str = Field(
        ..., description="A description of the sports supplement"
    )
    pros_cons: str = Field(
        ..., description="The pros and cons of the sports supplement"
    )

llm_model = "gpt-3.5-turbo"

# construct text splitter to split texts into chunks for processing
# this takes a while to process, you can increase processing time by using larger chunk_size
# file size is a factor too of course
node_parser = TokenTextSplitter(
    separator=" ", chunk_size=512, chunk_overlap=128
)

# create metadata extractor
metadata_extractor = MarvinMetadataExtractor(
    marvin_model=SportsSupplement, llm_model_string=llm_model
)  # let's extract custom entities for each node.

# use node_parser to get nodes from the documents
from llama_index.core.ingestion import IngestionPipeline

pipeline = IngestionPipeline(transformations=[node_parser, metadata_extractor])

nodes = pipeline.run(documents=documents, show_progress=True)

"""