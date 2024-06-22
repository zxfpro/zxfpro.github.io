import dis
import ctypes
import time
import threading
import functools
from threading import Thread
from multiprocessing.pool import Pool
import os
import types
import inspect
import cProfile
import pstats
from zxftools.io import IO
try:
    from memory_profiler import memory_usage
    # print(memory_usage(my_function))
    from memory_profiler import profile
except ModuleNotFoundError as e:
    raise Exception('please pip install memory_profiler')
try:
    import func_timeout
except ModuleNotFoundError as e:
    raise Exception('please pip install func_timeout')

def _format_list_dict_to_string(lst, dct):
    # 将列表中的元素转换为字符串，并用逗号连接
    if lst == () and dct == {}:
        return ''
    list_str = ','.join(map(str, lst))
    # 将字典中的键值对转换为字符串，并用逗号连接
    dict_str = ','.join(f"{key}={value}" for key, value in dct.items())
    # 将列表字符串和字典字符串合并
    return f"{list_str},{dict_str}"


class MyThread(Thread):
    def __init__(self, target, args=None, kwargs=None):
        Thread.__init__(self)
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self):
        super().join()
        return self.result

    def get_result(self):
        return self.result



class TimeAnalyse():
    def __init__(self):
        pass

    @staticmethod
    def analyse(func_name: str = 'my_function()', save_path=None):
        """
        save_path = 'profile_output'


        # 稳定性 可维护性 可扩展性 资源利用率 鲁棒性
        ncalls
        调用次数

        tottime
        在指定函数中消耗的总时间（不包括调用子函数的时间）

        percall
        是 tottime 除以 ncalls 的商

        cumtime
        指定的函数及其所有子函数（从调用到退出）消耗的累积时间。这个数字对于递归函数来说是准确的。

        percall
        是 cumtime 除以原始调用（次数）的商（即：函数运行一次的平均时间）

        filename:lineno(function)
        提供相应数据的每个函数
        """
        assert isinstance(func_name,str)
        if save_path:
            cProfile.run(func_name, save_path)
            p = pstats.Stats(save_path)
            p.strip_dirs().sort_stats('cumulative').print_stats()
        else:
            cProfile.run(func_name)

    @staticmethod
    def read(path):
        p = pstats.Stats(path)
        p.strip_dirs().sort_stats('cumulative').print_stats()

    @staticmethod
    def timecost(loggger=None):
        """
        用来记录执行时间的函数装饰器
        """

        def outer_packing(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                time1 = time.time()
                result = func(*args, **kwargs)
                time2 = time.time() - time1
                if loggger:
                    loggger.info(f"{func.__name__} time :{time2}")
                else:
                    print(f"{func.__name__} time :{time2}")
                return result
            return wrapper
        return outer_packing


    @staticmethod
    def external_timeout(n: str):
        """
        用于提供timeout机制的函数
        n timeout 时间 秒
        """
        return func_timeout.func_set_timeout(n)


class Optimize(object):
    def __init__(self):
        self.time_analyse = TimeAnalyse()


    @staticmethod
    def test_case(type: str = 'func', cache_home: str = './cache', v_func=None, dataset_path='output.json'):
        """
        # 修改为支持mysql
        用于记录测试用例,用于优化函数的执行逻辑和算法的装饰器
            func   : 记录 优先使用函数用例 覆盖
            cache  : 记录 优先使用cache 中的用例 不覆盖
            close  : 关闭 不使用模块
            verify : 验证 使用测试用例 验证本函数的正确性
            output : 输出所有的测试用例
            output_dataset : 特供TNode
        """

        def outer_packing(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                import diskcache  # 可以使用diskcache
                cache_path = os.path.join(cache_home, func.__name__)
                cache = diskcache.Cache(cache_path)
                key = f"name:{func.__name__},args:{args},kwargs:{kwargs}"
                if type == 'func':
                    result = func(*args, **kwargs)
                    cache.set([args, kwargs], result, tag="data", expire=None, read=True)

                elif type == 'cache':
                    cache_result = cache.get([args, kwargs])
                    if cache_result is None:
                        result = func(*args, **kwargs)
                        cache.set([args, kwargs], result, tag="data", expire=None, read=True)
                    else:
                        result = cache_result
                elif type == 'close':
                    result = func(*args, **kwargs)
                elif type == 'verify':
                    for key in cache:
                        args, kwargs = key
                        result = func(*args, **kwargs)
                        verify_func = v_func or (lambda x, y: x == y)
                        try:
                            assert verify_func(result, cache.get(key))
                            result = 'success'
                        except AssertionError as e:
                            print('Expected result:', cache.get(key))
                            print('Actual result:', result)
                            result = 'Verify Fair'
                elif type == 'output':
                    result = {'keys': [key for key in cache], 'values': [cache.get(key) for key in cache]}

                elif type == 'output_dataset':
                    result = [(key[0][0], cache.get(key)) for key in cache]
                    IO.save_json(result, dataset_path)
                else:
                    result = 'error'
                return result

            return wrapper

        return outer_packing

    @staticmethod
    def decorator(func):
        def inner(*args, **kwargs):
            t = threading.Thread(target=func, args=args, kwargs=kwargs)
            t.start()
        return inner

    @staticmethod
    def test_case2parallel(rightfunc: object = None):
        """
        并行的测试用例
        """

        def outer_packing(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                right_result = rightfunc(*args, **kwargs)
                result = func(*args, **kwargs)

                if right_result == result:
                    print('Comparison successful: The results match.')
                else:
                    print('Comparison failed: The results do not match.')
                    print('Expected result:', right_result)
                    print('Actual result:', result)

            return wrapper

        return outer_packing

    @staticmethod
    def thread_multi(n: int):
        """
        多线程装饰器 n 开启几个线程 单纯的是多个备份运行
        """
        def outer_packing(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                thread_list = []
                thread_return = []
                for i in range(n):
                    thread = MyThread(target=func, args=args, kwargs=kwargs)
                    thread_list.append(thread)
                for thread in thread_list:
                    thread.start()
                for thread in thread_list:
                    result = thread.join()
                    thread_return.append(result)
                return thread_return
            return wrapper
        return outer_packing


    @staticmethod
    def thread_multis(funcs, args_list, kwargs_list):
        """
        """
        threads = []
        for i, args, kwargs in zip(funcs, args_list, kwargs_list):
            threads.append(Thread(target=i, args=args, kwargs=kwargs))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()


    @staticmethod
    def thread_list(f, params: types.GeneratorType or list, processes=4, chunksize: int = 1):
        """
        1 必须到 if __name__ == '__main__': 下执行
        """
        pool = Pool(processes)
        if isinstance(params, types.GeneratorType):
            results = pool.imap(f, params, chunksize=chunksize)
        else:
            results = pool.map(f, params, chunksize=chunksize)
        pool.close()
        return results

    @staticmethod
    def trans_bytecode(func:object):
        """
        这一行会把源代码编译成字节码，就是 python 认识的操作。
        """
        return dis.dis(func)

    @staticmethod
    def memory_analyse(my_function, *args, **kwargs):
        """
        测试 每一句语言所消耗的内存资源
        """

        def types():
            pass

        if my_function.__class__ == types.__class__:
            func_source = inspect.getsource(my_function)
        else:
            class_name = my_function.__qualname__.split('.')[0]
            aaa = f"""
class {class_name}():
    def __init__(self):
        super().__init__()
        """

            func_source = inspect.getsource(my_function)
            func_source = aaa + '\n' + func_source

        params = _format_list_dict_to_string(args, kwargs)
        temp_file_content = func_source + f"""
from memory_profiler import profile"""

        if my_function.__class__ == types.__class__:
            profile_info = f"""
profunc = profile(func={my_function.__name__})
profunc({params})"""
        else:
            profile_info = f"""
profunc = profile(func={'Hello().' + my_function.__name__})
profunc({params})"""

        temp_file_content = temp_file_content + profile_info

        # 写入临时文件
        with open('temp_file.py', 'w') as f:
            f.write(temp_file_content)
        # 执行内存分析
        # TODO python310 与python 的自动转换
        out, err, return_code = os.system('python -m memory_profiler temp_file.py')
        # 删除临时文件
        os.remove('temp_file.py')
        print(out)
        return out

    @staticmethod
    def cpp2py(cpp_func='', output_file='pylib.so'):
        # 将CPP转化为 可以使用python执行的包
        cpp_code = """
    #include <iostream>
    extern "C" {
    // 函数代码

    """ + cpp_func + """

    // 函数结束
    }
    """
        assert output_file.endswith('.so')
        with open('.test.cpp', 'w') as f:
            f.write(cpp_code)
        os.system(f"g++ -o {output_file} -shared -fPIC .test.cpp")

    @staticmethod
    def load_cpp(path='pylib.so'):
        """
        PyBind11
        """
        assert path.endswith('.so')
        lib = ctypes.cdll.LoadLibrary(path)
        return lib

    @staticmethod
    def py2cpp(func=''):
        # python 转CPP 代码
        if isinstance(func, str):
            func_source = func
        else:
            func_source = inspect.getsource(func)
        # TODO
        # LLM 将python 代码转换为C++ 的代码
        transed_code = ''
        return transed_code

__all__ = ['Optimize']
