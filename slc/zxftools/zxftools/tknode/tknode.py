
from .optimize import zcache,OptConfig

class MustOverridOError(Exception):
    # 错误定义
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class TKNode(object):

    # 耗时
    # 成本
    # 失败率 好评率
    # 调用次数 调用比例
    # 数据积累
    def __init__(self, llm=None):
        self.llm = llm
        self.opt = OptConfig(self.__class__.__name__)

    def strategy(self, inputs: str) -> str:
        """
        策略模块 必须要重写的模块 是主要的逻辑载体
        """
        raise MustOverridOError('strategy 必须被重写 输入是str 输出是str')

    def noumenon(self, inputs):

        @zcache(optconfig=self.opt, type='exact_match')
        def warps(text):
            return self.strategy(text)

        return warps(text=inputs)

    def run(self, inputs: str) -> str:
        try:
            output = self.noumenon(inputs)
            return output
        except MustOverridOError as e:
            raise MustOverridOError(e)
        except Exception as e:
            raise Exception(e)

    def clean(self):
        pass  # TODO

    def analyse(self):
        pass

    def query(self):
        pass


class TKNodeStruct(object):
    def __init__(self,id:int,next_ids:list[int],obj:TKNode):
        assert isinstance(id,int)
        assert isinstance(next_ids,list)
        assert isinstance(obj,TKNode)
        self.id = id
        self.next_ids = next_ids
        self.obj = obj


class TKNodeWorker(object):
    def __init__(self):
        pass

    def run_with_seq(self, inputs, nodes=list[TKNodeStruct]):
        temp_id = 1
        text = inputs
        for node in nodes:
            if node.id == temp_id:
                text = node.obj.run(text)
                temp_id = node.next_ids[0]
        return text

    def run_with_react(self, inputs, nodes=list[TKNodeStruct]):
        # TODO
        pass

    def start_with_tree(self, prompt, tnodes: List[TNode]):
        # TODO
        pass

    def start_with_map(self, prompt, tnodes: List[TNode]):
        # TODO
        # 图结构的运行模式
        # 解决路由+ 循环问题
        pass

    def start_with_route(self, prompt, tnodes: List[TNode]):
        # TODO
        pass


if __name__ == '__main__':
    class VxV(TKNode):
        def __init__(self, llm=None):
            super().__init__(llm=llm)

        def strategy(self, inputs: str) -> str:
            pass

    x1 = TKNodeStruct(1,[2,3],VxV())