import os

import pandas as pd
import numpy as np
from pytorch_lightning import (
    LightningDataModule,
)
import torch
import torch.utils.data as torch_data
from esig import tosig
from sklearn.preprocessing import MinMaxScaler

def leadlag(X):
    lag = []
    lead = []

    for val_lag, val_lead in zip(X[:-1], X[1:]):
        lag.append(val_lag)
        lead.append(val_lag)

        lag.append(val_lag)
        lead.append(val_lead)

    lag.append(X[-1])
    lead.append(X[-1])

    return np.c_[lag, lead]

# 不带条件 单指标 数据  连续/离散
class Dataset(torch.utils.data.Dataset):
    def __init__(self, data, index_data):
        self.data = data.astype(np.float32)
        self.index_data = index_data.astype(np.float32)

    def __len__(self):
        # return self.local.shape[1]
        return len(self.index_data)

    def __getitem__(self, index):
        return self.data[index], self.index_data[index]

class SigDataModule(LightningDataModule):
    def __init__(self, path,batch_size: int, num_workers=16,level=4):

        super().__init__()
        self.path = path
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.minmax = MinMaxScaler(feature_range=(0.00001, 0.99999))
        self.level = level
    def train_dataloader(self):
        return torch_data.DataLoader(
            self.train_data, batch_size=self.batch_size, shuffle=True,
            num_workers=self.num_workers,
            pin_memory=True,
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
        data = pd.read_csv(self.path, index_col=0)["Close"]#
        data.index = data.index.astype("datetime64[ns]")
        windows = []
        windows_values = []
        for _, window in data.resample("M"):
            values = window.values  # / window.values[0]
            path = leadlag(values)
            windows.append(path)
            windows_values.append(values)

        self.windows = windows
        self.windows_values = windows_values
        self.orig_logsig = np.array([tosig.stream2logsig(path, self.level) for path in windows])

        logsig = self.minmax.fit_transform(self.orig_logsig)

        self.logsigs = logsig[1:]
        self.conditions = logsig[:-1]

        self.train_data = Dataset(self.logsigs,self.conditions)


if __name__ == '__main__':
    data = SigDataModule(batch_size=32)
    data.prepare_data()
    a = data.show_batch(dataset="train", idx=1)
    print(a)