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
### 2.1、重新索引
