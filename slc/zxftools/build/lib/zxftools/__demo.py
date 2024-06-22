import functools

def decorator(a = None):
    """
    一个装饰器的编写demo
    """
    def outer_packing(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(a,'a')
            print(func.__name__)  # 函数名
            print(args)  # (1, 2)
            print(kwargs)  # {'c': 3}
            return result
        return wrapper
    return outer_packing
