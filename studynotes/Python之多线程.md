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
### 不加锁

    import threading
    import time

    num = 0
    class MyThread(threading.Thread):
        def __init__(self,arg):
            super(MyThread,self).__init__()      #必须显示调用父类的初始化函数
            self.arg = arg
        def run(self):
            time.sleep(2)
            global num
            num+=1
            #time.sleep(2)
            print(num)

    for i in range(10):
        t = MyThread(i)   
        t.start()

    print('main thread end!!!!!!')

![](https://github.com/daacheng/PythonBasic/blob/master/pic/nolock.png?raw=true)

### 加锁

    import threading
    import time

    num = 0

    lock = threading.Lock()
    class MyThread(threading.Thread):
        def __init__(self,arg):
            super(MyThread,self).__init__()      #必须显示调用父类的初始化函数
            self.arg = arg
        def run(self):
            lock.acquire()
            #time.sleep(1)
            global num
            num+=1
            #print(num)
            lock.release()
    for i in range(6):
        t = MyThread(i)   
        t.start()

    print('main thread end!!!!!!')

![](https://github.com/daacheng/PythonBasic/blob/master/pic/lock.png?raw=true)
## Condition类（生产者与消费者）

    import threading
    import time
    """
        Condition类：
            除了Lock带有的锁定池外，Condition还包含一个等待池。
            池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。
        acquire/release:调用关联的锁相应方法
        wait():调用这个方法使线程进入Condition的等待池，等待通知，并释放锁。（必须在获得锁的前提下才能释放锁，否则会异常）
        notify()：从等待池挑选一个线程，并通知。收到通知的线程自动调用acquire()去获取锁（进入锁定池），其他线程仍在等待池。
                  调用这个方法不会释放锁，（必须在获得锁的前提下才能调用，否则会异常）
    """
    con = threading.Condition()
    products = 0
    #生产者
    class Producer(threading.Thread):
        def run(self):
            global products
            while True:
                if con.acquire():
                    if products<10:
                        products+=1
                        print('生产者生产商品个数目前为：',products)
                        con.notify()      #唤醒等待池中的一个线程
                        con.release()     #释放锁
                    else:
                        print('生产10个了，停止生产')
                        con.wait()        #释放锁，进入等待池
                    time.sleep(2)

    #消费者
    class Customer(threading.Thread):
        def run(self):
            global products
            while True:
                if con.acquire():
                    if products>1:
                        products-=1
                        print('消费者消费一个，目前商品数量为：',products)
                        con.notify()      #唤醒等待池中的一个线程
                        con.release()     #释放锁
                    else:
                        print('商品消费完了！！')
                        con.wait()        #释放锁，进入等待池
                    time.sleep(2)

    for p in range(2):
        p = Producer()
        p.start()
    for c in range(3):
        c = Customer()
        c.start()

![]()
