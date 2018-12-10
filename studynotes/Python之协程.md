# Python之协程
## 写在前面
关于进程、线程、协程概念理解，[进程、线程、协程概念理解](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E8%BF%9B%E7%A8%8B%E3%80%81%E7%BA%BF%E7%A8%8B%E3%80%81%E5%8D%8F%E7%A8%8B%E6%A6%82%E5%BF%B5.md)

**协程是一种比线程更加轻量级的存在，最重要的是，协程不被操作系统内核管理，协程是完全由程序控制的**
Python通过yield关键字实现协程，实现程序的流程控制。
## 1、简单的协程例子
* 一、函数中带有yield关键字，调用函数，函数并不执行，而是返回一个生成器（协程对象）
* 二、调用next()方法运行协程，直到yield关键字停止，yield关键字后面没有表达式，则返回None
* 三、send方法的参数，会成为暂停的yield表达式的值，只有当协程处于“yield暂停状态”时，才能调用send方法。
* 四、通过 inspect.getgeneratorstate(my_corou) 查看协程的4种状态<br>
      4.1. GEN_CREATED ：等待开始执行<br>
      4.2. GEN_RUNNING ：解释器正在执行<br>
      4.3. GEN_SUSPENDED ：在yield表达式处暂停<br>
      4.4. GEN_CLOSED ：执行结束<br>

    
        import inspect
        def simple_coroutine():
            print('start coroutine')
            while True:
                x = yield
                print('coroutine received: ', x)

        # 一、函数中带有yield关键字，调用函数，函数并不执行，而是返回一个生成器（协程对象）
        # <generator object simple_coroutine at 0x00000218157D04C0>
        my_corou = simple_coroutine()
        print(my_corou)
        # 查看这时候的协程状态  GEN_CREATED : 等待开始执行
        print(inspect.getgeneratorstate(my_corou))

        # 二、调用next()方法运行协程，直到yield关键字停止，yield关键字后面没有表达式，则返回None
        print(next(my_corou))
        # 查看这时候的协程状态  GEN_SUSPENDED : 在yield表达式处暂停
        print(inspect.getgeneratorstate(my_corou))

        for i in range(5):
            # 三、send方法的参数，会成为暂停的yield表达式的值，只有当协程处于“yield暂停状态”时，才能调用send方法。
            my_corou.send(i)

        # 关闭协程 GEN_CLOSED
        my_corou.close()
        print(inspect.getgeneratorstate(my_corou))
       
#### 运行结果       
![](https://github.com/daacheng/PythonBasic/blob/master/pic/xiecheng.jpg)    
## 2、使用协程计算移动平均值

    """
    计算移动平均值
    """
    def averager():
        total = 0
        count = 0
        average = None
        while True:
            item = yield average
            total += item
            count += 1
            average = total/count
    # 调用协程函数，返回协程对象
    aver = averager()
    # 执行next()方法，执行到yield表达式 （这一步也叫“预激”）
    print(next(aver))   # None
    # 给yield表达式赋值
    print(aver.send(10))  # 10.0
    print(aver.send(20))  # 15.0
    print(aver.send(30))  # 20.0
