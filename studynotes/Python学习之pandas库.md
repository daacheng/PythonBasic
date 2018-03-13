## 一、pandas的数据结构（Series、DataFrame）
### 1.1、Series

        from pandas import Series,DataFrame
        import pandas as pd

        #创建一个Series对象,Series的表现形式索引在左，值在右。默认整数索引。
        #Series类似于一维数组对象，它由一组数据和数据标签（索引）组成。
        obj = Series([3,4,-1,2])
        obj     #0    3
                #1    4
                #2   -1
                #3    2
                #dtype: int64
        obj.values    #array([ 3,  4, -1,  2], dtype=int64)
        obj.index     #RangeIndex(start=0, stop=4, step=1)

        #指定索引
        obj2 = Series([3,4,-1,2],index=['a','b','c','d'])
        obj2       #a    3
                   # b    4
                   # c   -1
                   # d    2
                   # dtype: int64 
        obj2.index    #Index(['a', 'b', 'c', 'd'], dtype='object')

        #Seriese通过索引的方式获取一个或一组值
        obj2['b']   #4
        obj2[['a','c','d']]    #a    3
                               # c   -1
                               # d    2
                               # dtype: int64

        #Series进行计算会保留索引和值之间的链接
        obj2*2     #a    6
                   # b    8
                   # c   -2
                   # d    4
                   # dtype: int64

        obj2[obj2>2]     #a    3
                         #b    4
                         #dtype: int64

        #通过字典的形式创建Series对象
        data={'a':1,'b':2,'c':-5}
        Series(data)    #a    1
                        #b    2
                        #c   -5
                        #dtype: int64

        #Series本身有一个name属性，索引又有个name属性
        obj2.name='obj_name'
        obj2.index.name='index_name'
        obj2        #index_name
                    #  a    3
                    #   b    4
                    #   c   -1
                    #   d    2
                    #   Name: obj_name, dtype: int64
 ### 1.2、DataFrame
 
        from pandas import Series,DataFrame
        import pandas as pd
        import numpy as np
        #DataFrame是一个表格型数据结构，它包含一组有序的列，既有行索引也有列索引
        #通过字典创建DataFrame对象，字典中每个元素代表一列，key代表列名，value代表列的值。
        data={'column_a':[1,2,3],'column_b':[4,5,6],'column_c':[7,8,9]}
        DataFrame(data)    #	column_a	column_b	column_c
                           # 0	1	4	7
                           # 1	2	5	8
                           # 2	3	6	9

        #自定义生成一个DataFrame
        df1=DataFrame({'a':[1,2,3],'b':[4,5,6],'c':[7,8,9]},columns=['a','b','c'],index=['row1','row2','row3'])    #	a	b	c
                                                                                                                #row1	1	4	7
                                                                                                                #row2	2	5	8
                                                                                                                #row3	3	6	9
        #获取列数据  通过DataFrame.列名  或者   DataFrame['列名']
        #通过字典的方式或者属性的方式，可以将DataFrame的列获取为一个Series,返回的Series拥有与DataFrame相同的索引。
        df1['a']
        df1.a    #  row1    1
                 #  row2    2
                 #  row3    3
                 #  Name: a, dtype: int64 

        #通过索引获取行数据  DataFrame.loc['索引名']
        df1.loc['row2']     #a    2
                            #b    5
                            #c    8
                            #Name: row2, dtype: int64 


        #列可以通过赋值的方式进行修改
        df1['d']=np.arange(3)
        df1

        #或者
        obj = Series([6,6,6],index=['row1','row2','row3'])
        df1['d']=obj 
        df1          #	a	b	c	d
              # row1	1	4	7	6
              # row2	2	5	8	6
              # row3	3	6	9	6
        #删除列
        del df1['d']
        df1

        #嵌套字典形式生成DataFrame   {列名：{行名：value，行名：value},
                                    # 列名：{行名：value，行名:value}    }
        data = {'lie1':{'row1':1,'row2':2},
                   'lie2':{'row1':3,'row2':4}}
        df2 = DataFrame(data)   #	    lie1	lie2
                          #  row1	1	3
                          #  row2	2	4  
        df2.values   #array([[1, 3],
                     #       [2, 4]], dtype=int64)

## 二、基本功能
### 2.1、重新索引(reindex)

        from pandas import Series,DataFrame
        import pandas as pd
        import numpy as np
        #重新索引，pandas通过reindex方法，创建一个适应新索引的新对象
        obj=Series([1,2,3],index=['a','b','c'])
        obj2=obj.reindex(['c','b','a','e'])
        obj2     #c    3.0
                 #b    2.0
                 #a    1.0
                 #e    NaN
                 #dtype: float64

        #reindex中的method选项，可以指定向前或向后填充  ffill向前    bfill向后
        obj3=obj.reindex(['c','b','a','e','g'],method='ffill')
        obj3       #c    3
                   #b    2
                   #a    1
                   #e    3
                   #g    3
                   #dtype: int64

        #对于DataFrame，reindex可以修改索引，列，或者两个都修改
        df=DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['c1','c2','c3'])      
        df       
               #    c1	c2	c3
               #a	0	1	2
               #b	3	4	5
               #c	6	7	8    
        df1=df.reindex(['a','b','c','d'])
        df1        #	c1	c2	c3
                   #a	0.0	1.0	2.0
                   #b	3.0	4.0	5.0
                   #c	6.0	7.0	8.0
                   #d	NaN	NaN	NaN
        df2=df.reindex(columns=['c1','c2','c3','c4'])
        df2        #	c1	c2	c3	c4
                   # a	0	1	2	NaN
                   # b	3	4	5	NaN
                   # c	6	7	8	NaN

### 2.2、丢弃指定轴上的索引

        #丢弃指定轴上的项drop
        obj = Series([1,2,3],index=['a','b','c'])
        obj2 = obj.drop('c')  
        obj2     #a    1
                # b    2
                #dtype: int64

        #DataFrame可以删除任意轴上的索引
        df3=df.drop(['a'])
        df3     
                #   c1	c2	c3
                #b	3	4	5
                #c	6	7	8
        df4=df.drop(['c1'],axis=1)
        df4     #	c2	c3
                #a	1	2
                #b	4	5
                #c	7	8    

### 2.3索引、选取、过滤
#### Series

                import numpy as np
                import pandas as pd
                from pandas import Series,DataFrame
                obj=Series([3,2,1],index=['a','b','c'])
                obj   #a    3
                      #b    2
                      #c    1
                      #dtype: int32

                #通过索引名称获取值
                obj['b']   #2
                #通过索引获取值
                obj[0]     #3
                obj[1]     #2
                #切片
                obj[0:2]   #a    3
                           #b    2
                           #dtype: int64
                #利用标签切片运算和普通python切片不同，其末端是包含的      
                obj[['c','a']]   #c    1
                                 #a    3
                                 #dtype: int64 

                obj['a':'b']     #a    3
                                 #b    2
                                 #dtype: int64

                #赋值
                obj['a':'b']=9
                obj      #a    9
                         #b    9
                         #c    1
                         #dtype: int64

#### DataFrame

                import numpy as np
                import pandas as pd
                from pandas import Series,DataFrame
                data = DataFrame(np.arange(9).reshape(3,3),index=['r1','r2','r3'],columns=['c1','c2','c3'])
                data       #	c1	c2	c3
                           #r1	0	1	2
                           #r2	3	4	5
                           #r3	6	7	8

                #对DataFrame索引就是获取一个或多个列
                data['c2']    #r1    1
                              #r2    4
                              #r3    7
                              #Name: c2, dtype: int32

                data[['c1','c3']]        #	   c1	c3
                                         #r1	0	2
                                         #r2	3	5
                                         #r3	6	8

                #通过切片选取行
                data[0:2]      #	c1	c2	c3
                               # r1	0	1	2
                               # r2	3	4	5

                #选取指定列，指定行
                data.loc['r2',['c1','c2']]        #c1    3
                                                  #c2    4
                                                  #Name: r2, dtype: int32 

### 2.4、算术运算

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame

        #Series算术运算
        s1=Series([1,2,3],index=['a','b','c'])
        s2=Series([1,2,3],index=['a','b','d'])
        s1+s2      #a    2.0
                   #b    4.0
                   #c    NaN
                   #d    NaN
                   #dtype: float64

        #DataFrame算术运算
        df1=DataFrame(np.arange(4).reshape(2,2),index=['a','b'],columns=['c1','c2'])
        df2=DataFrame(np.arange(4).reshape(2,2),index=['a','b'],columns=['c1','c3'])
        df1+df2     #	c1	c2	c3
                    #a	0	NaN	NaN
                    #b	4	NaN	NaN

        #填充值（没有填充值会产生NAN）
        #运算 add sub div mul
        df1.add(df2,fill_value=0)     #	c1	c2	c3
                                    #a	0	1.0	1.0
                                    #b	4	3.0	3.0

        #DataFrame与Series运算
        #二位数组与某行运算（广播）
        arr=np.arange(9).reshape(3,3)
        arr   #array([[0, 1, 2],
              #     [3, 4, 5],
              #     [6, 7, 8]])
        arr[0]        #array([0, 1, 2])
        arr-arr[0]    #array([[0, 0, 0],
                      #       [3, 3, 3],
                      #       [6, 6, 6]])

        #DataFrame与Serie运算就是在行上进行广播
        df=DataFrame(arr,index=[1,2,3],columns=['a','b','c'])
        df     #	a	b	c
               # 1	0	1	2
               # 2	3	4	5
               # 3	6	7	8
        df.loc[1]  #DataFrame取指定行的值    a    0
                                            #b    1
                                            #c    2

        df-df.loc[1]       #	a	b	c
                           # 1	0	0	0
                           # 2	3	3	3
                           # 3	6	6	6

        #DataFrame在列上广播,必须使用算数运算方法
        df['a']     #1    0
                    #2    3
                    #3    6
        df.sub(df['a'],axis=0)      #	a	b	c
                                    #1	0	1	2
                                    #2	0	1	2
                                    33	0	1	2     

### 2.5、函数应用

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame

        #函数应用
        df=DataFrame(np.arange(9).reshape(3,3),columns=list('abc'))
        df         #	a	b	c
                   # 0	0	1	2
                   # 1	3	4	5
                   # 2	6	7	8
        f=lambda x:x.max()-x.min()
        #axis=0,函数f应用在每一列上
        df.apply(f,axis=0)     #a    6
                               #b    6
                               #c    6
        #axis=1，函数f应用在每一行上                    
        df.apply(f,axis=1)     #0    2
                               #1    2
                               #2    2

### 2.6、排序

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame
        obj=Series([2,1,4,3],index=list('bcda'))
        obj     #b    2
                #c    1
                #d    4
                #a    3
        #根据索引排序
        obj.sort_index()      #a    3
                              #b    2
                              #c    1
                              #d    4

        #根据值排序
        obj.sort_values()     #c    1
                              #b    2
                              #a    3
                              #d    4

        df=DataFrame([[3,2,1],[9,7,8],[4,6,5]],index=list('cba'),columns=list('cba'))

        #指定轴索引排序(行索引)
        df.sort_index(axis=0)    #	c	b	a
                                #a	4	6	5
                                #b	9	7	8
                                #c	3	2	1
        #指定轴索引排序(列索引)
        df.sort_index(axis=1)   #   a	b	c
                                #c	1	2	3
                                #b	8	7	9
                                #a	5	6	4
## 三、汇总和计算描述统计

### 3.1、常用汇总统计

        import numpy as np
        import pandas as pd
        from pandas import Series,DataFrame
        df= DataFrame(np.arange(6).reshape(3,2),index=list('abc'),columns=['c1','c2'])
        df         #	c1	c2
                   # a	0	1
                   # b	2	3
                   # c	4	5
        #DataFrame的sum方法，返回一个含有列小计的Series
        df.sum()   #c1    6
                   #c2    9
        #axis=1,按行进行小计
        df.sum(axis=1)    #a    1
                          #b    5
                          #c    9
        #统计达到最大值或最小值的索引
        df.idxmax()     #c1    c
                        #c2    c
        df.idxmin()     #c1    a
                        #c2    a
        #累计
        df.cumsum()     #	c1	c2
                        #a	0	1
                        #b	2	4
                        #c	6	9
        #汇总统计
        df.describe()       #	     c1	c2
                            #count 	3.0	3.0
                            #mean  	2.0	3.0
                            #std	2.0	2.0
                            #min	0.0	1.0
                            #25%	1.0	2.0
                            #50%	2.0	3.0
                            #75%	3.0	4.0
                            #max	4.0	5.0

### 3.2、相关系数与协方差（没懂）
### 3.3、唯一值、值计数以及成员资格

        obj=Series([1,1,1,2,2,2,2,2,3,3,3,8,4,4,5])
        #unique()方法返回Series中的唯一值，以数组的形式
        uniques=obj.unique()
        uniques    #array([1, 2, 3, 8, 4, 5], dtype=int64)

        #value_counts()计算Series中各个值出现的次数
        obj.value_counts()          #2    5
                                    #3    3
                                    #1    3
                                    #4    2
                                    #8    1
                                    #5    1
        #计算一个表示“Series中的值是否包含于传入的值”布尔型序列
        mask=obj.isin([1,2,3])      #0      True
                                    #1      True
                                    #2      True
                                    #3      True
                                    #4      True
                                    #5      True
                                    #6      True
                                    #7      True
                                    #8      True
                                    #9      True
                                    #10     True
                                    #11    False
                                    #12    False
                                    #13    False
                                    #14    False 

        obj[mask]           #0     1
                            #1     1
                            #2     1
                            #3     2
                            #4     2
                            #5     2
                            #6     2
                            #7     2
                            #8     3
                            #9     3
                            #10    3                        

### 3.4、滤除缺失数据
#### Series去除NAN

        obj=Series([1,2,np.nan,3,np.nan])
        obj.dropna()
        obj[obj.notnull()]

#### DataFrame去除NAN
        #丢弃全为NAN的行
        df.dropna(how='all')
        #丢弃全为NAN的列
        df.dropna(how='all',axis=1)
