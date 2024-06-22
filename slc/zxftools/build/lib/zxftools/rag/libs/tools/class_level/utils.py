import subprocess
import os
class EnvBase():
    """
    work,works方法二：先用 os.chdir 切换工作目录，
    再用 os.system 执行命令，例如：os.chdir("path-to-repo")
    os.system("python setup.py install")13。
    """
    def __init__(self):
        self.cwd = None

    def work(self, order, run=False):
        if run:
            if order.startswith('cd'):
                cwd = order.split(' ')[-1]

                os.chdir(cwd)
                print(os.getcwd())

                self.cwd = os.getcwd()
                return 'success'
            out, err, return_code = self._execute_shell_command(order, cwd=self.cwd)
            if return_code == 0:
                return out or 'success'
            else:
                return f"Error {out}"
        else:
            return order

    def works(self, orders, run=False):
        if run:
            order_result = []
            for order in orders:
                result = self.work(order, run)
                order_result.append(result[-100:])

            return '\n'.join(order_result)

        else:
            return orders

    def _execute_shell_command(self, cmd, cwd=None):
        # 创建一个子进程来执行shell命令
        process = subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # 获取命令的输出和错误信息
        out, err = process.communicate()
        # 获取命令的返回码
        return_code = process.returncode
        # 返回命令的输出、错误信息和返回码
        return out.decode(), err, return_code

    def word_count(self,text: str) -> str:
        """the tool use to know the number of word"""
        return len(text)
