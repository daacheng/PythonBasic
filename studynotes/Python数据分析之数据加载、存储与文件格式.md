# Python数据分析之数据加载、存储与文件格式
## 一、读写文本格式的数据
### 1.1读取文本格式数据

        import pandas as pd

        #read_csv()常用参数path，sep，header，names，index_col,skiprows,na_values,nrows，chunksize

        #使用pandas的read_csv()读取csv文件,默认分隔符为“,”
        df=pd.read_csv('testfile.csv')
        df           #	a	b	c	d	message
                    #0	1	2	3	4	hello
                    #1	5	6	7	8	world
                    #2	9	10	11	12	foo
        #使用pandas的read_table读取，需要指定分隔符
        df1=pd.read_table('testfile.csv',sep=',')

        #没有标题行的csv文件，一可以通过header=None指定，默认header=0第一行为标题行。
        pd.read_csv('testfile.csv',header=None)         #	0	1	2	3	4
                                                   # 0	a	b	c	d	message
                                                   # 1	1	2	3	4	hello
                                                   # 2	5	6	7	8	world
                                                   # 3	9	10	11	12	foo
        #二可以通过names自定义标题行
        pd.read_csv('testfile.csv',names=['h1','h2','h3','h4','h5'])               #h1	h2	h3	h4	h5
                                                                                #0	a	b	c	d	message
                                                                                #1	1	2	3	4	hello
                                                                                #2	5	6	7	8	world
                                                                                #3	9	10	11	12	foo

        #指定行索引(指定csv中的某一列为DataFrame的行索引)
        pd.read_csv('testfile.csv',index_col='message')          #	a	b	c	d
                                                            #message				
                                                            #hello	1	2	3	4
                                                            #world	5	6	7	8
                                                            #foo	9	10	11	12
        #skiprows=[],读取文件时，跳过指定行
        pd.read_csv('testfile.csv',skiprows=[1])            #	a	b	c	d	message
                                                            #0	5	6	7	8	world
                                                            #1	9	10	11	12	foo

        #na_values指定值为NAN
        dict={'a':[1],'b':[2,6,10]}
        pd.read_csv('testfile.csv',na_values=dict)          #a	b	c	d	message
                                                            #0	NaN	NaN	3	4	hello
                                                            #1	5.0	NaN	7	8	world
                                                            #2	9.0	NaN	11	12	foo         

        #nrows参数，指定读取几行
        pd.read_csv('testfile.csv',nrows=2)                 #a	b	c	d	message
                                                            #0	1	2	3	4	hello
                                                            #1	5	6	7	8	world
        #逐块读取文本文件，chunksize指定多少行分为一个块，
        chunker=pd.read_csv('testfile.csv',chunksize=1)
        for piece in chunker:
            print(piece)#打印每一行数据

### 1.2、将数据写出到文本格式

        import pandas as pd
        import numpy as np
        from pandas import Series,DataFrame

        #DataFrame保存至csv文件，默认会自动写入表头header和索引index，设置为False可以只写数据正文
        df=DataFrame(np.arange(9).reshape(3,3))
        df.to_csv('dffile.csv',index=False,header=False)
        pd.read_csv('dffile.csv',header=None)

        #column参数指定列写入文本文件
        df.to_csv('dffile.csv',index=False,columns=[0,1])

### 1.3、python内置csv模块读写

        import pandas as pd
        import numpy as np
        import csv
        from pandas import Series,DataFrame
        df=DataFrame(np.arange(9).reshape(3,3))
        df.to_csv('dffile.csv',index=False,header=False)
        #使用python内置的csv模块读取文件
        f=open('dffile.csv')
        reader=csv.reader(f)
        for line in reader:
            print(line)

        #写入csv文件
        with open('dffile2.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow((1,2,3))
            writer.writerow((3,4,5))
