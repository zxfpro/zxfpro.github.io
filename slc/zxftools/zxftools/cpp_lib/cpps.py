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
