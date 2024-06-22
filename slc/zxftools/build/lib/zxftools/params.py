"""
"""
import pandas as pd
import functools
import os
import time
from zxftools.io import IO
try:
    from collections import namedtuple  # namedtuple 让dict 使用点语法
except Exception as e:
    raise Exception('please pip install collections')
try:
    import diskcache
except Exception as e:
    raise Exception('please pip install diskcache')

__all__ = ['Params']



class Params(object):
    """
    优先级 :传参 > yaml >环境变量
    """

    def __init__(self, project: str, args_set: set = {'A', 'B'},cache_home=''):
        """
        需要设定环境变量
        project 项目名
        args_set 参数定义
        cache_home 用来控制存储参数设定的位置
        """
        assert isinstance(args_set,set)
        self.args_set = args_set
        self.args_list = list(args_set)
        self.data = namedtuple('data_struct', self.args_list)
        self.cache = diskcache.Cache(os.path.join(cache_home, project))

        self.nowdates = ' '.join([time.ctime().rsplit(' ', 2)[0], time.ctime().split(' ')[-1]])

        self.kwargs_list = self.cache.get(self.nowdates) or []
        self.struct_list = []

    def input(self, **kwargs):
        # 单次存储
        kwargs = self._priority_control(**kwargs)

        class superdata(self.data):
            """
            sdg
            """
            score = None
            remark = None
            createtime = time.ctime()
            @classmethod
            def mark(cls, score: float, remark: str):
                cls.score = score
                cls.remark = remark

            @classmethod
            def output(cls, path='output.yaml'):
                '用来导出为默认配置参数'
                IO.save_yaml(kwargs, path)

        aa = superdata(**kwargs)
        self.struct_list.append(aa)
        return aa

    def __call__(self, **kwargs):
        return self.input(**kwargs)


    def _priority_control(self, **kwargs):
        try:
            yaml = IO.load_yaml(self.default_params_path)
        except:
            yaml = {}
        for key in self.args_list:
            value = os.environ.get(key, None)
            value = yaml.get(key, value)
            value = kwargs.get(key, value)
            kwargs[key] = value
        return kwargs

    def set_default(self,default_params_path):
        params_ = IO.load_yaml(default_params_path)
        assert set(params_.keys()) == self.args_set
        self.default_params_path = default_params_path


    def build_by_path(self,params_path):
        params_ = IO.load_yaml(params_path)
        assert set(params_.keys()) == self.args_set
        self.default_params_path = params_
        return self.input(**params_)

    def __repr__(self):
        return str(self.args_list)


    def save(self):
        for struct in self.struct_list:
            dicts = struct._asdict()
            dicts['score'] = struct.score
            dicts['remark'] = struct.remark
            dicts['time'] = struct.createtime
            self.kwargs_list.append(dicts)
        self.cache.set(self.nowdates, self.kwargs_list)
        self.clean()


    def clean(self):
        self.kwargs_list = []
        self.struct_list = []

    def get_dates(self):
        return [i for i in self.cache.iterkeys()]
    def show(self,dates=None):
        dates = dates or self.nowdates
        return pd.DataFrame(self.cache.get(dates) or [])
