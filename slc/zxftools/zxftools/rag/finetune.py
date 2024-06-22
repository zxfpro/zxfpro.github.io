# TODO
import json
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import MetadataMode



train_nodes = load_corpus(TRAIN_FILES, verbose=True)
val_nodes = load_corpus(VAL_FILES, verbose=True)


# 准备 nodes
# Gradient


from llama_index.finetuning import generate_qa_embedding_pairs
from llama_index.core.evaluation import EmbeddingQAFinetuneDataset
from llama_index.llms.openai import OpenAI

from llama_index.finetuning import SentenceTransformersFinetuneEngine


def get_dataset(train_nodes,val_nodes,llm):
    train_dataset = generate_qa_embedding_pairs(
        llm=llm, nodes=train_nodes[:10]
    )
    val_dataset = generate_qa_embedding_pairs(
        llm=llm, nodes=val_nodes[:5]
    )

def load_json():
    train_dataset = EmbeddingQAFinetuneDataset.from_json("train_dataset.json")
    val_dataset = EmbeddingQAFinetuneDataset.from_json("val_dataset.json")


def embedding_fineine():
    finetune_engine = SentenceTransformersFinetuneEngine(
        train_dataset,
        model_id="BAAI/bge-small-en",
        model_output_path="test_model",
        val_dataset=val_dataset,
    )
    return finetune_engine

finetune_engine.finetune()
embed_model = finetune_engine.get_finetuned_model()

embed_model


epochs = 2
for i in range(epochs):
    finetune_engine.finetune()
fine_tuned_model = finetune_engine.get_finetuned_model(max_tokens=100)



ft_llm = finetune_engine.get_finetuned_model(
    max_tokens=500, is_chat_model=True
)

finetune_engine.model_adapter_id

fine_tuned_model._model.delete()
if __name__ == '__main__':
    dataset = get_dataset()
    dataset.save_json("train_dataset.json")







from pydantic import Field
from typing import List


class Citation(BaseModel):
    """Citation class."""

    author: str = Field(
        ..., description="Inferred first author (usually last name"
    )
    year: int = Field(..., description="Inferred year")
    desc: str = Field(
        ...,
        description=(
            "Inferred description from the text of the work that the author is"
            " cited for"
        ),
    )


class Response(BaseModel):
    """List of author citations.

    Extracted over unstructured text.

    """
    citations: List[Citation] = Field(
        ...,
        description=(
            "List of author citations (organized by author, year, and"
            " description)."
        ),
    )


##############


# setup dataset generator
from llama_index.core.evaluation import DatasetGenerator
from llama_index.core import SummaryIndex
from llama_index.core import PromptTemplate
from tqdm.notebook import tqdm
from tqdm.asyncio import tqdm_asyncio

import pickle

fp = open("data/qa_pairs.jsonl", "w")

question_gen_prompt = PromptTemplate(
    """
{query_str}

Context:
{context_str}

Questions:
"""
)

question_gen_query = """\
Snippets from a research paper is given below. It contains citations.
Please generate questions from the text asking about these citations.

For instance, here are some sample questions:
Which citations correspond to related works on transformer models?
Tell me about authors that worked on advancing RLHF.
Can you tell me citations corresponding to all computer vision works? \
"""

qr_pairs = []
node_questions_tasks = []
for idx, node in enumerate(nodes[:39]):
    num_questions = 1  # change this number to increase number of nodes
    dataset_generator = DatasetGenerator(
        [node],
        question_gen_query=question_gen_query,
        text_question_template=question_gen_prompt,
        llm=eval_llm,
        metadata_mode="all",
        num_questions_per_chunk=num_questions,
    )

    task = dataset_generator.agenerate_questions_from_nodes(num=num_questions)
    node_questions_tasks.append(task)
node_questions_lists = await tqdm_asyncio.gather(*node_questions_tasks)

len(node_questions_lists)

node_questions_lists[1]

# [optional] save

pickle.dump(node_questions_lists, open("llama2_questions.pkl", "wb"))

# [optional] load questions
node_questions_lists = pickle.load(open("llama2_questions.pkl", "rb"))

