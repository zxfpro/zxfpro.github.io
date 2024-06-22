from .base import BaseTools

class MathTools(BaseTools):
    register_default = ['multiply', 'minus', 'plus']
    def __init__(self, register=[]):
        super().__init__(register,self.register_default)

    def multiply(self ,a: int, b: int) -> int:
        """Multiple two integers and returns the result integer"""
        return a * b

    def minus(self ,a: int, b: int) -> int:
        """minus two integers and returns the result integer"""
        return a - b

    def plus(self ,a: int, b: int) -> int:
        """plus two integers and returns the result integer"""
        return a + b

