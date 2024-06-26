import pandas as pd
import os

class Querier:
    """
    English类用于处理英语单词。
    """
    def __init__(self):
        """
        初始化English类。
        """
        self.package = self._get_package()
        self.root = pd.read_csv(os.path.join(self.package,'data/English/root.csv'))
        self.freq = pd.read_csv(os.path.join(self.package,'data/English/word_freq.csv'))
    def _get_package(self):
        file_path = os.path.abspath(__file__)
        dir_name = os.path.dirname(file_path)
        package_path = os.path.dirname(dir_name)
        # 返回文件路径和目录名称
        return package_path

    def get_root(self, starts='a'):
        """
        获取以特定字母开头的词根。

        参数:
        starts (str): 开头的字母。

        返回:
        DataFrame: 包含词根的数据框。
        """
        return self.root[self.root['cigen'].str.startswith(starts)]

    def get_freq(self, word='the'):
        """
        获取一个单词的频率。

        参数:
        word (str): 单词。

        返回:
        DataFrame: 包含单词频率的数据框。
        """
        return self.freq[self.freq['单词'] == word]

    def run(self, test_list: list, day: int, show=True):
        """
        运行一个测试列表。

        参数:
        test_list (list): 测试列表。
        day (int): 天数。
        show (bool): 是否显示结果。

        返回:
        str: 测试结果。
        """
        day_study = []
        day_reset = []
        day_plan = []
        assert day <= len(test_list)

        def review_(day: int):
            if i >= day:
                try:
                    day_reset.append(test_list[i - day])
                except:
                    pass

        for i in range(43):
            try:
                day_study.append(test_list[i])
                day_reset.append(test_list[i])
            except:
                pass
            review_(1)
            review_(3)
            review_(8)
            review_(15)
            review_(30)
            day_plan.append([day_study, day_reset])
            day_study, day_reset = [], []
        plan = day_plan[day - 1]
        return f"study:{plan[0]}- review{plan[1]}" if show else plan
