
import pandas as pd
import numpy as np
import dask.dataframe as dd

# 基础知识复习
def create_dataframe(data):
    """
    创建DataFrame
    :param data: 字典形式的数据
    :return: DataFrame
    """
    return pd.DataFrame(data)

def select_and_filter(df, column, condition=None):
    """
    数据选择与过滤
    :param df: DataFrame
    :param column: 选择的列
    :param condition: 过滤条件
    :return: 过滤后的DataFrame
    """
    if condition:
        return df[df[column] > condition]
    return df[column]

def clean_and_preprocess(df, new_column, operation, dropna=True):
    """
    数据清洗与预处理
    :param df: DataFrame
    :param new_column: 新增列名
    :param operation: 新增列的操作
    :param dropna: 是否删除缺失值
    :return: 处理后的DataFrame
    """
    df[new_column] = operation(df)
    if dropna:
        df.dropna(inplace=True)
    return df

# 数据合并与连接
def merge_dataframes(df1, df2, key, how='inner'):
    """
    合并两个DataFrame
    :param df1: 第一个DataFrame
    :param df2: 第二个DataFrame
    :param key: 合并键
    :param how: 合并方式
    :return: 合并后的DataFrame
    """
    return pd.merge(df1, df2, on=key, how=how)

def join_dataframes(df1, df2, how='inner'):
    """
    使用join连接两个DataFrame
    :param df1: 第一个DataFrame
    :param df2: 第二个DataFrame
    :param how: 连接方式
    :return: 连接后的DataFrame
    """
    return df1.join(df2, how=how)

def concatenate_dataframes(dfs, axis=0):
    """
    沿指定轴连接多个DataFrame
    :param dfs: DataFrame列表
    :param axis: 连接轴
    :return: 连接后的DataFrame
    """
    return pd.concat(dfs, axis=axis)

# 数据透视表与交叉表
def create_pivot_table(df, values, index, columns, aggfunc='sum'):
    """
    创建数据透视表
    :param df: DataFrame
    :param values: 透视表值
    :param index: 行索引
    :param columns: 列索引
    :param aggfunc: 聚合函数
    :return: 数据透视表
    """
    return pd.pivot_table(df, values=values, index=index, columns=columns, aggfunc=aggfunc)

def create_crosstab(df, row, col):
    """
    创建交叉表
    :param df: DataFrame
    :param row: 行变量
    :param col: 列变量
    :return: 交叉表
    """
    return pd.crosstab(df[row], df[col])

# 重塑与透视
def reshape_dataframe(df, id_vars, value_vars):
    """
    使用melt函数重塑DataFrame
    :param df: DataFrame
    :param id_vars: 保持不变的列
    :param value_vars: 需要重塑的列
    :return: 重塑后的DataFrame
    """
    return pd.melt(df, id_vars=id_vars, value_vars=value_vars)

def pivot_dataframe(df, index, columns, values):
    """
    使用pivot方法透视DataFrame
    :param df: DataFrame
    :param index: 行索引
    :param columns: 列索引
    :param values: 透视值
    :return: 透视后的DataFrame
    """
    return df.pivot(index=index, columns=columns, values=values)

# 分组与聚合
def group_and_aggregate(df, by, aggfunc='sum'):
    """
    分组并聚合DataFrame
    :param df: DataFrame
    :param by: 分组键
    :param aggfunc: 聚合函数
    :return: 聚合后的DataFrame
    """
    return df.groupby(by).agg(aggfunc)

def multi_group_and_aggregate(df, by, agg_dict):
    """
    多层分组与多重聚合
    :param df: DataFrame
    :param by: 分组键
    :param agg_dict: 聚合字典
    :return: 聚合后的DataFrame
    """
    return df.groupby(by).agg(agg_dict)

# 时间序列数据处理
def create_time_series(start, end, freq='D'):
    """
    创建时间序列DataFrame
    :param start: 开始日期
    :param end: 结束日期
    :param freq: 频率
    :return: 时间序列DataFrame
    """
    date_rng = pd.date_range(start=start, end=end, freq=freq)
    df = pd.DataFrame(date_rng, columns=['date'])
    df['data'] = pd.Series(range(1, len(df)+1))
    df.set_index('date', inplace=True)
    return df

def resample_time_series(df, rule, aggfunc='sum'):
    """
    时间重采样
    :param df: 时间序列DataFrame
    :param rule: 重采样规则
    :param aggfunc: 聚合函数
    :return: 重采样后的DataFrame
    """
    return df.resample(rule).agg(aggfunc)

# 高级数据处理技巧
def conditional_merge(df1, df2, key, condition_column, new_column):
    """
    条件合并两个DataFrame
    :param df1: 第一个DataFrame
    :param df2: 第二个DataFrame
    :param key: 合并键
    :param condition_column: 条件列
    :param new_column: 新列名
    :return: 合并后的DataFrame
    """
    merged = pd.merge(df1, df2, on=key, how='outer')
    merged[new_column] = np.where(pd.notnull(merged[condition_column[0]]), merged[condition_column[0]], merged[condition_column[1]])
    return merged

def apply_custom_function(df, column, func):
    """
    使用自定义函数处理DataFrame
    :param df: DataFrame
    :param column: 需要处理的列
    :param func: 自定义函数
    :return: 处理后的DataFrame
    """
    df[column] = df[column].apply(func)
    return df

def custom_aggregate(df, by, func):
    """
    自定义聚合函数
    :param df: DataFrame
    :param by: 分组键
    :param func: 自定义聚合函数
    :return: 聚合后的DataFrame
    """
    return df.groupby(by).agg(func)

# 性能优化
def optimize_performance(df, npartitions=10):
    """
    使用Dask进行大数据处理
    :param df: 大数据集DataFrame
    :param npartitions: 分区数
    :return: 处理后的DataFrame
    """
    dask_df = dd.from_pandas(df, npartitions=npartitions)
    return dask_df.groupby('A').sum().compute()

# 实战案例与项目
def merge_orders_and_customers(orders, customers):
    """
    合并订单表和客户表
    :param orders: 订单表DataFrame
    :param customers: 客户表DataFrame
    :return: 合并后的DataFrame
    """
    return pd.merge(orders, customers, on='customer_id')

def analyze_customer_total(merged_data):
    """
    分析每个客户的总订单金额
    :param merged_data: 合并后的DataFrame
    :return: 每个客户的总订单金额DataFrame
    """
    return merged_data.groupby('customer_name')['amount'].sum().reset_index()

# 参考资料与社区资源
def get_official_docs():
    """
    获取Pandas官方文档链接
    :return: 官方文档链接
    """
    return "https://pandas.pydata.org/pandas-docs/stable/"

def get_books_and_tutorials():
    """
    获取推荐书籍与教程
    :return: 推荐书籍与教程列表
    """
    return [
        "《Python for Data Analysis》 by Wes McKinney",
        "Pandas官方教程"
    ]

def get_community_resources():
    """
    获取社区与论坛资源
    :return: 社区与论坛资源列表
    """
    return [
        "Stack Overflow上的Pandas标签",
        "Pandas GitHub社区"
    ]
