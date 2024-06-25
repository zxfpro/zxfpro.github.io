import sys
resource_path = 'resources'
sys.path.append(resource_path)
from pytorch_lightning_evaluation.evaluation import Evaluation_Callback,Sampler_Callback,log_return
import pandas as pd
import numpy as np


from pytorch_lightning import (
    LightningDataModule,
)
import torch
import torch.utils.data as torch_data

from sklearn.preprocessing import MinMaxScaler

def _prepare_data(window_size,stride,type):
    if type in ['shibor','libor','sofr']:
        if type == 'shibor':
            DF = pd.read_csv('../datadealer/ending.csv')
        elif type == 'libor':
            DF = pd.read_csv('ending2.csv')
        elif type == 'sofr':
            DF = pd.read_csv('ending3.csv')

        DF = DF.apply(pd.to_numeric, errors='ignore')
        data = DF['PX_LAST']

        dataset_data = log_return(data)
        end_data = pd.DataFrame()
        for i in range(int((len(dataset_data) - window_size) / stride)):
            end_data[i] = dataset_data[i * stride:i * stride + window_size].values
        data_dim1 = end_data.values.reshape(-1)
        return data_dim1,data,end_data

    elif type in ['EURUSD','USDJPY']:
        qeds = QEData()
        if type =='EURUSD':
            DF = qeds.read(library='MS_DataBase', table='EURUSD')
        elif type =='USDJPY':
            DF = qeds.read(library='MS_DataBase', table='USDJPY')
        DF = DF.apply(pd.to_numeric)
        DF = DF[1:]
        data = DF['value']
        volatility = DF['volatility'].values

        dataset_data = log_return(data)

        end_data = pd.DataFrame()
        for i in range(int((len(dataset_data) - window_size) / stride)):
            end_data[i] = dataset_data[i * stride:i * stride + window_size].values / volatility[i]

        data_dim1 = end_data.values.reshape(-1)
        return data_dim1,data,end_data

# 不带条件 单指标 数据  连续/离散
class Dataset(torch.utils.data.Dataset):
    def __init__(self, data, index_data):
        self.data = data
        self.index_data = index_data

    def __len__(self):
        # return self.local.shape[1]
        return len(self.index_data)

    def __getitem__(self, index):
        return self.data[index].values.astype(np.float32).reshape(-1), self.index_data.values[index]

class SynDataModule(LightningDataModule):
    def __init__(self, batch_size: int, window_size: int, num_workers=16,type_ = 'shibor'):

        super().__init__()
        self.batch_size = batch_size
        self.window_size = window_size
        self.num_workers = num_workers
        self.minmax = MinMaxScaler()
        self.type_ = type_

    def train_dataloader(self):
        return torch_data.DataLoader(
            self.train_data, batch_size=self.batch_size, shuffle=True,
            num_workers=self.num_workers
        )

    def show_batch(self, dataset="train", idx=1):
        """
        返回真实数据，方便查看数据结构和内容
        """
        self.prepare_data()
        try:
            if dataset == "train":
                data_iter = iter(self.train_data)
            elif dataset == "valid":
                data_iter = iter(self.valid_data)
            elif dataset == "test":
                data_iter = iter(self.test_data)
        except:
            raise NameError('请先定义')
        for i in range(idx):
            data = next(data_iter)
        return data

    def prepare_data(self):
        stride = 1
        scatter = True  # 控制输出数据是否离散化 默认为False 即连续数据
        index_scatter = True  # 控制标签是否离散

        data_dim1, data, end_data = _prepare_data(window_size=self.window_size,stride=stride,type=self.type_)

        # 离散化
        if scatter:
            data_dim2, retbins = pd.cut(data_dim1, bins=64, labels=range(0, 64), retbins=True)
            self.retbins = retbins
        else:
            # self.local = local#
            pass

        end_data2 = pd.DataFrame(np.array(data_dim2).reshape(end_data.shape[0], end_data.shape[1]))

        index_data = log_return(data, periods=22)[self.window_size:]  # 控制预测天数
        if index_scatter:
            index_data, index_retbins = pd.cut(index_data, bins=16, labels=range(0, 16), retbins=True)
            self.index_retbins = index_retbins

        self.train_data = Dataset(end_data2, index_data)  # 控制数据数据是一维还是二维默认为一维

