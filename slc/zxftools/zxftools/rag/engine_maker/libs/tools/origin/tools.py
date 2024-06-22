# from llama_hub.tools.bing_search import BingSearchToolSpec
# Exa
from llama_hub.tools.arxiv import ArxivToolSpec
from llama_hub.tools.wikipedia import WikipediaToolSpec
from llama_hub.tools.code_interpreter import CodeInterpreterToolSpec

from llama_hub.tools.python_file import PythonFileToolSpec

from llama_index.core.tools.tool_spec.load_and_search import LoadAndSearchToolSpec
from llama_hub.tools.multion import MultionToolSpec
from llama_index.core.tools.ondemand_loader_tool import OnDemandLoaderTool
from llama_hub.tools.openapi import OpenAPIToolSpec
from llama_hub.tools.requests import RequestsToolSpec
from llama_hub.tools.vector_db import VectorDBToolSpec

import os

def CusTavilyToolSpec():
    from llama_hub.tools.tavily_research import TavilyToolSpec
    return TavilyToolSpec(os.environ.get('TAVILY_API_KEY'))

def CusAzureSpeechToolSpec():
    from llama_hub.tools.azure_speech import AzureSpeechToolSpec
    return AzureSpeechToolSpec(os.environ.get('SPEECH_REGION'),os.environ.get('SPEECH_KEY'))


