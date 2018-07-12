# pandas时间序列和数据删除
### 时间序列
[数据集地址](https://github.com/daacheng/PythonBasic/blob/master/dataset/appl_1980_2014.csv)

https://github.com/daacheng/PythonBasic/blob/master/dataset/appl_1980_2014.csv
### 代码

    %matplotlib inline
    import pandas as pd

    # 时间序列
    # 读取苹果公司股票数据文件
    appl = pd.read_csv('appl_1980_2014.csv')
    appl.head(5)

    # 查看列名
    # Index(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], dtype='object') 
    appl.columns

    # 查看每一列的数据类型
    appl.dtypes

    # 把date列转换成时间类型
    appl.Date =  pd.to_datetime(appl.Date)

    # 把Date设置成索引
    appl = appl.set_index('Date')

    # 查看有没有重复的日期   True
    appl.index.is_unique

    # 按照升序排列索引
    appl = appl.sort_index(ascending=True)

    # 数据集中时间相隔多少天   12261
    (appl.index[-1]-appl.index[0]).days

    # 数据集中一共有多少个月  404
    appl.resample('M').mean().shape[0]

    # 可视化，画出股票价格趋势
    appl['Adj Close'].plot(title = 'apple stock price trend')

### 删除数据
[数据集地址](https://github.com/daacheng/PythonBasic/blob/master/dataset/iris.csv)

https://github.com/daacheng/PythonBasic/blob/master/dataset/iris.csv

### 代码

    import pandas as pd
    import numpy as np

    # 读取数据集文件
    iris = pd.read_csv('iris.csv')
    iris.head(5)

    # 给DataFrame添加列名
    iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
    iris

    # 查看缺失值数量
    pd.isnull(iris).sum()

    #  设置10-29行，"petal_length" 的值为nan
    iris.iloc[10:30,2:3] = np.nan
    iris

    # 把nan的值设置为1.0   inpalce = True 表示直接在源DataFrame上进行修改
    iris.petal_length.fillna(1.0, inplace = True)
    iris

    # 删除指定列
    del iris['class']
    iris

    # 设置前几行的数据为nan
    iris.iloc[:3,:]=np.nan
    iris

    # 删除有nan值的行
    iris = iris.dropna(how='any')
    iris

    # 重置索引  drop = True 把原来的索引删除掉
    iris.reset_index(drop = True)
