
# 评价
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core.schema import TextNode
from tqdm.notebook import tqdm
import pandas as pd

def evaluate(
    dataset,
    embed_model,
    top_k=5,
    verbose=False,
):
    corpus = dataset.corpus
    queries = dataset.queries
    relevant_docs = dataset.relevant_docs

    nodes = [TextNode(id_=id_, text=text) for id_, text in corpus.items()]
    index = VectorStoreIndex(
        nodes, embed_model=embed_model, show_progress=True
    )
    retriever = index.as_retriever(similarity_top_k=top_k)

    eval_results = []
    for query_id, query in tqdm(queries.items()):
        retrieved_nodes = retriever.retrieve(query)
        retrieved_ids = [node.node.node_id for node in retrieved_nodes]
        expected_id = relevant_docs[query_id][0]
        is_hit = expected_id in retrieved_ids  # assume 1 relevant doc

        eval_result = {
            "is_hit": is_hit,
            "retrieved": retrieved_ids,
            "expected": expected_id,
            "query": query_id,
        }
        eval_results.append(eval_result)
    return eval_results


from sentence_transformers.evaluation import InformationRetrievalEvaluator
from sentence_transformers import SentenceTransformer
from pathlib import Path


def evaluate_st(
    dataset,
    model_id,
    name,
):
    corpus = dataset.corpus
    queries = dataset.queries
    relevant_docs = dataset.relevant_docs

    evaluator = InformationRetrievalEvaluator(
        queries, corpus, relevant_docs, name=name
    )
    model = SentenceTransformer(model_id)
    output_path = "results/"
    Path(output_path).mkdir(exist_ok=True, parents=True)
    return evaluator(model, output_path=output_path)



ada = OpenAIEmbedding()
ada_val_results = evaluate(val_dataset, ada)

df_ada = pd.DataFrame(ada_val_results)

df_ada

hit_rate_ada = df_ada["is_hit"].mean()
hit_rate_ada

bge = "local:BAAI/bge-small-en"
bge_val_results = evaluate(val_dataset, bge)

df_bge = pd.DataFrame(bge_val_results)

hit_rate_bge = df_bge["is_hit"].mean()
hit_rate_bge

evaluate_st(val_dataset, "BAAI/bge-small-en", name="bge")



finetuned = "local:test_model"
val_results_finetuned = evaluate(val_dataset, finetuned)

df_finetuned = pd.DataFrame(val_results_finetuned)

hit_rate_finetuned = df_finetuned["is_hit"].mean()
hit_rate_finetuned

evaluate_st(val_dataset, "test_model", name="finetuned")


#评价汇总
df_ada["model"] = "ada"
df_bge["model"] = "bge"
df_finetuned["model"] = "fine_tuned"

df_all = pd.concat([df_ada, df_bge, df_finetuned])
df_all.groupby("model").mean("is_hit")

df_st_bge = pd.read_csv(
    "results/Information-Retrieval_evaluation_bge_results.csv"
)
df_st_finetuned = pd.read_csv(
    "results/Information-Retrieval_evaluation_finetuned_results.csv"
)

df_st_bge["model"] = "bge"
df_st_finetuned["model"] = "fine_tuned"
df_st_all = pd.concat([df_st_bge, df_st_finetuned])
df_st_all = df_st_all.set_index("model")
df_st_all

