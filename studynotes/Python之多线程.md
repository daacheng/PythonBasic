## 两种方法实现多线程
### 1、将要执行的方法作为参数传给Thread的构造方法

    import threading
    import time
    def action(arg):
        time.sleep(2)
        print('hello',arg)
    for i in range(10):
        t = threading.Thread(target = action,args = (i,))
        t.start()
    print('main thread end!!!')




    """
        构造方法 ：Thread(group=None, target=None, name=None, args=(), kwargs={})
        group:线程组
        target:要执行的方法
        name：线程名字
        args：传入执行方法的参数
    """
    """
        实例方法：
        isAlive():线程是否在运行，（启动后，终止前）
        get/setName():获取/设置线程名称
        start():线程准备好，等待cpu调用
        setDaemon(bool):设置是后台线程（默认为前台线程（setDaemon(False)））.在start()之前设置
         ：如果是后台线程，主线程执行过程中，后台线程也在执行，主线程执行完毕，后台线程不论成功与否，主线程和后台线程都停止。
         ：如果是前台线程，主线程执行过程中，前台线程也在执行，主线程执行完毕后，等待前台线程执行完毕，程序停止。
        join(timeout):阻塞当前上下文环境的线程，知道调用此方法的线程中止或者达到timeout。

    """

### 2、继承Thread类，并重写run()

    import threading
    import time

    class MyThread(threading.Thread):
        def __init__(self,arg):
            super(MyThread,self).__init__()      #必须显示调用父类的初始化函数
            self.arg = arg
        def run(self):
            time.sleep(2)
            print(self.getName())
            print('hello',self.arg)

    for i in range(10):
        t = MyThread(i)   
        t.start()
        name = '线程'+str(i)
        t.setName(name)

    print('main thread end!!!!!!')

## setDaemon

    import threading
    import time

    class MyThread(threading.Thread):
        def __init__(self,arg):
            super(MyThread,self).__init__()      #必须显示调用父类的初始化函数
            self.arg = arg
        def run(self):
            time.sleep(2)
            print(self.getName())
            print('hello',self.arg)

    for i in range(10):
        t = MyThread(i)
        t.setDaemon(True)        #和idea有关
        t.start()
        name = '线程'+str(i)
        t.setName(name)

    print('main thread end!!!!!!')

![](https://github.com/daacheng/PythonBasic/blob/master/pic/setDaemonTrue.png?raw=true)

## 设置join()
**设置join之后，主线程等待子线程全部执行完成后或者子线程超时后，主线程才结束.即使设置了setDeamon（True）主线程依然要等待子线程结束。**

    import threading
    import time

    class MyThread(threading.Thread):
        def __init__(self,arg):
            super(MyThread,self).__init__()      #必须显示调用父类的初始化函数
            self.arg = arg
        def run(self):
            time.sleep(2)
            print(self.getName())
            print('hello',self.arg)

    list_thread = []
    for i in range(10):
        t = MyThread(i)
        t.setDaemon(True)        #和idea有关
        t.start()
        name = '线程'+str(i)
        t.setName(name)
        list_thread.append(t)

    for t in list_thread:
        t.join()

    print('main thread end!!!!!!')

![](https://github.com/daacheng/PythonBasic/blob/master/pic/join.png?raw=true)

## 加锁与不加锁
