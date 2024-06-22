from .base import BaseTools
from llama_hub.tools.code_interpreter import CodeInterpreterToolSpec

class CoderTools(BaseTools):
    register_default = ['code_interpreter', 'write_test_code', 'run_test_code', 'rewrite_test_code', 'code_writer']
    def __init__(self, register=[],llm=None):
        super().__init__(register,self.register_default)
        self.llm = llm
        self.inter = CodeInterpreterToolSpec()

    def code_interpreter(self,code_path:str)->str:
        """
        A function to execute python code, and return the stdout and stderr

        You should import any libraries that you wish to use. You have access to any libraries the user has installed.

        The code passed to this functuon is executed in isolation. It should be complete at the time it is passed to this function.

        You should interpret the output and errors returned from this function, and attempt to fix any problems.
        If you cannot fix the error, show the code to the user and ask for help

        It is not possible to return graphics or other complicated data from this function. If the user cannot see the output, save it to a file and tell the user.
        """
        with open(code_path,'r') as f:
            code = f.read()

        return self.inter.code_interpreter(code)

    def write_test_code(self,code: str) -> str:
        """
        This is a tool for writing complete test code for a given piece of code
        """
        result = self.llm.complete(f"""
Write test code for this code, which should be as complete as possible to cover all parameter combinations
code:
{code}
-----------
text_code:
""").text
        return result

    def run_test_code(self,code: str) -> str:
        """
        This tool helps you execute your test code locally
        """
        return self.inter.code_interpreter(code)

    def rewrite_test_code(self,test_code:str,demand:str)->str:
        """
        This is a tool that allows you to rewrite test code according to guidance and requirements
        """
        result = self.llm.complete(f"""
Modify the existing test code as required.
require: {demand}
test_code:
{test_code}
-----------
new_text_code:
""").text
        return result

    def code_writer(self, text: str) -> str:
        return self.llm.complete(
            f'You are a Python code expert and can write code according to requirements. Requirement: {text}').text



