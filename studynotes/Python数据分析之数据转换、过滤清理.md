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
