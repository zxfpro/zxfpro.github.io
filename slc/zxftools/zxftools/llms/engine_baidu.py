from llama_index.core.llms.callbacks import llm_completion_callback
from typing import Any
from llama_index.core.llms import (
    CustomLLM,
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
)
import requests
import json
import os

convert_dict = {
                'baidu1':'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant',
                'mixtral_8x7b':'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/mixtral_8x7b_instruct',
                'llama3:70b':'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_3_70b',
                }


def convert_obj_to_str(messages, stream=False, temperature=0.95, top_p=0.8,
                       top_k=50, penalty_score=1.0, stop=[],
                       user_id=None):
    python_obj = {
        'user_id': user_id,
        'stream': stream,
        'messages': messages,
        'temperature': temperature,
        'top_p': top_p,  # 0-1
        'top_k': top_k,  # int
        'penalty_score': penalty_score,  # 1.0-2.0
        'stop': stop,  # 停用词
        'max_tokens': '2',  # 没用

    }
    json_str = json.dumps(python_obj)
    return json_str


def stream_post(request_url, params, headers, show=False):
    response = requests.post(request_url, data=params, headers=headers, stream=True)
    word = ''
    for line in response.iter_lines():
        str_data = line.decode()
        if str_data != '':
            json_str = str_data.split("data: ", 1)[1]
            data_dict = json.loads(json_str)
            if show:
                if data_dict['result'] != '\n' and data_dict['result'] != '':
                    yield data_dict['result']
            else:
                word += data_dict['result']
                yield word


def HTTP_Post(json_str, my_access_token, model_name='baidu0', stream=False, show=False):
    # 自己的服务
    # request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/falv"
    # 系统内置服务

    request_url = convert_dict.get(model_name)
    print(request_url,'request_url')
    try:
        assert request_url
    except Exception as e:
        raise Exception(f'{e} model_name is not support')

    params = json_str
    access_token = my_access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {
        'content-type': 'application/json'
    }

    if stream:
        return stream_post(request_url, params, headers, show=show)
    else:
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            response_json = response.json()
            return response_json
        else:
            print('ERROR: ')
            print(response)


class Baidu_API():
    def __init__(self, Baidu_API_Key=None, Baidu_Secret_Key=None):
        # print('get Baidu_API_Key,Baidu_Secret_Key')
        API_Key = Baidu_API_Key if Baidu_API_Key is not None else os.environ.get('Baidu_API_Key', None)
        Secret_Key = Baidu_Secret_Key if Baidu_Secret_Key is not None else os.environ.get('Baidu_Secret_Key', None)
        if API_Key is None or Secret_Key is None:
            raise ValueError("Baidu_API_Key or Baidu_Secret_Key is not set")
        self.my_access_token = self.get_access_token(API_Key, Secret_Key)

    def get_access_token(self, API_Key, Secret_Key):
        # 获取 get_access_token
        # !curl 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=KXLBVbkcCJmi4Mq8X4HS6ngZ&client_secret=xgR17aCZTYYPEcJg6DM5xjgPw5VNjeis'

        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_Key + '&client_secret=' + Secret_Key
        response = requests.get(host)
        if response:
            response_json = response.json()
            my_access_token = response_json['access_token']
            return my_access_token

    def get_result(self, messages, my_access_token, model_name='baidu0', stream=False, show=False, temperature=0.95,
                   top_p=0.8,
                   top_k=50, penalty_score=1.0, stop=[], user_id=None):

        json_str = convert_obj_to_str(messages, stream, temperature=temperature, top_p=top_p,
                                      top_k=top_k, penalty_score=penalty_score, stop=stop, user_id=user_id)
        response_json = HTTP_Post(json_str, my_access_token, model_name=model_name, stream=stream, show=show)
        if stream:
            return response_json
        else:
            result = response_json['result']
            return result

    def chat(self, text, history, model_name='baidu0', temperature=0.95, top_p=0.8,
             top_k=50, penalty_score=1.0, stop=[],
             user_id=None):
        '''
        :param model_name: baidu0 or baidu1
        :return:
        '''
        if history == []:
            messages = [{"role": "user", "content": text}]
        else:
            messages = []
            for i in history:
                messages.append({"role": "user", "content": i[0]})
                messages.append({"role": "assistant", "content": i[1]})
            messages.append({"role": "user", "content": text})
        result = self.get_result(messages, self.my_access_token, model_name=model_name, stream=False,
                                 temperature=temperature, top_p=top_p,
                                 top_k=top_k, penalty_score=penalty_score, stop=stop,
                                 user_id=user_id)
        return result

    def stream_chat(self, text, history, model_name='baidu0', show=False, temperature=0.95, top_p=0.8,
                    top_k=50, penalty_score=1.0, stop=[],
                    user_id=None):
        if history == []:
            messages = [{"role": "user", "content": text}]
        else:
            messages = []
            for i in history:
                messages.append({"role": "user", "content": i[0]})
                messages.append({"role": "assistant", "content": i[1]})

        result = self.get_result(messages, self.my_access_token, model_name=model_name, stream=True, show=show,
                                 temperature=temperature, top_p=top_p,
                                 top_k=top_k, penalty_score=penalty_score, stop=stop,
                                 user_id=user_id)
        return result



class BaiduLLM(CustomLLM):
    context_window: int = 3900
    num_output: int = 256
    model_name: str = 'mixtral_8x7b'
    temperature: int = 0.2
    top_p: float = 0.9
    top_k: int = 50
    penalty_score: float = 1.0
    stop = []

    def __init__(self, Baidu_API_Key=None, Baidu_Secret_Key=None, temperature=0.2, 
                       model_name='mixtral_8x7b', top_p=0.9,
                       top_k=50, penalty_score=1.0, stop=[]):
        super().__init__()
        object.__setattr__(self, 'baidu_api', Baidu_API(Baidu_API_Key, Baidu_Secret_Key))
        self.temperature = temperature
        self.model_name = model_name
        self.top_p = top_p
        self.top_k = top_k
        self.penalty_score = penalty_score
        self.stop = stop

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        response = self.baidu_api.chat(prompt, [], model_name=self.model_name, temperature=self.temperature, 
                                       top_p=self.top_p, top_k=self.top_k, penalty_score=self.penalty_score, 
                                       stop=self.stop)
        return CompletionResponse(text=response)

    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen:
        response_generate = self.baidu_api.stream_chat(prompt, [], model_name=self.model_name, show=False, 
                                                       temperature=self.temperature, top_p=self.top_p, 
                                                       top_k=self.top_k, penalty_score=self.penalty_score, 
                                                       stop=self.stop)
        response = ""
        for token in response_generate:
            response += token
            yield CompletionResponse(text=response, delta=token)
