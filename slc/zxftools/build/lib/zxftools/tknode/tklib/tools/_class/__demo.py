from .base import BaseTools
import time

class MathTools(BaseTools):
    register_default = ['multiply', 'minus', 'plus']
    def __init__(self, register=[],human_supervision=True):

        super().__init__(register,self.register_default)
        self.ssh = None
        self.channel = None
        self.human_supervision = human_supervision

    def multiply(self ,a: int, b: int) -> int:
        """Multiple two integers and returns the result integer"""
        if self.human_supervision:
            return
        return a * b


    def minus(self ,a: int, b: int) -> int:
        """minus two integers and returns the result integer"""
        return a - b

    def plus(self ,a: int, b: int) -> int:
        """plus two integers and returns the result integer"""
        return a + b


from .base import BaseTools
import time


class ControlHome(BaseTools):
    register_default = ['multiply', 'minus', 'plus']

    def __init__(self, register=[], human_supervision=True):
        super().__init__(register, self.register_default)
        self.human_supervision = human_supervision

    def control_faucet(self, target: str, action: str) -> str:
        """
        你可以通过这个工具来控制水龙头,你可以通过输入 open /close 来控制水龙头的开关
        target 代表了是哪一个水龙头 目前可选有 f1 f2 f3 f4
        """
        return f"{target} {action}d"

