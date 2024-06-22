# TODO

from llama_index.core.llama_dataset import download_llama_dataset
from llama_index.core.llama_dataset.generator import RagDatasetGenerator
from llama_index.core.llama_dataset import (
    LabelledRagDataExample,
    CreatedBy,
    CreatedByType,
)
from llama_index.core.llama_dataset import LabelledRagDataset


class Llama_Dataset():
    def __init__(self):
        """
        rag_dataset.to_pandas()
        rag_dataset.save_json("rag_dataset.json")
        """

    def get_dataset_from_hub(self, dataset_name="PaulGrahamEssayDataset", dataset_cache="./paul_graham"):
        rag_dataset, documents = download_llama_dataset(dataset_name, dataset_cache)
        return rag_dataset, documents

    def get_dataset_from_documents(self, documents, llm, num_questions_per_chunk=2, show_progress=True, ):
        dataset_generator = RagDatasetGenerator.from_documents(
            documents,
            llm=llm,
            num_questions_per_chunk=num_questions_per_chunk,  # set the number of questions per nodes
            show_progress=show_progress,
        )

        rag_dataset = dataset_generator.generate_dataset_from_nodes()
        return rag_dataset, documents

    def get_ragdata_example(self,
                            query="This is a test query, is it not?",
                            query_by='ai',
                            query_by_model_name=None,
                            reference_contexts=["This is a sample context"],
                            reference_answer="Yes it is.",
                            reference_answer_by="human",

                            ):
        # rag_example.json()
        query_by = CreatedBy(type=CreatedByType.AI, model_name="gpt-3.5"),

        if query_by == 'human':
            query_by_ = CreatedBy(type=CreatedByType.HUMAN, model_name=query_by_model_name)
        elif query_by == 'ai':
            query_by_ = CreatedBy(type=CreatedByType.AI, model_name=query_by_model_name)

        if reference_answer_by == 'human':
            reference_answer_by_ = CreatedBy(type=CreatedByType.HUMAN)
        elif reference_answer_by == 'ai':
            reference_answer_by_ = CreatedBy(type=CreatedByType.AI)

        rag_example = LabelledRagDataExample(
            query=query,
            query_by=query_by_,
            reference_contexts=reference_contexts,
            reference_answer=reference_answer,
            reference_answer_by=reference_answer_by_,
        )
        return rag_example

    def get_ragdata_example_from_json(rag_json):
        return LabelledRagDataExample.parse_raw(rag_json)

    def get_ragdata_example_from_dict(rag_dict):
        return LabelledRagDataExample.parse_obj(rag_dict)

    def get_dataset_from_examples(self, rag_examples: list):
        rag_dataset = LabelledRagDataset(examples=rag_examples)

    def get_dataset_from_json(dataset_json):
        rag_dataset = LabelledRagDataset.from_json(dataset_json)
        return rag_dataset

    def test(self, query_engine, rag_dataset):
        """
        使用documents 构建 query_engine
        使用方法 测试query_engine 的生成与基准之间的关系
        """
        # rag_dataset.amake_predictions_with(
        rag_dataset.make_predictions_with(query_engine=query_engine, show_progress=True)