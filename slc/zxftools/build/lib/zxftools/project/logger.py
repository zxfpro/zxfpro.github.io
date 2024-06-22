import inspect
import functools
from typing import Callable, Union
import sys
import os
try:
    from loguru import logger as _logger
except Exception as e:
    raise Exception(f'{e} please install loguru use "pip install loguru==0.7.2"')

# Logger 不支持异步函数
__all__ = ['Logger']
# 它应该要完全取代print才行 参数管理应该要更方便才行
class Logger():
    """
    Level: DEBUG INFO WARNING ERROR
    """
    def __new__(cls, log_path=None, print_level: str = "INFO", logfile_level: str = "DEBUG"):
        cls.log_path = log_path or os.environ.get('LoggerPath')
        logger = cls._get(print_level=print_level, logfile_level=logfile_level)
        return logger

    def help(self):
        return """
    TODO
    logger 不支持 异步

    for example:
        logger = Logger('aa.log')
        logger.info('aa')

        logger = Logger('aa.log')
        @Logger.load(logger)
        def test():
            return 1

    """

    @classmethod
    def _get(cls, print_level: str = "INFO", logfile_level: str = "DEBUG"):
        """
        创建一个日志记录器。

        参数:
        log_path (str): 日志文件的路径，默认为'./log.txt'。
        print_level (str): 控制台输出的日志级别，默认为'INFO'。
        logfile_level (str): 日志文件的日志级别，默认为'DEBUG'。

        返回:
        logger: 日志记录器对象。
        """
        _logger.remove()
        _logger.add(sys.stderr, level=print_level)
        _logger.add(cls.log_path, level=logfile_level)
        return _logger

    @staticmethod
    def load(logger: Callable = None, run_info: bool = False, raise_error: bool = True):
        """
        用于便捷使用log 的装饰器, 输入 logger 对象进行工作
        """

        def outer_packing(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                if 'logger' in kwargs.keys() and logger is not None:
                    kwargs['logger'] = logger
                if logger is not None and run_info:
                    logger.info(f"running function:{func.__name__}")

                try:
                    result = func(*args, **kwargs)
                    return result
                # except
                except Exception as e:
                    # 获取原函数的局部变量字典
                    local_vars = inspect.trace()[-1][0].f_locals
                    # 创建一个空字符串，用于存储变量的名字和值
                    var_info = ''
                    # 遍历局部变量字典，将每个变量的名字和值拼接到字符串中
                    for name, value in local_vars.items():
                        var_info += f'{name} = {value}\n\n'

                    # 使用logger对象记录错误信息和变量信息
                    if logger is not None:
                        logger.error(f'error in {func.__name__}: {e}\n\n params:\n\n\n{var_info}')
                    else:
                        print(f'error in {func.__name__}: {e}\n\n params:\n\n\n{var_info}')
                    if raise_error:
                        raise e
                finally:
                    pass

            return wrapper

        return outer_packing

if __name__ == '__main__':
    pass
