# 数据的过滤与排序
[欧洲杯数据集链接](https://github.com/daacheng/PythonBasic/blob/master/dataset/euro12.csv)
https://github.com/daacheng/PythonBasic/blob/master/dataset/euro12.csv
## 代码

    import pandas as pd

    # pandas读取12年欧洲杯数据文件，对象DataFrame
    euro = pd.read_csv('euro12.csv')
    euro.head(10)

    # 查看球队个数  16
    euro.shape[0]

    # 查看数据集列
    # Index(['Team', 'Goals', 'Shots on target', 'Shots off target', 'Shooting Accuracy', '% Goals-to-shots', 'Total shots (inc. Blocked)',
    #     'Hit Woodwork', 'Penalty goals', 'Penalties not scored', 'Headed goals','Passes', 'Passes completed', 'Passing Accuracy', 'Touches',
    #     'Crosses','Dribbles', 'Corners Taken', 'Tackles', 'Clearances', 'Interceptions','Clearances off line', 'Clean Sheets', 'Blocks',
    #     'Goals conceded', 'Saves made', 'Saves-to-shots ratio', 'Fouls Won', 'Fouls Conceded', 'Offsides', 'Yellow Cards', 'Red Cards', 
    #     'Subs on', 'Subs off','Players Used'], dtype='object')
    euro.columns

    # 查看每个队的红牌，黄牌个数
    euro[['Team','Red Cards','Yellow Cards']]

    # 先按照红牌排序，再按照黄牌排序
    euro[['Team','Red Cards','Yellow Cards']].sort_values(['Red Cards','Yellow Cards'],ascending=False)

    # 计算球队黄牌的平均值   7
    round(euro['Yellow Cards'].mean())

    # 找到进球数大于6的球队
    euro[euro.Goals>6]

    # 查找字母G开头的球队
    euro[euro.Team.str.startswith('G')]

    # 查看前7列    iloc方法
    euro.iloc[:,:7]

    # 查看除了最后三列的所有列
    euro.iloc[:,:-3]

    #  查看英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(Shooting Accuracy)
    # 方式一
    euro[euro.Team.isin(['England','Italy','Russia'])][['Team','Shooting Accuracy']]
    # 方式二   loc方法
    euro.loc[euro.Team.isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]


