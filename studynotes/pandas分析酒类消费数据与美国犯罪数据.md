# pandas分析酒精类消费数据（数据分组）
“酒精类消费数据”数据集地址：https://github.com/daacheng/PythonBasic/blob/master/dataset/drinks.csv

## 代码

    import pandas as pd

    # pandas数据分组

    # 读取数据集"酒精类消费数据"
    drinks = pd.read_csv('drinks.csv')
    drinks.head()

    # 查看数据集的列
    # Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings','total_litres_of_pure_alcohol', 'continent'],dtype='object')
    drinks.columns

    # 查看各个大陆(continent)啤酒平均消费量
    drinks.groupby('continent').beer_servings.mean()

    # 查看每个大陆的红酒消费统计信息 (样本个数，均值，标准差，最大值，最小值)
    drinks.groupby('continent').wine_servings.describe()

    # 查看每个大陆每种酒类消费品的平均酒精消耗量  mean()
    drinks.groupby('continent').mean()

    # 查看每个大陆每种酒精类消费品的酒精消耗量中位数  median()
    drinks.groupby('continent').median()

    # 查看每个大陆对白酒和红酒消耗量的平均值，最大值和最小值
    drinks.groupby('continent')[['spirit_servings','wine_servings']].agg(['mean','max','min'])
    
# pandas分析美国犯罪数据(应用函数)
“美国犯罪数据”数据集地址：https://github.com/daacheng/PythonBasic/blob/master/dataset/US_Crime_Rates_1960_2014.csv

## 代码

    import pandas as pd

    # 应用函数：pd.to_datetime   set_index   del   resample   idxmax

    # 读取数据集"美国犯罪数据"
    crime = pd.read_csv('US_Crime_Rates_1960_2014.csv')
    crime.head()

    # 查看数据集的列
    # Index(['Unnamed: 0', 'Year', 'Population', 'Total', 'Violent', 'Property','Murder', 'Forcible_Rape', 'Robbery', 'Aggravated_assault',
    #        'Burglary', 'Larceny_Theft', 'Vehicle_Theft'],dtype='object')
    #Violent:暴力   Property：财产   Murder：谋杀  Forcible_Rape：强奸  Robbery：抢劫   Aggravated_assault：严重袭击   Burglary：窃案
    # Vehicle_Theft：车辆盗窃
    crime.columns

    # 查看year的数据类型   dtype('int64')
    crime.Year.dtype

    # 把Year类型从int转换为datatime
    crime.Year = pd.to_datetime(crime.Year,format = '%Y')
    # 再次查看类型  dtype('<M8[ns]')
    crime.Year.dtype

    # 把Year列变为数据集的索引   drop=True表示把Year字段删除掉，作为索引列。默认是False
    crime = crime.set_index('Year',drop=True)
    crime

    # 删除Total列
    del crime['Total']
    crime

    # Pandas中的resample，重新采样，是对原样本重新处理的一个方法，是一个对常规时间序列数据重新采样和频率转换的便捷的方法。
    # 参数表示采样的规则   常见时间频率 ：A year M month W week D day H hour T minute S second
    # 按照每十年为一组进行采样统计
    crime.resample('10AS').sum()

    # 查看每个字段 最大值 对应的索引   idxmax函数
    crime.idxmax(0)

