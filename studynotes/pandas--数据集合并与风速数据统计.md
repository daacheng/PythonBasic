## pandas--数据集合并
### 代码

    import pandas as pd

    # pandas合并(concat,merge)

    #  创建数据集
    raw_data_1 = {
            'subject_id': ['1', '2', '3', '4', '5'],
            'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
            'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

    raw_data_2 = {
            'subject_id': ['4', '5', '6', '7', '8'],
            'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
            'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

    raw_data_3 = {
            'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
            'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

    data1 = pd.DataFrame(raw_data_1)
    data2 = pd.DataFrame(raw_data_2)
    data3 = pd.DataFrame(raw_data_3)

    # 把data1和data2按照行的轴向(行的延伸方向)合并
    all_data = pd.concat([data1,data2])

    # 把data1和data2按照列的轴向（列的延伸方向）合并
    pd.concat([data1,data2],axis=1)

    # 根据subject_id的值合并 all_data 和 data3
    pd.merge(all_data,data3,on='subject_id')

    # 只合并data1和data2中具有相同subject_id的数据
    pd.merge(data1,data2,how='inner',on='subject_id')

    # 合并data1,data2所有数据
    pd.merge(data1,data2,how='outer',on='subject_id')

## pandas--风速数据统计
[风速数据地址](https://github.com/daacheng/PythonBasic/blob/master/dataset/wind_data.csv)

https://github.com/daacheng/PythonBasic/blob/master/dataset/wind_data.csv
### 代码

    import pandas as pd
    import datetime
    # pandas 风速数据统计

    # 读取风速数据，并将前三列合并转换成日期
    wind = pd.read_csv('wind_data.csv',sep='\s+',parse_dates=[[0,1,2]])
    wind.head(5)

    # 发现 日期时间不对，出现2061-01-01
    # 创建时间修改函数， 应用在Yr_Mo_Dy列上，修改异常时间值
    def fix_date(Yr_Mo_Dy):
        year = Yr_Mo_Dy.year-100 if Yr_Mo_Dy.year>2018 else Yr_Mo_Dy.year
        return datetime.date(year, Yr_Mo_Dy.month, Yr_Mo_Dy.day)

    wind.Yr_Mo_Dy = wind.Yr_Mo_Dy.apply(fix_date)


    # 把Yr_Mo_Dy的类型转换为 datetime   dtype('<M8[ns]') 
    wind.Yr_Mo_Dy = pd.to_datetime(wind['Yr_Mo_Dy'])
    wind.Yr_Mo_Dy.dtype

    # 把时间列 Yr_Mo_Dy设置为索引
    wind = wind.set_index('Yr_Mo_Dy')
    wind


    # 查看每一列的缺失值个数
    wind.isnull().sum()

    # 查看每一列 一共有多少个完整数据   （总行数-缺失值个数）
    wind.shape[0]-wind.isnull().sum()

    # 查看每列数据的平均值
    wind.mean()

    # 查看全部数据的平均值
    wind.mean().mean()

    # 创建一个DataFrame对象，用于存储每一列的 统计值（最大值，最小值，平均值，标准差）
    wind_stats = pd.DataFrame()
    wind_stats['min'] = wind.min()
    wind_stats['max'] = wind.max()
    wind_stats['mean'] = wind.mean()
    wind_stats['std'] = wind.std()
    wind_stats


    # 创建一个DataFrame对象，用于存储每一行的 统计值（最大值，最小值，平均值，标准差）
    day_stats = pd.DataFrame()
    day_stats['min'] = wind.min(axis = 1)
    day_stats['max'] = wind.max(axis = 1)
    day_stats['mean'] = wind.mean(axis = 1)
    day_stats['std'] = wind.std(axis = 1)
    day_stats


    #  查看所有一月份的数据
    # 新增列 month， 通过query方法得到一月份的数据
    wind['date'] = wind.index
    wind['year'] = wind['date'].apply(lambda x:x.year)
    wind['month'] = wind['date'].apply(lambda x:x.month)
    wind['day'] = wind['date'].apply(lambda x:x.day)

    january_winds  = wind.query('month == 1')

    # loc是基于列名columns选择数据集，iloc是基于索引index选择数据集
    january_winds.loc[:,'RPT':'MAL'].mean()

    #  按照年采样，统计每一年的平均风速
    wind.resample('1AS').mean()

    #  按照月采样，统计每月的平均风速
    wind.resample('1M').mean().drop(['year','month','day'],axis = 1)
