import pandas as pd
import numpy as np

def get_data(data):
    data = data.dropna()
    data = data.reset_index(drop=True)
    data = data.drop(['Unnamed: 0'], axis=1)
    return data

def select_data(data):
    # 筛选数据
    data = data[(data.TERM=='Swap') & (data.TICKER=='1Y')]
    return data[['PRICING_DATE','PX_LAST']]

def sort_data(data):
    # 排序数据
    data = data.sort_values(by='PRICING_DATE')
    return data

def pull_nan(data):
    data['PX_LAST'] = data['PX_LAST'].replace('(null)', np.nan)
    return data
#去除nan值
def drop_nan(data):
    data = data.dropna(axis=0)
    return data


if __name__ == '__main__':
    Text = False
    if Text:
        origin_data = pd.read_csv('test.csv')
    else:
        origin_data = pd.read_excel('SOFR曲线历史数据.xlsx', sheet_name=0)

    data = select_data(origin_data)
    data = sort_data(data)
    data = pull_nan(data)

    data = drop_nan(data)
    data.to_csv('ending3.csv', index=False)
    print(data.isnull().any(axis=0).sum())



