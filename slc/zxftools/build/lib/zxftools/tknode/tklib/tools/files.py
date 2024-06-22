from .base import BaseTools

class FileTools(BaseTools):
    register_default = ['delay', 'save_py', 'read_py']
    def __init__(self, llm, register=[]):

        super().__init__(register,self.register_default)
        self.llm = llm

    def delay(self,time_later: int) -> str:
        """
        the tool can be used to jump over [time_later] second
        """
        import time
        time.sleep(time_later)
        return f'{time_later} second later'

    def save_py(self,code: str, save_path: str) -> str:
        """
        This is a code review tool that saves your code to a local file so that you can use shell_tool to validate your code in a local dockerfiles.
        for example:
            save_path = temp.py
        """
        with open(save_path, 'w') as f:
            f.write(code)
        return f'saved your code in {save_path}'

    def read_py(self,path: str) -> str:
        """
        这个工具可以用来读py文件 输入文件路径 就能得到文件中的内容
        """
        try:
            with open(path, 'r') as f:
                text = f.read()
        except Exception as e:
            return f'Error {e}'
        return text