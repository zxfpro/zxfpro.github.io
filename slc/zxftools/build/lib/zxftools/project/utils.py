import sys
import signal
from typing import Callable, Union
import functools

class MonitorError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def setproctit(name="my_process"):
    import setproctitle
    # 设置进程名称为 my_process
    setproctitle.setproctitle(name)
    # 以下是你的其他代码

def pop_get(dicts,key,default=None):
    if dicts.get(key):
        key_ = dicts.pop(key)
    else:
        key_ = default
    return key_

def external_handle_quit(quit_func: Union[Callable, None] = None):
    """
    是一个可以通过ctrl C 来进行退出的装饰器
    quit_func 表示传入Callable or None
    退出 模块
    default func:
        def quit(signum, frame):
            print('退出')
            sys.exit()

    except KeyboardInterrupt as e:
    退出函数无法解决 传入变量的事情 所以无法对东西做及时的保存
    """
    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def quit(signum, frame):
                print('退出')
                sys.exit()
            _quit = quit_func or quit
            signal.signal(signal.SIGINT, _quit)
            signal.signal(signal.SIGTERM, _quit)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return outer_packing

#other
