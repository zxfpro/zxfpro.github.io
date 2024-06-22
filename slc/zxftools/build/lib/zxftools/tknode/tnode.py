
import time
from typing import Optional, List, Mapping, Any

from zxftools.optimize import Optimize
from zxftools import Logger
from zxftools.tknode.llms import BaiduLLM, OpenAI
from zxftools.tknode.config import model_lora_dict
from zxftools.tknode.servers import AgentAPIService
from zxftools.tknode.streamlit_helper import Streamlit_helper

class MustOverridOError(Exception):
    # 错误定义
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class 循环调用(Exception):
    # 错误定义
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TNode(object):
    topic = None
    llm_name = None
    lora = ''
    temperature = 0.2
    top_p = 0.9
    top_k = 50
    penalty_score = 1.0
    stop = []
    recall = True

    flow_data_path = None
    # 任务id = None
    平均耗时 = None
    当前耗时 = None
    平均成本 = None
    当前成本 = None
    失败率 = None
    失败次数 = None
    好评率 = None
    唤起率 = None
    使用次数 = None
    使用百分比 = None
    数据积累条数 = None
    人工标注条数 = None
    AI标注条数 = None
    待标注条数 = None
    opt = Optimize()
    logger = Logger('ff.log')
    test_case_type = 'record'
    cache_home: str = './cache'
    def __init__(self,agentapi_config:dict=None):
        print('2222222222222')
        self.runnodes = RunNodes()
        self.nodename = self.__class__.__name__
        try:
            assert self.llm_name in model_lora_dict.keys() or self.llm_name == None
        except AssertionError as e:
            raise Exception(f"{self.llm_name} 没有被配置 可以使用TNode.get_model_table() 查看相关信息")

        try:
            assert self.lora in (model_lora_dict.get(self.llm_name) or [''])
        except AssertionError as e:
            raise Exception(f"{e} and {self.llm_name} not have lora model {self.lora}")
        self.llm = self._get_llm()
        self.opt = Optimize()
        self.lit_help = Streamlit_helper()
        if agentapi_config:
            self.agentapi   = AgentAPIService(**agentapi_config)

    def _get_llm(self):# TODO 配置
        # 判断llm 与 lora 是否配套
        if self.llm_name in ['mixtral_8x7b', 'llama_2_70b']:
            llm_ = BaiduLLM(temperature=self.temperature, top_p=self.top_p,
                            top_k=self.top_k, penalty_score=self.penalty_score,
                            stop=self.stop, model_name=self.llm_name)
            # 是否加载lora
            llm = llm_

        elif self.llm_name in ['gpt-4', 'gpt-4-32k', 'gpt-4-1106-preview',
                               'gpt-4-0125-preview', 'gpt-4-turbo-preview', 'gpt-4-vision-preview',
                               'gpt-4-0613', "gpt-4-32k-0613", 'gpt-4-0314', 'gpt-4-32k-0314', 'gpt-3.5-turbo',
                               'gpt-3.5-turbo-16k', 'gpt-3.5-turbo-0125', 'gpt-3.5-turbo-1106', 'gpt-3.5-turbo-0613',
                               'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-0301', 'text-davinci-003', 'text-davinci-002',
                               'gpt-3.5-turbo-instruct', 'text-ada-001', 'text-babbage-001', 'text-curie-001', 'ada',
                               'babbage', 'curie', 'davinci', 'gpt-35-turbo-16k', 'gpt-35-turbo', 'gpt-35-turbo-1106',
                               'gpt-35-turbo-0613', 'gpt-35-turbo-16k-0613']:
            llm_ = OpenAI(model=self.llm_name)  # max_tokens
            llm = llm_
        elif self.llm_name is None:
            llm = None
        else:
            raise Exception('llm_name 配置错误')
            return None
        return llm

    def __repr__(self):
        return f"""
        topic: {self.topic}    # Tknode 主题 即 主要做的事(要求专注于一件事)
        llm_name  : {self.llm_name} # 该Tknode 使用的大模型名称 要求必须是注册过的大模型 str 
        lora : {self.lora}        # 该Tknode 使用的lora模组,要求必须与大模型匹配 匹配关系详见表
        temperature :{self.temperature}    # 大模型温度
        top_p :{self.top_p}               # 大模型参数
        top_k :{self.top_k}                  # 大模型参数
        penalty_score :{self.penalty_score}   # 大模型参数
        stop :{self.stop}                     # 大模型参数 部分有效
        
        flow_data_path: {self.flow_data_path}
        平均耗时: {self.平均耗时}                 # 运行该Tknode 的平均时长,即时间成本 不需被赋值
        当前耗时: {self.当前耗时}                 # 运行该Tknode 的最新一次的耗时记录
        平均成本: {self.平均成本}                 # 运行该Tknode 的平均成本 即tokens * 单价
        当前成本: {self.当前成本}                 # 运行该Tknode 的最近成本 即tokens * 单价
        平均失败率: {self.失败率}                 # Tknode 运行抛出异常的概率
        失败次数: {self.失败次数}                 # Tknode 运行抛出异常的次数
        好评率: {self.好评率}                     # Tknode 输出结果获得优质的比率
        唤起率: {self.唤起率}                    # Tknode 触发二次唤起且成功通过的概率
        使用次数: {self.使用次数}                 # Tknode 被引用的次数
        使用百分比: {self.使用百分比}              # Tknode 的引用次数 占所有引用次数的比例
        
        数据积累条数:{self.数据积累条数}            # 积累数据的条数
        人工标注条数: {self.人工标注条数}           # 人工标注条数
        AI标注条数 : {self.AI标注条数}             # AI标注条数
        待标注条数 : {self.待标注条数}              # 待标注条数    
        

        可用方法:
        self.nodename
        self.runnodes
        
        self.llm
        """


    def strategy(self, inputs: str) -> str:
        """
        策略模块 必须要重写的模块 是主要的逻辑载体
        """
        raise MustOverridOError('strategy 必须被重写 输入是str 输出是str')

    def test(self,inputs:str):
        # print(self.__class__.__name__)
        print('time analyse\n')
        self.opt.time_analyse.analyse(f'{self.__class__.__name__}().strategy("{inputs}")')
        print('memory analyse\n')
        self.opt.memory_analyse(self.strategy, '你好')# TODO

    @staticmethod
    def get_model_table():
        # return model_table
        return model_lora_dict


    def noumenon(self,inputs):
        @self.opt.test_case(type=self.test_case_type,cache_home=self.cache_home)
        def warps(inputss):
            return self.strategy(inputss)

        return warps(inputs)

    @Logger.load(logger)
    @opt.time_analyse.timecost(logger)
    def run(self, inputs: str) -> str:
        try:
            output = self.noumenon(inputs)
            return output
        except MustOverridOError as e:
            raise MustOverridOError(e)
        except Exception as e:
            self.logger.warning(f'error :{e} 记录错误+1 尝试重调用 time:{time.ctime()},任务id')
            if self.recall:
                try:
                    new_input = OpenAI().complete(f'help me rewrite this text to easyer to understand , input: {inputs}')
                    self.logger.info(f'new_input :{new_input} 开始重调用 time:{time.ctime()},任务id')
                    output = self.noumenon(new_input)
                    assert output
                    print('重调用成功')
                    return output
                except Exception as e:
                    print('记录冲调用失败 +1')
                    raise Exception(e)
            else:
                raise Exception(e)

    def train_tknode(self):
        """利用数据训练本tnode 的端到端的lora"""
        self.flow_data_path  # read
        # 进行训练
        # 保存lora 模型
        # 将lora模型注册到 模型注册表中


class RunNodes(object):
    def __init__(self):
        self.round = 0

    # @ #端到端的数据保存 会有错误记录 会有时间记录等
    def start_seq(self, prompt, tnodes: List[TNode]):
        try:
            for i in tnodes:
                assert i.nodename != i.father
        except AssertionError as e:
            raise 循环调用('构成了循环调用')
        try:
            for tnode in tnodes:
                assert isinstance(tnode, TNode)
                result = tnode.run(prompt)
                prompt = result
                self.round += 1
            return result
        except AssertionError as e:
            print(e, 'aa')
        except Exception as e:
            print(e, tnode.topic, 'bb')

    def start_if(self, prompt, tnodes: List[TNode]):
        #  解决路由问题 简化的树逻辑
        pass

    def start_and(self):
        pass

    def start_or(self):
        pass

    def start_not(self):
        pass

    def start_tree(self, prompt, tnodes: List[TNode]):
        # 树结构的运行模式 解决路由问题
        pass

    def start_map(self, prompt, tnodes: List[TNode]):
        # 图结构的运行模式
        # 解决路由+ 循环问题
        pass


class TNodesManager():
    def __init__(self,tnode:TNode):
        self.tnode = tnode

    def get_data(self,type='all'):
        self.tnode

    def analyse(self):
        print('统计异常次数')
        print('平均执行时间')
        print('平均花费成本')
        print('统计调用总次数')
        print('统计调用占比')

    def show_all(self):
        print('格式化显示当前信息')

    def clean_cache(self):
        pass

    def data_annotation(self):
        print('优质回复的标注')
        print('正反回复的补充')
        print('回复的修改等 ')
        print('人为 或者 使用高级AI 或者打分机制 为模型打分 1-5分')
        print('标注完毕之后 会对剩下的数据的反面用大模型生成 以适应各种微调')

    def output_data(self):
        print('数据导出为数据集')

    def fineturning(self):
        pass

    def train(self):
        pass

    def history_train_analyse(self):
        pass

    def history_data_picture(self):
        pass

class TNodesManagers():
    pass

    def update(self, tnodes):
        for tnode in tnodes:
            tnode.train()

    def show_all(self):
        print('格式化显示当前信息')
