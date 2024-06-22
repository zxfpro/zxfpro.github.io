class BaseTools():
    def __init__(self,register=[],register_default = ['code_writer', 'question_rewriter']):
        self.register = register or register_default


# 也可以做一个few-shot 的效果让他可以自动扩充我的tools