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
