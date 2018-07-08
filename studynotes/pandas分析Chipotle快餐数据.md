# pandas分析Chipotle快餐数据.md
### [chipo数据集](https://github.com/daacheng/PythonBasic/blob/master/dataset/chipotle.csv)

### 练习代码

    import pandas as pd
    import numpy as np

    # pandas读取csv文件，读取后的对象类型是DataFrame
    chipo = pd.read_csv('chipotle.csv', sep=',')
    type(chipo)    #pandas.core.frame.DataFrame

    # 查看数据集前10条记录
    chipo.head(10)

    # 查看数据集的行数，列数
    chipo.shape       # (4622, 6)
    chipo.shape[0]    # 4622行
    chipo.shape[1]    # 6列

    # 查看数据集的详细信息，字段类型，行数，列数，数据内存大小
    chipo.info()

    # 查看数据集的列名    
    # Index(['Unnamed: 0', 'order_id', 'quantity', 'item_name', 'choice_description','item_price'], dtype='object')
    chipo.columns

    # 查看数据集的行索引
    # RangeIndex(start=0, stop=4622, step=1)
    chipo.index

    # 查看每个商品的总销量
    # 按照商品名称分组，求和，按照销量排序
    chipo.groupby('item_name').sum().sort_values(['quantity'], ascending = False)

    # 查看所有商品总销售量
    chipo.quantity.sum()

    # 改变“商品价格”列的类型
    # 查看“商品价格”列的列类型    dtype('O') object
    chipo.item_price.dtype
    # 创建一个转换函数
    transfloat = lambda x : float(x[1:-1])
    # 把转换函数应用在“商品价格”列
    chipo.item_price = chipo.item_price.apply(transfloat)
    # 再次查看类型  dtype('float64')
    chipo.item_price.dtype

    # 查看总的销售额    每个订单的商品价格*商品数量，然后再求和
    (chipo.quantity*chipo.item_price).sum()

    # 查看一共有多少个订单
    # value_counts： 统计Series或者DataFrame中每个值出现的次数 
    chipo.order_id.value_counts().count()  # 1834个订单
    # 或者
    chipo.order_id.value_counts().shape[0]

    # 计算每个订单的平均价格
    # 方法一：总销售额/总订单数   21.394231188658701
    (chipo.quantity*chipo.item_price).sum()/(chipo.order_id.value_counts().count()) 
    # 或者
    chipo['total_amount'] = chipo.quantity*chipo.item_price
    chipo.groupby('order_id').sum().mean()['total_amount']
    # 或者 
    chipo['total_amount'] = chipo.quantity*chipo.item_price
    chipo.groupby('order_id').sum().total_amount.mean()

    # 一共有多少种商品  50
    chipo.item_name.value_counts().count()
