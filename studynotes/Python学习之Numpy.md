## 一、创建array对象

    #一、创建数组对象（通过列表的方式）
    data1=[6,7,5.4,8,0,1]
    arr1=np.array(data1)#array([6, 7, 5, 8, 0, 1])

    data2=[[6,7,8,9],[1,2,3,4],[1,2,3,5]]
    arr2=np.array(data2)#array([[6, 7, 8, 9],
                               #[1, 2, 3, 4]])
    arr2.shape#(3, 4)，元组的长度length代表数组的维度，元组中每一个元素对应每一个维度中的元素个数
    arr2.ndim #维度，当用数组下标表示的时候，需要用几个数字来表示才能唯一确定这个元素，这个数组就是几维

    #zero和ones生成指定形状的全为0或1的数组，empty可以创建一个没有任何具体值的数组
    np.zeros((2,3,2))
    np.ones((2,2,3))
    np.empty((4,2,3))

    np.arange(10)#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    #np.eye(N),np.identity(N),创建一个正方形N*N的矩阵，对角线为1，其他为0
    np.eye(3)
    np.identity(6)

## 二、array数据类型

    #二、数组的数据类型
    arr1.dtype#dtype('float64'),np.array会为新建的数组推断出一个合适的数据类型，通过arr.dtype查看数据类型,
    arr2.dtype#dtype('int32')
    arr3=arr1.astype(np.int32)
    print(arr3.dtype)#int32  通过arr.astype()改变数组的数据类型,返回一个新数组，原数组并不改变。

## 三、数组和标量之间的运算

        import numpy as np
        data=[[1,2,3],[4,5,6]]
        arr1 = np.array(data)

        #大小相等的数组之间的任何算数运算符都会将运算应用到元素级
        #arr1  #array([[1, 2, 3],
              # [4, 5, 6]])
        #arr1*arr1  #array([[ 1,  4,  9],
                   #    [16, 25, 36]])
        #arr1+arr1  array([[ 2,  4,  6],
                   #    [ 8, 10, 12]])

        #数组与标量的算术运算也会将标量值应用到各个元素
        #1/arr1  #array([[ 1.        ,  0.5       ,  0.33333333],
                 #       [ 0.25      ,  0.2       ,  0.16666667]])
        #arr1**2  #array([[ 1,  4,  9],
                  #     [16, 25, 36]], dtype=int32)
 
 ## 四、基本索引和切片
 ### 简单一维数组
 
        import numpy as np

        #切片
        arr2 =np.arange(10)  #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        arr2[2:8]   #array([2, 3, 4, 5, 6, 7])

        #赋值
        #arr2[2:8]=1
        #arr2   #array([0, 1, 1, 1, 1, 1, 1, 1, 8, 9])

        #将一个标量赋值给一个切片时，该值会自动传播到整个选区
        #和列表的区别是，数组切片时原始数组的视图，数据不会被复制，视图上任何修改都会直接反映到源数组上。
        arr3 = arr2[2:8]
        arr3[:]=0
        #arr2   #array([0, 1, 0, 0, 0, 0, 0, 0, 8, 9])

        #如果想要得到的是复制的一份副本，可以用array的copy()方法
        arr4=arr2[:].copy()
        arr4

### 索引

        import numpy as np
        data=[[1,2,3],[4,5,6],[7,8,9]]
        arr=np.array(data)  #array([[1, 2, 3],
                            #       [4, 5, 6],
                            #      [7, 8, 9]])

        #元素索引
        #arr[1][2]和arr[1,2]两种索引方式等效
        arr[1][2]  #6
        arr[1,2]   #6

        #切片索引
        arr[:2,:2]   #array([[1, 2],
                     #     [4, 5]])
        arr[:2,1]    #array([2, 5])

        #花式索引
        #为了以特定顺序选取行子集，只需传入一个用于指定顺序的列表或array即可。
        arr[[1,2,0]]   #array([[4, 5, 6],
                       #        [7, 8, 9],
                       #        [1, 2, 3]])


        arr2=np.arange(20).reshape(5,4)
        arr2  #array([[ 0,  1,  2,  3],
              #         [ 4,  5,  6,  7],
              #         [ 8,  9, 10, 11],
              #         [12, 13, 14, 15],
              #         [16, 17, 18, 19]])

        arr2[[1,2,3,4]]   #array([[ 4,  5,  6,  7],
                          #         [ 8,  9, 10, 11],
                          #         [12, 13, 14, 15],
                          #         [16, 17, 18, 19]])

        arr2[[1,2,3,4],[1,2,1,1]]  #array([ 5,  10, 13, 17]),最终选出的元素是(1,1),(2,2),(3,1),(4,1)

## 五、数组转置（transpose）

    import numpy as np

    #二维数组的转置，高维数组不是很明白
    arr = np.arange(15).reshape(5,3)  #array([[ 0,  1,  2],
                                      #         [ 3,  4,  5],
                                      #         [ 6,  7,  8],
                                      #         [ 9, 10, 11],
                                      #         [12, 13, 14]])

    arr.T                             #array([[ 0,  3,  6,  9, 12],
                                      #         [ 1,  4,  7, 10, 13],
                                      #         [ 2,  5,  8, 11, 14]])

## 六、通用函数（元素级数组函数）
通用函数是一种对array中的数据执行元素级运算的函数。应用到数组中的每一个函数
### 一元函数
abs：计算数组中绝对值，np.abs(arr)</br>
sqrt:计算各元素的平方根，np.sqrt(arr)</br>
square:计算个元素的平方</br>
exp:计算个元素的指数eⁿ</br>
等……
### 二元函数
add：将数组中对应元素相加</br>
subtract:第一个数组中的元素减去第二个数组中的元素</br>
multiply:数组相乘
divide:除法

## 七、数学和统计方法

        import numpy as np
        data=[[1,2,3],[4,5,6],[7,8,9]]
        arr = np.array(data)   #array([[1, 2, 3],
                               #        [4, 5, 6],
                               #        [7, 8, 9]])

        #sum()对数组中全部或某轴向的元素求和
        arr.sum(0)  #array([12, 15, 18])
        arr.sum(1)  #array([ 6, 15, 24])
        arr.sum()   #45

        #mean()求数组中全部元素的算数平均数或某个轴向的算数平均数
        arr.mean()   #5.0
        arr.mean(0)  #array([ 4.,  5.,  6.])
        arr.mean(1)  #array([ 2.,  5.,  8.])

        #std()为标准差   var()为方差
        arr.std()    #2.5819888974716112
        arr.var()    #6.666666666666667

        #min,max求数组中最小值，最大值。
        arr.min() #1
        arr.max() #9

        #argmin最小元素的索引，argmax最大元素的索引
        arr.argmin()  #0
        arr.argmax()  #8

        #cumsum求所有元素的累计和
        arr.cumsum()    #array([ 1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)

        #cumprod求所有元素的累计积
        arr.cumprod()   #array([     1,      2,      6,     24,    120,    720,   5040,  40320,  362880], dtype=int32)

## 八、用于布尔型数组的方法

    import numpy as np
    bools = np.array([False,False,True,False])

    #布尔值经常被转换为1（True），0（False）
    (bools>0).sum()   #1

    #any()用于测试数组中是否存在True
    bools.any()       #True

    #all()用于检查数组中是否所有都是True
    bools.all()       #False

## 九、集合运算

    import numpy as np
    arr1= np.array([1,1,1,2,3,4,4,4,5,5,5,0,3])

    #unique()计算数组中唯一元素，并返回有序结果
    np.unique(arr1)  #array([0, 1, 2, 3, 4, 5])

    #intersect1d(x,y)  计算数组中公共元素并返回有序结果
    arr2 = np.array([1,2,3,4])
    arr3 = np.array([4,3,6,7,8])
    np.intersect1d(arr2,arr3)    #array([3, 4])

    #union1d(x,y)计算数组的并集，返回有序结果
    np.union1d(arr2,arr3)        #array([1, 2, 3, 4, 6, 7, 8])

    #in1d(x,y) 得到一个x中的元素是否包含于y的布尔型数组
    np.in1d(arr2,arr3)

    #setdiff1d(x,y)  集合的差，元素在x中，不在y中
    np.setdiff1d(arr2,arr3)

    #setxor1d(x,y)  集合的对称差，不同时存在于两个数组中的元素
    np.setxor1d(arr2,arr3)

## 十、数组文件的输入输出
### 将数组以二进制格式保存

    import numpy as np
    arr = np.arange(10)

    #np.save可以将数组保存为.npy的二进制文件在磁盘上
    #np.load可以将磁盘上保存的数组读取出来
    np.save('arr_save',arr)
    np.load('arr_save.npy')   #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    #np.savez可以将多个数组保存在一个压缩文件中（.npz格式），将数组以关键字参数形式传入
    #np.load()读取时，会得到一个类似字典的对象
    np.savez('many_arr',a=arr,b=arr)
    many_arr = np.load('many_arr.npz')
    many_arr['a']   #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    many_arr['b']   #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

### 存取文本文件

        import numpy as np
        arr = np.array([[1,2,3,4],[5,6,7,8]])
        arr
        np.savetxt('arr.txt',arr)

## 十一、矩阵计算（两个矩阵的相乘）

    import numpy as np
    arr1 = np.array([[1,2,3],[2,3,4],[3,4,5]])
    arr1  #array([[1, 2, 3],
           #[2, 3, 4],
           #[3, 4, 5]])
    arr2 = np.array([[6,6],[8,8],[5,5]])
    arr2    #array([[6, 6],
            #       [8, 8],
            #       [5, 5]])

    arr1.dot(arr2)    #array([[37, 37],
                      #         [56, 56],
                      #         [75, 75]]) 

## 十二、随机数生成

    import numpy as np
    #通过normal得到一个标准正态分布的样本数组
    np.random.normal(size=(4,4))

    #rand()生成[0,1)的随机值
    np.random.rand(2,3)  #array([[ 0.96515435,  0.97895945,  0.84420243],
                         #      [ 0.80194013,  0.53194176,  0.41690594]])

    #randn产生正态分布的样本值（均值0，标准差1）   
    np.random.randn(3)

    #randint(a,b),从给出的上下限范围内随机选取整数
    np.random.randint(3,8)
