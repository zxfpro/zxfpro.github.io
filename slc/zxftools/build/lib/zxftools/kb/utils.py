from llama_index.core.response.notebook_utils import display_source_node
from llama_index.core.response.notebook_utils import display_response
from IPython.display import JSON,display,Markdown

def display_node(node):
    return JSON(node.dict())

def display_json(content):
    display(JSON(content))

def display_source_nodes(result, source_length=1000, show_source_metadata=False):
    for node in result.source_nodes:
        display_source_node(node, source_length, show_source_metadata)

def print_documents(documents):
    from colorama import Fore

    for document in documents:
        print(Fore.GREEN + "Document:" + Fore.RESET)
        print(document.get_text())

def print_document_details(index):
    for id in index.docstore.get_all_document_hashes().values():
        print('\033[34m' + str(id) + '\033[0m')  # id in blue
        print('\033[31m' + str(len(index.docstore.get_node(id).text)) + '\033[0m')  # len in red
        print('\033[32m' + index.docstore.get_node(id).text + '\033[0m')  # text in green

        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

def index_node_id(index):
    return index.index_struct

def documents2text(documents):
    return ''.join([document.text for document in documents])

# define prompt viewing function
def display_prompt_dict(prompts_dict):
    for k, p in prompts_dict.items():
        text_md = f"**Prompt Key**: {k}" f"**Text:** "
        display(Markdown(text_md))
        print(p.get_template())
        display(Markdown(""))

def convert_kb_to_mb_gb(kb):
    mb = kb / 1024
    gb = mb / 1024
    if gb >= 1:
        return gb, "GB"
    elif mb >= 1:
        return mb, "MB"
    else:
        return kb, "KB"

#可视化
import llama_index
from traceloop.sdk import Traceloop
from traceloop.sdk.decorators import workflow
def visable(type ='traceloop'):
    if type == 'sample':
        # 这个简单的可观察性工具将每个LLM输入 / 输出对打印到终端。当您需要在LLM应用程序上快速启用调试日志记录时，最有用。
        llama_index.core.set_global_handler("simple")
    elif type == 'traceloop':
        Traceloop.init(disable_batch=True, api_key="ab0ae62b7b82304dbbad13dccbc0387e87c5ae46e4c5d865cacc9d0dda3244f78992d4a8aed94c1f81e643638effbc8a")

        # @workflow(name="suggest_answers")
        # def suggest_answers(question: str):
        #     print(question)

