"""
# llmopenai = OpenAI(model="gpt-3.5-turbo-0613")
"""
from llama_index.core.llms.callbacks import llm_completion_callback
from typing import Any

from llama_index.core.llms import (
    CustomLLM,
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
)
import qet

class BaiduLLM(CustomLLM):
    context_window: int = 3900
    num_output: int = 256
    model_name: str = 'mixtral_8x7b'
    response: str = "My response"
    Baidu_API_Key: str = 'aHGDC5XXmJc9KvlmyMttFyc6'
    Baidu_Secret_Key: str = 'YFrHL23ltPtIeXbYcqYmXDdpkOiP1yWj'
    temperature: int = 0.2
    top_p: float = 0.9
    top_k: int = 50
    penalty_score: float = 1.0
    stop = []

    def __init__(self, temperature=0.2, model_name='mixtral_8x7b', top_p=0.9,
                 top_k=50, penalty_score=1.0, stop=[]):
        super().__init__()
        self.temperature = temperature
        self.model_name = model_name
        self.top_p = top_p
        self.top_k = top_k
        self.penalty_score = penalty_score
        self.stop = stop

    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        prompt = f" {prompt}"
        response = qet.baidu_chat(prompt, model_name=self.model_name,
                                  Baidu_API_Key=self.Baidu_API_Key,
                                  Baidu_Secret_Key=self.Baidu_Secret_Key,
                                  temperature=self.temperature,
                                  top_p=self.top_p,
                                  top_k=self.top_k,
                                  penalty_score=self.penalty_score,
                                  stop=self.stop,
                                  stream=False)
        self.response = response
        return CompletionResponse(text=self.response)

    @llm_completion_callback()
    def stream_complete(
            self, prompt: str, **kwargs: Any
    ) -> CompletionResponseGen:
        self.response = qet.baidu_chat(prompt, model_name=self.model_name,
                                       Baidu_API_Key=self.Baidu_API_Key,
                                       Baidu_Secret_Key=self.Baidu_Secret_Key,
                                       temperature=self.temperature,
                                       top_p=self.top_p,
                                       top_k=self.top_k,
                                       penalty_score=self.penalty_score,
                                       stop=self.stop,
                                       stream=False)
        response = ""
        for token in self.response:
            response += token
            yield CompletionResponse(text=response, delta=token)

