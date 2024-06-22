import sys
import signal
from typing import Callable, Union
import re
import functools
import pkg_resources
from rich import print

def check_package(hard_dependencies, check=True):
    if check:
        missing_dependencies = []
        # 正则表达式匹配包名和版本号
        pattern = r'([a-zA-Z0-9_]+)([<>=!]+)([\d\.]+)'

        for dependency in hard_dependencies:
            match = re.match(pattern, dependency)
            if match:
                module_name, version_operator, module_version = match.groups()
                try:
                    # 获取已安装包的版本
                    installed_version = pkg_resources.get_distribution(module_name).version
                    # 比较版本号
                    if not pkg_resources.working_set.by_key[module_name].parsed_version in pkg_resources.Requirement.parse(f"{module_name}{version_operator}{module_version}"):
                        missing_dependencies.append(f"{module_name}: the package need version {version_operator}{module_version}, now version is {installed_version}")
                except pkg_resources.DistributionNotFound:
                    missing_dependencies.append(f"{module_name}: package not found")
                except pkg_resources.VersionConflict as e:
                    missing_dependencies.append(f"{module_name}: {e}")

        if missing_dependencies:
            raise ImportError(
                "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
            )
        del hard_dependencies, dependency, missing_dependencies

def check_all(mobile):
    for i in mobile.__all__:
        try:
            assert i not in __all__
            __all__.append(i)
        except:
            raise Exception(f'{i}命名重复')

class MonitorError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def setproctit(name="my_process"):
    import setproctitle
    # 设置进程名称为 my_process
    setproctitle.setproctitle(name)
    # 以下是你的其他代码


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
