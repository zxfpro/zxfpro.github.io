class BaseTools():
    def __init__(self,register=[],register_default = ['code_writer', 'question_rewriter']):
        self.register = register or register_default
