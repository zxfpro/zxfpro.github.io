# MultiModal
from llama_index.llms.anthropic import Anthropic
from llama_index.multi_modal_llms.anthropic import AnthropicMultiModal
from llama_index.core import SimpleDirectoryReader
from llama_index.multi_modal_llms.openai import OpenAIMultiModal
from llama_index.multi_modal_llms.replicate import ReplicateMultiModal
from llama_index.core import PromptTemplate
import os

# qa_tmpl_str = (
#     "Images of hand gestures for ASL are provided.\n"
#     "---------------------\n"
#     "{context_str}\n"
#     "---------------------\n"
#     "If the images provided cannot help in answering the query\n"
#     "then respond that you are unable to answer the query. Otherwise,\n"
#     "using only the context provided, and not prior knowledge,\n"
#     "provide an answer to the query."
#     "Query: {query_str}\n"
#     "Answer: "
# )
# qa_tmpl = PromptTemplate(qa_tmpl_str)
# text_qa_template=qa_tmpl






def get_multi_modal_llms(type='claude_wildcard',model = None,temperature=0.1,max_tokens=None,api_key = None,**kwargs):
    if type == 'openai_api':
        mm_llm = OpenAIMultiModal(
            model="gpt-4-vision-preview",
            max_new_tokens=300,
        )

    elif type == 'claude_wildcard':
        mm_llm = AnthropicMultiModal(
            model=model or "claude-3-sonnet-20240229",
            api_base="https://api.gptsapi.net",
            api_key=api_key or os.environ.get('WildCard_API_KEY'),
            max_tokens=max_tokens or 100000,
            **kwargs
            )
    elif type == 'Replicate':
        mm_llm = ReplicateMultiModal(
            model="yorickvp/llava-13b:2facb4a474a0462c15041b78b1ad70952ea46b5ec6ad29583c0b29dbd4249591",
            max_new_tokens=300,
        )

    return mm_llm


if __name__ == '__main__':
    image_documents = SimpleDirectoryReader(
        input_files=['prometheus_paper_card.png']
    ).load_data()
    response = mm_llm.complete(
        prompt="Describe the images as an alternative text",
        image_documents=image_documents,
    )

