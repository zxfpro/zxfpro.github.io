import functools

class Hanshu():
    def __init__(sel,定义域,值域,max,min,单调性,奇偶性,图像,公式):
        self.定义域 = 定义域
        self.值域 = 值域
        self.max = max
        self.min = min
        self.单调性 = 单调性
        self.奇偶性 = 奇偶性
        self.图像 = 图像
        self.公式 = 公式

    def function(self,**kwargs):
        #不等式与等式  整式分式
        # 关系 加减法 乘除法 乘方
        func = functools.partial(self.一次函数,**kwargs)
        return func

    def equation(self,**kwargs):
        # 方程 方程是函数指定了y值以后的特殊形式 有唯一解或者降维解
        # 数形结合指的是函数 三元方程的解 可以是二元的函数 或一元的函数 所以 方程的图形其实是降维函数的图形
        # func = functools.partial(self.一次函数,**kwargs)
        # return func

        # import sympy as sp
        # x = sp.Symbol('x')
        # equation = sp.Eq(2 * x + 3, 7)
        # sol = sp.solve(equation)
        # print(sol)
        pass


class 幂函数(Hanshu):
    def __init__(self):
        定义域 = 'R'
        值域 = '无穷'
        max = '正无穷'
        min = '负无穷'
        单调性 = '单调递增'
        奇偶性 = '奇函数'
        图像 = ''
        公式 = '指数函数'
        super().__init__(定义域,值域,max,min,单调性,奇偶性,图像,公式)


class 指数函数(Hanshu):
    def __init__(self):
        定义域 = 'R'
        值域 = '无穷'
        max = '正无穷'
        min = '负无穷'
        单调性 = '单调递增'
        奇偶性 = '奇函数'
        图像 = ''
        公式 = '指数函数'
        super().__init__(定义域,值域,max,min,单调性,奇偶性,图像,公式)


class 对数函数(Hanshu):
    def __init__(self):
        定义域 = 'R'
        值域 = '无穷'
        max = '正无穷'
        min = '负无穷'
        单调性 = '单调递增'
        奇偶性 = '奇函数'
        图像 = ''
        公式 = '指数函数'
        super().__init__(定义域,值域,max,min,单调性,奇偶性,图像,公式)


class 幂函数(Hanshu):
    def __init__(self):
        定义域 = 'R'
        值域 = '无穷'
        max = '正无穷'
        min = '负无穷'
        单调性 = '单调递增'
        奇偶性 = '奇函数'
        图像 = ''
        公式 = '指数函数'
        super().__init__(定义域,值域,max,min,单调性,奇偶性,图像,公式)

class 分段函数(Hanshu):
    def __init__(self):
        定义域 = 'R'
        值域 = '无穷'
        max = '正无穷'
        min = '负无穷'
        单调性 = '单调递增'
        奇偶性 = '奇函数'
        图像 = ''
        公式 = '指数函数'
        super().__init__(定义域,值域,max,min,单调性,奇偶性,图像,公式)

