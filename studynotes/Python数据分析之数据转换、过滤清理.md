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
