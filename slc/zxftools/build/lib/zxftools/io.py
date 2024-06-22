import pickle
import multiprocessing
from io import StringIO
from io import BytesIO
import json
import os
import sys

try:
    import chardet
    import dill
    import yaml
except Exception as e:
    print(e)

import diskcache

class IOdisk():
    def __init__(self,cache_path=''):
        self.cache = diskcache.Cache(cache_path)


    def save_cache(self,key, value) -> StringIO or BytesIO:
        self.cache.set(key=key,value=value)

    def load_cache(self,key) -> str or bytes:
        result = self.cache.get(key)
        return result



class IO():
    """

    """
    def help(self):
        return f"""
    负责IO交互的功能
    1  IO.cpu_count() -> int
    2  IO.platform() -> str
    3  IO.encode_json(content: dict) -> str
    4  IO.decode_json(content: str) -> dict
    5  IO.load_dill(file_path: str) -> dill
    6  IO.save_dill(v: dict, file_path: str) - > None
    7  IO.encode_str(content: str) -> bytes
    8  IO.decode_str(content: bytes) -> str
    9  IO.open_io(file_path: str) -> str
    10 IO.save_io(content: str, type='str') -> StringIO or BytesIO
    11 IO.load_io(f: StringIO or BytesIO) -> str or bytes
    12 IO.load_env(key, default=None)
    13 IO.save_env(key, value=None, keyword=True)
    14 IO.load_json(file_path:str)
    15 IO.save_json(v, file_path)
    16 IO.load_variable(file_path)
    17 IO.save_variable(v, file_path)
    18 IO.load_yaml(file_path: str, encoding: str = 'utf-8')
    19 IO.save_yaml(v: dict, file_path: str)

"""

    @staticmethod
    def cpu_count()-> int:
        """
        获取CPU的数量。

        返回:
        int: CPU的数量。
        """
        return multiprocessing.cpu_count()

    @staticmethod
    def platform()-> str:
        """
        获取操作系统的名称。

        返回:
        str: 操作系统的名称。
        """
        return sys.platform

    @staticmethod
    def encode_json(content: dict) -> str:
        """
        将字典编码为JSON字符串
        content：需要编码的字典
        返回：编码后的JSON字符串
        """
        return json.dumps(content)

    @staticmethod
    def decode_json(content: str) -> dict:
        """
        将JSON字符串解码为字典
        content：需要解码的JSON字符串
        返回：解码后的字典
        """
        return json.loads(content)

    @staticmethod
    def encode_str(content: str) -> bytes:
        """
        将字符串编码为字节
        content：需要编码的字符串
        返回：编码后的字节
        """
        return content.encode()

    @staticmethod
    def load_dill(file_path: str):
        """
        加载dill文件
        file_path：dill文件的路径
        返回：dill文件中的内容，以字典形式返回
        """
        with open(file_path, 'rb') as f:
            return dill.load(f)

    @staticmethod
    def save_dill(v: dict, file_path: str):
        """
        将字典保存为dill文件
        v：需要保存的字典
        file_path：dill文件的路径
        """
        with open(file_path, 'wb') as f:
            dill.dump(v, f)


    @staticmethod
    def decode_str(content: bytes) -> str:
        """
        将字节解码为字符串
        content：需要解码的字节
        返回：解码后的字符串
        """
        return content.decode()

    @staticmethod
    def open_io(file_path: str) -> str:
        """
        打开文件并自动检测编码
        file_path：文件的路径
        返回：文件的内容
        """
        with open(file_path, 'rb') as f:
            data = f.read()
            result = chardet.detect(data)
            encoding = result['encoding']
            if encoding:
                encoding = 'GBK' if encoding.startswith('GB') else encoding
                encoding = 'iso-8859-9' if encoding.startswith('Windows') else encoding
                return data.decode(encoding)
            else:
                return None

    @staticmethod
    def load_env(key, default=None):
        """
        加载环境变量
        key：环境变量的键
        default：默认值
        返回：环境变量的值
        """
        return os.environ.get(key, default)

    @staticmethod
    def save_env(key, value=None, keyword=True):
        """
        保存环境变量
        key：环境变量的键
        value：环境变量的值
        keyword：是否通过输入获取环境变量的值
        """
        if keyword:
            import getpass
            os.environ[key] = getpass.getpass(f'{key} input:')
        else:
            try:
                assert value
            except:
                print('value is None')
            os.environ[key] = value

    @staticmethod
    def load_json(file_path):
        """
        加载JSON文件
        file_path：JSON文件的路径
        返回：JSON文件中的内容，以字典形式返回
        """
        with open(file_path, 'r') as f:
            v = json.load(f)
        return v

    @staticmethod
    def save_json(v, file_path):
        """
            将字典保存为JSON文件
            v：需要保存的字典
            file_path：JSON文件的路径
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            assert v is not None
            file = json.dump(v, f, ensure_ascii=False)
        return file

    @staticmethod
    def load_variable(file_path):
        """
        加载pickle文件
        file_path：pickle文件的路径
        返回：pickle文件中的内容
        """
        with open(file_path, 'rb') as f:
            r = pickle.load(f)
        return r

    @staticmethod
    def save_variable(v, file_path):
        """
        将变量保存为pickle文件
        v：需要保存的变量
        file_path：pickle文件的路径
        """
        with open(file_path, 'wb') as f:
            pickle.dump(v, f)

    @staticmethod
    def load_yaml(file_path: str, encoding: str = 'utf-8'):
        """
            加载YAML文件
            file_path：YAML文件的路径
            encoding：文件编码，默认为'utf-8'
            返回：YAML文件中的内容，以字典形式返回
        """
        f = open(file_path, encoding=encoding)
        return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def save_yaml(v: dict, file_path: str):
        """
        将字典保存为YAML文件
        v：需要保存的字典
        file_path：YAML文件的路径
        """
        f = open(file_path, 'w')
        yaml.dump(v, f)

    @staticmethod
    def save_io(content: str, type='str') -> StringIO or BytesIO:
        """
        将字符串或二进制内容保存到内存文件对象中
        content：需要保存的内容
        type：'str'表示保存的是字符串，'other'表示保存的是二进制内容
        返回：保存了内容的内存文件对象
        """
        f = StringIO() if type == 'str' else BytesIO()
        f.write(content)
        return f
    @staticmethod
    def load_io(f: StringIO or BytesIO) -> str or bytes:
        """
        从内存文件对象中读取内容
        f：内存文件对象
        返回：内存文件对象中的内容
        """
        return f.getvalue()


__all__ = ['IO']
