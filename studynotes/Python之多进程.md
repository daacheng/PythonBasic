# Python之多进程
## 一、创建多进程
    import multiprocessing
    import os
    def hello(name):
        print('hello',name)
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
    for i in range(4):
        p = multiprocessing.Process(target=hello,args=('tom',))
        p.start()
        p.join()
## 二、multiprocessing.Queue
    import multiprocessing
    import os

    def in_num(name,q):
        print('hello',name)
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
        for i in range(10):
            q.put(i)

    def out_num(q):
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
        for i in range(10):
            print('out:',q.get())

    q = multiprocessing.Queue()
    l = []
    for i in range(2):
        p1 = multiprocessing.Process(target=in_num,args=('tom',q))
        p2 = multiprocessing.Process(target=out_num,args=(q,))
        l.append(p1)
        l.append(p2)

    for p in l:
        p.start()
        p.join()
## 三、multiprocessing.Value
    import multiprocessing
    import os

    def in_num(name,num):
        print('hello',name)
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
        for i in range(10):
            num.value += i
            print('in:%d' % num.value)

    def out_num(num):
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
        for i in range(10):
            num.value -= i
            print('out:%d' % num.value)

    num = multiprocessing.Value('i',0)
    l = []
    for i in range(2):
        p1 = multiprocessing.Process(target=in_num,args=('tom',num))
        p2 = multiprocessing.Process(target=out_num,args=(num,))
        l.append(p1)
        l.append(p2)

    for p in l:
        p.start()
        p.join()

## 四、multiprocessing.Lock
    import multiprocessing
    import os

    def in_num(name,num,lock):
        print('hello',name)
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
        lock.acquire()
        for i in range(5):
            num.value += i
            print('in:%d' % num.value)
        lock.release()


    def out_num(num):
        # 查看父进程id
        print('父进程：',os.getppid())
        # 查看进程id
        print('子进程：',os.getpid())
        for i in range(5):
            num.value -= i
            print('out:%d' % num.value)


    num = multiprocessing.Value('i',0)
    lock = multiprocessing.Lock()
    l = []
    for i in range(2):
        p1 = multiprocessing.Process(target=in_num,args=('tom',num,lock))
        p2 = multiprocessing.Process(target=out_num,args=(num,))
        l.append(p1)
        l.append(p2)


    for p in l:
        p.start()
        p.join()
