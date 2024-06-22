from llama_index.llms.openai import OpenAI as qet_openai
from .engine_baidu import BaiduLLM
from typing import Any, Optional
from llama_index.core import PromptTemplate
import os

def get_llm(type: str = 'openai_wildcard', model: Optional[str] = None, temperature: float = 0.1,
            max_tokens: Optional[int] = None, api_key: Optional[str] = None, **kwargs: Any):
    llm = None

    if type == 'openai_api':
        llm = qet_openai(
            model=model or "gpt-3.5-turbo-0613",
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
    elif type == 'openai_wildcard':
        llm = qet_openai(
            model=model or "gpt-3.5-turbo-0613",
            api_base="https://api.gptsapi.net/v1",
            api_key=api_key or os.environ.get('WildCard_API_KEY'),
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
    elif type == 'openai_bianxieai':
        llm = qet_openai(
            model=model or "gpt-3.5-turbo-0613",
            api_base="https://api.bianxieai.com/v1",
            api_key=api_key or os.environ.get('bianxieai_API_KEY'),
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs
        )
    elif type == 'claude_wildcard':
        try:
            from llama_index.llms.anthropic import Anthropic
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "pip install llama-index-llms-anthropic"')

        llm = Anthropic(
            base_url="https://api.gptsapi.net",
            api_key=api_key or os.environ.get('WildCard_API_KEY'),
            model=model or "claude-3-sonnet-20240229",
            temperature=temperature,
            max_tokens=max_tokens or 100000,
            **kwargs
        )
    elif type == 'baidu':
        llm = BaiduLLM(
            model_name=model or 'mixtral_8x7b',
            temperature=temperature,
            **kwargs
        )
    elif type == 'ollama':

        try:
            from llama_index.llms.ollama import Ollama
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "llama-index-llms-ollama"')

        base_url = kwargs.get('base_url')
        llm = Ollama(
            model=model or "llama3",
            base_url=base_url or 'http://192.168.8.125:11435',
            request_timeout=120.0,
            temperature=temperature,
            **kwargs
        )
    elif type == 'triton':
        try:
            from llama_index.llms.nvidia_triton import NvidiaTriton
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "llama-index-llms-nvidia-triton"')
        llm = NvidiaTriton(
            server_url="localhost:8001",
            model_name=model or "gpt2",
            temperature=temperature,
            tokens=32,
            **kwargs
        )
    elif type == 'huggingface':
        try:
            from llama_index.llms.huggingface import HuggingFaceLLM
        except ModuleNotFoundError as e:
            raise Exception(
                f'{e} please install use "llama-index-llms-huggingface "')

        system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
        - StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
        - StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
        - StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
        - StableLM will refuse to participate in anything that could harm a human.
        """

        query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")

        llm = HuggingFaceLLM(
            context_window=4096,
            max_new_tokens=256,
            generate_kwargs={"temperature": temperature, "do_sample": False},
            system_prompt=system_prompt,
            query_wrapper_prompt=query_wrapper_prompt,
            tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
            model_name=model or "StabilityAI/stablelm-tuned-alpha-3b",
            device_map="auto",
            stopping_ids=[50278, 50279, 50277, 1, 0],
            tokenizer_kwargs={"max_length": 4096},
            **kwargs
        )

    return llm