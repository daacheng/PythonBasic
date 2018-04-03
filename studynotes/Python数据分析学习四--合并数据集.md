# Python数据分析之合并数据集、及轴向旋转
1. pandas.merge可以根据一个键或多个键将不同的DataFrame的行连接起来。（参数：left,right,how,on,left_on,right_on,left_index,right_index）
2. pandas.concat可以沿着一条轴将多个对象堆叠到一起。
## 一、pandas.merge合并数据集
### 两个DataFrame具有相同的列名时

    import pandas as pd
    from pandas import Series,DataFrame
    dict1={
        'key':['a','b','c'],
        'data1':range(3)
    }
    df1 = DataFrame(dict1)
    df1                        #data	key
                            #0	0	a
                            #1	1	b
                            #2	2	c
    dict2={
        'key':['b','c','d'],
        'data2':range(1,4)
    }
    df2=DataFrame(dict2)
    df2                         #	data	key
                                #0	1	b
                                #1	2	c
                                #2	3	d
    #pandas.merge可以根据一个或多个键将不同的DataFrame中的行连接起来。
    #默认merge是inner内连接，结果中的键是交集。
    #pd.merge(df1,df2)           	data1	key	data2
                                #0	   1	b	1
                                #1	   2	c	2

    #如果参数没有指定要用哪个列进行连接，merge就会将重叠的列当做键。也可以通过on参数指定要连接的列。
    pd.merge(df1,df2,on='key')

    #outer外连接求取的是键的并集。
    pd.merge(df1,df2,how='outer')                         #	data1	key	data2
                                                         #0	0.0	a	NaN
                                                         #1	1.0	b	1.0
                                                         #2	2.0	c	2.0
                                                         #3	NaN	d	3.0
    #inner内连接取键的交集
    pd.merge(df1,df2,how='inner')                        #	data1	key	data2
                                                          #0	1	b	1
                                                          #1	2	c	2         
    #left左连接以左边的DataFrame的键为基准
    pd.merge(df1,df2,how='left')                        #data1	key	data2
                                                        #0	0	a	NaN
                                                        #1	1	b	1.0
                                                        #2	2	c	2.0
    #right右连接以右边的DataFrame的键为基准
    pd.merge(df1,df2,how='right')                       #data1	key	data2
                                                        #0	1.0	b	1
                                                        #1	2.0	c	2
                                                        #2	NaN	d	3

### 两个DataFrame具有不同的列名时，进行合并

    import pandas as pd
    from pandas import Series,DataFrame
    dict1={
        'lkey':['a','b','c'],
        'data1':range(3)
    }
    df1 = DataFrame(dict1)
    df1                        #data1	lkey
                            #0	0	a
                            #1	1	b
                            #2	2	c
    dict2={
        'rkey':['a','b','b','c','d'],
        'data2':range(5,10)
    }
    df2=DataFrame(dict2)
    df2                         #	data2	rkey
                                #    0	5	a
                                #    1	6	b
                                #    2	7	b
                                #    3	8	c
                                #    4	9	d     
    #两个DataFrame的列名不同的情况，可以通过left_on和right_on指定,默认内连接
    pd.merge(df1,df2,left_on='lkey',right_on='rkey')                     #	data1	lkey	data2	rkey
                                                                        #0	0	a	5	a
                                                                        #1	1	b	6	b
                                                                        #2	1	b	7	b
                                                                        #3	2	c	8	c
    #outer外链接
    pd.merge(df1,df2,left_on='lkey',right_on='rkey',how='outer')         #data1	lkey	data2	rkey
                                                                        #0	0.0	a	5	a
                                                                        #1	1.0	b	6	b
                                                                        #2	1.0	b	7	b
                                                                        #3	2.0	c	8	c
                                                                        #4	NaN	NaN	9	d

### 需要根据多个键进行合并，传入一个由列名组成的列表即可

    import pandas as pd
    from pandas import Series,DataFrame
    left=DataFrame({
        'key1':['one','two','one'],
        'key2':['foo','foo','bar'],
        'lval':[1,2,3]
    })
    right=DataFrame({
        'key1':['one','one','one','two'],
        'key2':['foo','foo','bar','bar'],
        'rval':[4,5,6,7]
    })
    #要根据多个键进行合并，需要传入一个由列名组成的列表,默认inner内连接
    pd.merge(left,right,on=['key1','key2'])                                       #key1	key2	lval	rval
                                                                                #0	one	foo	1	4
                                                                                #1	one	foo	1	5
                                                                                #2	one	bar	3	6

    pd.merge(left,right,on=['key1','key2'],how='outer')                           #key1	key2	lval	rval
                                                                                #0	one	foo	1.0	4.0
                                                                                #1	one	foo	1.0	5.0
                                                                                #2	two	foo	2.0	NaN
                                                                                #3	one	bar	3.0	6.0
                                                                                #4	two	bar	NaN	7.0
### 索引上的合并（left_index,right_index）

        import pandas as pd
        from pandas import Series,DataFrame
        left1=DataFrame({
            'key':['a','a','b','c','d'],
            'lvalue':[1,2,3,4,5]
        })
        left1                                        #	key	lvalue
                                                    #0	a	1
                                                    #1	a	2
                                                    #2	b	3
                                                    #3	c	4
                                                    #4	d	5
        right1=DataFrame({
            'rvalue':[6,7,8]
        },index=['a','b','c'])
        right1                                       #	rvalue
                                                    #a	6
                                                    #b	7
                                                    #c	8
        #索引上的合并，可以通过left_index=True或者right_index=True来说明索引被用作连接键。默认是内连接，取交集。
        pd.merge(left1,right1,left_on='key',right_index=True)               #key	lvalue	rvalue
                                                                            #0	a	1	6
                                                                            #1	a	2	6
                                                                            #2	b	3	7
                                                                            #3	c	4	8
        #外连接 
        pd.merge(left1,right1,left_on='key',right_index=True ,how='outer')     #   key	lvalue	rvalue
                                                                                #0	a	1	6.0
                                                                                #1	a	2	6.0
                                                                                #2	b	3	7.0
                                                                                #3	c	4	8.0
                                                                                #4	d	5	NaN

## 二、轴向连接
### numpy的concatenate函数可用于连接原始数组。

        import numpy as np
        arr=np.arange(9).reshape(3,3)
        arr                             #([[0, 1, 2],
                                         #  [3, 4, 5],
                                         #  [6, 7, 8]])
        #numpy的连接数组的函数concatenate ，axis=0或1表示，第0轴沿着行的垂直往下，第1轴沿着列的方向水平延伸。
        np.concatenate([arr,arr],axis=1)    #array([[0, 1, 2, 0, 1, 2],
                                                  # [3, 4, 5, 3, 4, 5],
                                                  # [6, 7, 8, 6, 7, 8]])
        np.concatenate([arr,arr],axis=0)    #array([[0, 1, 2],
                                            #   [3, 4, 5],
                                            #   [6, 7, 8],
                                            #   [0, 1, 2],
                                            #   [3, 4, 5],
                                            #   [6, 7, 8]])

### pandas.concat连接Series（参数axis，join）

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame

        #创建两个没有重叠索引的Series
        s1=Series([1,2],index=['a','b'])
        s2=Series([3,4,5],index=['c','d','e'])

        #pandas.concat默认是在 axis=0上工作，这样得到一个新的Series
        pd.concat([s1,s2])                        #a    1
                                                  #b    2
                                                  #c    3
                                                  #d    4
                                                  #e    5
        #当axis=1时，得到一个DataFrame，
        pd.concat([s1,s2],axis=1)                #	0	1
                                                #a	1.0	NaN
                                                #b	2.0	NaN
                                                #c	NaN	3.0
                                                #d	NaN	4.0
                                                #e	NaN	5.0
        #有重叠索引是Series
        s3=Series([6,7],index=['a','c'])
        pd.concat([s1,s3])                       #  a    1
                                                 #  b    2
                                                 #  a    6
                                                 #  c    7
        #外连接，取索引的并集
        pd.concat([s1,s3],axis=1)                #0	1
                                            #a	1.0	6.0
                                            #b	2.0	NaN
                                            #c	NaN	7.0
        #join=inner内连接，取索引的交集
        pd.concat([s1,s3],axis=1,join='inner')    #	0	1
                                                #a	1	6

## 三、轴向旋转（DataFrame的stack和unstack方法）
stack：将列旋转为行

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame
        df=DataFrame(np.arange(6).reshape(2,3),index=['one','two'],columns=['a','b','c'])
        df             #    	a	b	c
                       # one	0	1	2
                       # two	3	4	5
        #stack()将列旋转为行
        df.stack()                 # one  a    0
                                   #      b    1
                                   #      c    2
                                   # two  a    3
                                   #      b    4
                                   #      c    5
        #对于一个层次化的Series，可以用unstack（）将其重排为一个DataFrame，stack和unstack默认操作的都是最内层。
        result=df.stack()
        result.unstack()                      #    a	b	c
                                            #one	0	1	2
                                            #two	3	4	5
        #传出分层级别，对指定的分层进行操作
        result.unstack(0)                    #	one	two
                                            #a	0	3
                                            #b	1	4
                                            #c	2	5      

        s1=Series([0,1,2,3],index=['a','b','c','d'])
        s2=Series([4,5,6],index=['c','d','e'])
        pd.concat([s1,s2],keys=['one','two'])               #one  a    0
                                                            #     b    1
                                                            #     c    2
                                                            #     d    3
                                                            #two  c    4
                                                            #     d    5
                                                            #     e    6
        #引入缺失值
        pd.concat([s1,s2],keys=['one','two']).unstack()     #a	b	c	d	e
                                                       #one	0.0	1.0	2.0	3.0	NaN
                                                       #two	NaN	NaN	4.0	5.0	6.0
        #再次进行转化，stack（）会自动滤除缺失值
        pd.concat([s1,s2],keys=['one','two']).unstack().stack()       #one  a    0.0
                                                                      #     b    1.0
                                                                      #     c    2.0
                                                                      #     d    3.0
                                                                      #two  c    4.0
                                                                      #     d    5.0
                                                                      #     e    6.0

