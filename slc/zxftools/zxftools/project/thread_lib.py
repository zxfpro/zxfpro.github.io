import threading
from threading import Thread
from multiprocessing.pool import Pool
import types
import functools


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

class ThreadLib(object):
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

