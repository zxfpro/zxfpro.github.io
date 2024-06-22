from .base import BaseTools

class ControlHome(BaseTools):
    register_default = ['control_faucet', 'control_lamp']

    def __init__(self, register=[], human_supervision=True):
        super().__init__(register, self.register_default)
        self.human_supervision = human_supervision

    def control_faucet(self,target:str,action:str)->str:
        """
        你可以通过这个工具来控制水龙头,你可以通过输入 open /close 来控制水龙头的开关
        target 代表了是哪一个水龙头 目前可选有 f1 f2 f3 f4
        """
        return f"{target} {action}d"

    def control_lamp(self,target:str,action:str)->str:
        """
        你可以通过这个工具来控制灯,你可以通过输入 open /close 来控制灯的开关
        target 代表了是哪一盏灯 目前可选有 l1 l2 l3 l4
        """
        return f"{target} {action}d 任务已结束"