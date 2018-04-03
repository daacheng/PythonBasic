# 数据转换
## 移除重复数据（duplicated,drop_duplicates）

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame
        df=DataFrame({
            'k1':['a','a','b','b','c','c'],
            'k2':['1','1','2','2','3','4']
        })
        df                               #	k1	k2
                                        #0	a	1
                                        #1	a	1
                                        #2	b	2
                                        #3	b	2
                                        #4	c	3
                                        #5	c	4
        #drop_duplicates()去除重复行
        df.drop_duplicates()            #	k1	k2
                                        #0	a	1
                                        #2	b	2
                                        #4	c	3
                                        #5	c	4

        df['k3']=range(6)
        df                              #	k1	k2	k3
                                        #0	a	1	0
                                        #1	a	1	1
                                        #2	b	2	2
                                        #3	b	2	3
                                        #4	c	3	4
                                        #5	c	4	5
        #drop_duplicates()默认判断全部列，当全部列的数据都重复时才会去除。
        df.drop_duplicates()            #	k1	k2	k3
                                        #0	a	1	0
                                        #1	a	1	1
                                        #2	b	2	2
                                        #3	b	2	3
                                        #4	c	3	4
                                        #5	c	4	5
        #通过指定过滤的列来选择数据
        df.drop_duplicates(['k2'])      #   k1	k2	k3
                                        #0	a	1	0
                                        #2	b	2	2
                                        #4	c	3	4
                                        #5	c	4	5
## 利用函数或映射进行数据转换（map元素级）

        import pandas as pd
        from pandas import Series,DataFrame
        #利用函数或映射进行数据转换
        data=DataFrame({
            'food':['火腿肠','五香牛肉','腊肉','牛排'],
            'kg':[3,4,5,6]
        })
        data                       #food	kg
                                #0	火腿肠	3
                                #1	五香牛肉	4
                                #2	腊肉	5
                                #3	牛排	6
        #现在要添加一列表示食物来源于那种动物
        #方法：定义一个映射集合，通过map方法实现实现元素级转换
        meat_to_animal = {
            '火腿肠':'pig',
            '五香牛肉':'row',
            '腊肉':'pig',
            '牛排':'row'
        }
        data['animal']=data['food'].map(meat_to_animal)
        data                       #food	kg	animal
                                #0	火腿肠	3	pig
                                #1	五香牛肉	4	row
                                #2	腊肉	5	pig
                                #3	牛排	6	row
## 替换值（replace）

        import pandas as pd
        from pandas import Series,DataFrame
        #替换值
        data = Series([1,-99,2,-99])
        data                        #0     1
                                    #1   -99
                                    #2     2
                                    #3   -99
        #replace()方法替指定值，不影响原Series，重新生成一个新的Series
        data.replace(-99,np.nan)    #0    1.0
                                    #1    NaN
                                    #2    2.0
                                    #3    NaN
        #一次性替换多个值,可以传入一个列表。
        data.replace([-99,2],np.nan)#0    1.0
                                    #1    NaN
                                    #2    NaN
                                    #3    NaN

        #如果要实现对不同的值进行不同的转换
        #方法一：可传入一个由替换关系组成的列表即可
        data.replace([-99,2],[np.nan,0])              #0    1.0
                                                      #1    NaN
                                                      #2    0.0
                                                      #3    NaN
        #方法二：传入一个对应关系列表
        data.replace({-99:np.nan,2:0})
