

import tqdm

# instantiate the gpt-4 judge
from llama_index.llms.openai import OpenAI
from llama_index.core.evaluation import (
    CorrectnessEvaluator,
    FaithfulnessEvaluator,
    RelevancyEvaluator,
    SemanticSimilarityEvaluator,
)

import json


from llama_index.core.evaluation import RetrieverEvaluator

# Relevancy Evaluator¶

from llama_index.core import (
    TreeIndex,
    VectorStoreIndex,
    SimpleDirectoryReader,
    Response,
)
from llama_index.llms.openai import OpenAI
from llama_index.core.evaluation import RelevancyEvaluator
from llama_index.core.node_parser import SentenceSplitter

from llama_index.core.evaluation import EvaluationResult


# [optional] load
qa_dataset = EmbeddingQAFinetuneDataset.from_json("pg_eval_dataset.json")







def judge():
    judges = {}

    judges["correctness"] = CorrectnessEvaluator(
        llm=OpenAI(temperature=0, model="gpt-4"),
    )

    judges["relevancy"] = RelevancyEvaluator(
        llm=OpenAI(temperature=0, model="gpt-4"),
    )

    judges["faithfulness"] = FaithfulnessEvaluator(
        llm=OpenAI(temperature=0, model="gpt-4"),
    )
    judges["semantic_similarity"] = SemanticSimilarityEvaluator()



    evals = {
        "correctness": [],
        "relevancy": [],
        "faithfulness": [],
        "context_similarity": [],
    }




    for example, prediction in tqdm.tqdm(
        zip(rag_dataset.examples, prediction_dataset.predictions)
    ):
        correctness_result = judges["correctness"].evaluate(
            query=example.query,
            response=prediction.response,
            reference=example.reference_answer,
        )

        relevancy_result = judges["relevancy"].evaluate(
            query=example.query,
            response=prediction.response,
            contexts=prediction.contexts,
        )

        faithfulness_result = judges["faithfulness"].evaluate(
            query=example.query,
            response=prediction.response,
            contexts=prediction.contexts,
        )

        semantic_similarity_result = judges["semantic_similarity"].evaluate(
            query=example.query,
            response="\n".join(prediction.contexts),
            reference="\n".join(example.reference_contexts),
        )

        evals["correctness"].append(correctness_result)
        evals["relevancy"].append(relevancy_result)
        evals["faithfulness"].append(faithfulness_result)
        evals["context_similarity"].append(semantic_similarity_result)

    # saving evaluations
    evaluations_objects = {
        "context_similarity": [e.dict() for e in evals["context_similarity"]],
        "correctness": [e.dict() for e in evals["correctness"]],
        "faithfulness": [e.dict() for e in evals["faithfulness"]],
        "relevancy": [e.dict() for e in evals["relevancy"]],
    }

    with open("evaluations.json", "w") as json_file:
        json.dump(evaluations_objects, json_file)




import uuid
import re
from llama_index.core.evaluation import LabelledQADataset
from llama_index.core.evaluation import MultiModalRetrieverEvaluator

from llama_index.core.evaluation import get_retrieval_results_df



clip_retriever_evaluator =      MultiModalRetrieverEvaluator.from_metric_names(
    ["mrr", "hit_rate"], retriever=clip_retriever
)

def get_retrieval():
    df = get_retrieval_results_df(
        names=["asl_index-image", "asl_index-text", "asl_text_desc_index"],
        results_arr=[
            eval_results_image,
            eval_results_text,
            eval_results_text_desc,
        ],
    )
    return df


def asl_create_labelled_retrieval_dataset(
    reg_ex, nodes, mode
) -> LabelledQADataset:
    """Returns a QALabelledDataset that provides the expected node IDs
    for every query.

    NOTE: this is specific to the ASL use-case.
    """
    queries = {}
    relevant_docs = {}
    for node in nodes:
        # find the letter associated with the image/text node
        if mode == "image":
            string_to_search = node.metadata["file_path"]
        elif mode == "text":
            string_to_search = node.text
        else:
            raise ValueError(
                "Unsupported mode. Please enter 'image' or 'text'."
            )
        match = re.search(reg_ex, string_to_search)
        if match:
            # build the query
            query = QUERY_STR_TEMPLATE.format(symbol=match.group(1))
            id_ = str(uuid.uuid4())
            # store the query and expected ids pair
            queries[id_] = query
            relevant_docs[id_] = [node.id_]

    return LabelledQADataset(
        queries=queries, relevant_docs=relevant_docs, corpus={}, mode=mode
    )



from llama_index.core.evaluation import GuidelineEvaluator
from llama_index.llms.openai import OpenAI


from llama_index.core.evaluation import DatasetGenerator, RelevancyEvaluator
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Response
from llama_index.llms.openai import OpenAI


# Retrieval Evaluation

from llama_index.core.evaluation import generate_question_context_pairs
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.openai import OpenAI

# 获取retrieve


from llama_index.core.evaluation import (
    generate_question_context_pairs,
    EmbeddingQAFinetuneDataset,
)


from llama_index.core.evaluation import RetrieverEvaluator


def aaaa():
    GUIDELINES = [
        "The response should fully answer the query.",
        "The response should avoid being vague or ambiguous.",
        "The response should be specific and use statistics or numbers when possible.",
    ]

    evaluators = [GuidelineEvaluator(llm=llm, guidelines=guideline) for guideline in GUIDELINES]

    for guideline, evaluator in zip(GUIDELINES, evaluators):
        eval_result = evaluator.evaluate(
            query=sample_data["query"],
            contexts=sample_data["contexts"],
            response=sample_data["response"],
        )
        print("=====")
        print(f"Guideline: {guideline}")
        print(f"Pass: {eval_result.passing}")
        print(f"Feedback: {eval_result.feedback}")


from llama_index.core.llama_pack import download_llama_pack

RagEvaluatorPack = download_llama_pack("RagEvaluatorPack", "./pack")
rag_evaluator = RagEvaluatorPack(
    query_engine=query_engine, rag_dataset=rag_dataset, show_progress=True
)


# 关联评价
# retriver 评价

def aa(llm,index,eval_questions):
    evaluator_gpt4 = RelevancyEvaluator(llm=llm)
    query_engine = index.as_query_engine()
    response_vector = query_engine.query(eval_questions[1])
    eval_result = evaluator_gpt4.evaluate_response(
        query=eval_questions[1], response=response_vector
    )
    return eval_result

def aaa(qa_dataset):
    metrics = ["mrr", "hit_rate", "cohere_rerank_relevancy"]
    retriever_evaluator = RetrieverEvaluator.from_metric_names(
        metrics, retriever=retriever)

    eval_results = await retriever_evaluator.aevaluate_dataset(qa_dataset)

    sample_id, sample_query = list(qa_dataset.queries.items())[0]
    sample_expected = qa_dataset.relevant_docs[sample_id]

    eval_result = retriever_evaluator.evaluate(sample_query, sample_expected)
    print(eval_result)



def bbb():

    evaluator_gpt4 = RelevancyEvaluator(llm=gpt4)

    query_str =  "What battles took place in New York City in the American Revolution?"

    response_vector = query_engine.query(query_str)
    eval_result = evaluator_gpt4.evaluate_response(
        query=query_str, response=response_vector
    )

    evaluator_gpt4.evaluate(
            query=query_str,
            response=response_vector.response,
            contexts=[source_node.get_content()],
        )

def ccc():
    query_engine = index.as_query_engine()

    response_vector = query_engine.query(eval_questions[1])

    evaluator_gpt4 = RelevancyEvaluator(llm=llm)

    eval_result = evaluator_gpt4.evaluate_response(
        query=eval_questions[1], response=response_vector
    )

if __name__ == '__main__':
    # labelled dataset for image retrieval with asl_index.as_retriever()
    qa_dataset_image = asl_create_labelled_retrieval_dataset(
        r"(?:([A-Z]+).jpg)", image_nodes, "image"
    )

    # labelled dataset for text retrieval with asl_index.as_retriever()
    qa_dataset_text = asl_create_labelled_retrieval_dataset(
        r"(?:To sign ([A-Z]+) in ASL:)", text_nodes, "text"
    )

    # labelled dataset for text-desc with asl_text_desc_index.as_retriever()
    qa_dataset_text_desc = asl_create_labelled_retrieval_dataset(
        r"(?:([A-Z]+).jpg)", image_with_text_nodes, "image"
    )

    eval_results_image = await clip_retriever_evaluator.aevaluate_dataset(
        qa_dataset_image
    )
    eval_results_text = await clip_retriever_evaluator.aevaluate_dataset(
        qa_dataset_text
    )
    eval_results_text_desc = await text_desc_retriever_evaluator.aevaluate_dataset(
        qa_dataset_text_desc
    )
