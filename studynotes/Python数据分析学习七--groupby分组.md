## 一、分组键为Series

        import pandas as pd
        import numpy as np
        from pandas import Series,DataFrame
        data = {
            'k1':['a','a','b','b','b'],
            'k2':['one','two','one','two','one'],
            'data1':range(5),
            'data2':np.random.randn(5)
        }
        df = DataFrame(data)                               #data1	data2	k1	k2
                                                        #0	0	-1.751940	a	one
                                                        #1	1	0.355081	a	two
                                                        #2	2	-1.105436	b	one
                                                        #3	3	0.839877	b	two
                                                        #4	4	-0.761272	b	one
        #一、分组键为Series
        #根据k1键进行分组
        grouped = df['data1'].groupby(df['k1'])            #<pandas.core.groupby.SeriesGroupBy object at 0x000001FA54483F98>
        #求每组的平均值
        grouped.mean()                                    #k1
                                                          #a    0.5
                                                          #b    3.0
        #根据k1,k2键进行分组
        #得到一个层次化的索引
        df['data1'].groupby([df['k1'],df['k2']]).mean()                    #k1  k2 
                                                                           #a   one    0
                                                                           #    two    1
                                                                           #b   one    3
                                                                           #    two    3

        df['data1'].groupby([df['k1'],df['k2']]).mean().unstack()          #k2	one	two
                                                                           #k1		
                                                                           #a	0	1
                                                                           #b	3	3

## 二、分组键为长度适当的任意数组

        #二、分组键为长度适当的任意数组
        #根据一个自定义数组进行分组（分组键可以是长度适当的任意数组）
        years=np.array([2005,2006,2006,2006,2005])
        df['data1'].groupby(years).mean()                 #2005    2
                                                          #2006    2

## 三、分组键为列名

        #三、分组键为列名
        df.groupby(['k1']).mean()                       #data1	data2
                                                    #k1		
                                                    #a	0.5	0.364062
                                                    #b	3.0	0.124075

## 四、size方法查看分组大小

        #四、groupby的size方法，返回一个有分组大小的Series
        df.groupby(['k1']).size()                   #k1
                                                    #a    2
                                                    #b    3

## 五、分组对象可以进行迭代

        #五、对分组进行迭代(分组产生一个二元元组，由分组名和数据块组成)
        #一个分组键的情况
        #for name,group in df.groupby('k1'):
            #print(name)
            #print(group)                       #a
                                               #   data1     data2 k1   k2
                                               #0      0  0.104821  a  one
                                               #1      1  0.177355  a  two
                                               #b
                                               #   data1     data2 k1   k2
                                               #2      2 -0.676046  b  one
                                               #3      3  0.806155  b  two
                                               #4      4 -0.506097  b  one
        #多个分组键的情况,元组的第一个元素是由分组键组成的元组
        #for (k1,k2),group in df.groupby(['k1','k2']):
            #print(k1,k2)
            #print(group)                       #a one
                                               #   data1     data2 k1   k2
                                               #0      0 -0.879509  a  one
                                               #a two
                                               #   data1     data2 k1   k2
                                               #1      1 -0.309208  a  two
                                               #b one
                                               #   data1     data2 k1   k2
                                               #2      2  0.006868  b  one
                                               #4      4 -0.736024  b  one
                                               #b two
                                               #   data1     data2 k1   k2
                                               #3      3 -0.612376  b  two
        #可以看出分组对象是一个二元元组，由分组键和数据块组成
        list(df.groupby('k1'))                 #[('a',    data1     data2 k1   k2
                                               #   0      0  0.296102  a  one
                                               #   1      1  0.761831  a  two), ('b',    data1     data2 k1   k2
                                               #   2      2  0.763685  b  one
                                               #   3      3 -0.105020  b  two
                                               #   4      4 -0.483341  b  one)]
        #转换成字典
        pieces = dict(list(df.groupby('k1')))  
        pieces['a']                            #	data1	data2	k1	k2
                                               # 0	0	-0.142410	a	one
                                               # 1	1	1.059362	a	two

        pieces['b']                            #	data1	data2	k1	k2
                                               # 2	2	0.865926	b	one
                                               # 3	3	1.479096	b	two
                                               # 4	4	0.668402	b	one

## 六、分组对象也可以索引，通过索引选取指定列

        #六、通过对groupby对象进行索引,能达到选取指定列  df.groupby('k1')['data1']等同 df['data1'].groupby('k1')
        df.groupby('k1')['data1']

## 七、通过字典进行分组

        #七、通过字典进行分组
        data = DataFrame(np.arange(20).reshape(4,5),columns=['a','b','c','d','e'])
        data                                   #a	b	c	d	e
                                            #0	0	1	2	3	4
                                            #1	5	6	7	8	9
                                            #2	10	11	12	13	14
                                            #3	15	16	17	18	19
        mapping={'a':'一组','b':'一组','c':'一组','d':'二组','e':'二组'}
        data.groupby(mapping,axis=1).sum()          # 一组	二组
                                                    #0	3	7
                                                    #1	18	17
                                                    #2	33	27
                                                    #3	48	37

## 八、通过函数进行分组

        #八、通过函数进行分组
        data = DataFrame(np.arange(20).reshape(4,5),columns=['a','b','c','d','e'],index=['bob','tom','lily','joee'])
        data                               #	a	b	c	d	e
                                        #bob	0	1	2	3	4
                                        #tom	5	6	7	8	9
                                        #lily	10	11	12	13	14
                                        #joee	15	16	17	18	19

        data.groupby(len).sum()           #a	b	c	d	e
                                        #3	5	7	9	11	13
                                        #4	25	27	29	31	33
