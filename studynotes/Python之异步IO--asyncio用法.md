# Python之异步IO--asyncio用法
最近接触爬虫代理池，需要利用异步的方式去检测代理池中n多个代理的可用性，之前也很少接触异步编程，在这里总结一下查到的关于Python异步IO库asyncio。
## 一、同步与异步
关于同步与异步，在知乎上看到的一个解释的很好的高票回答。</br>
同步和异步关注的是**消息通信的机制**

同步：指的是，在发出一个调用时候(函数调用)，在没有得到结果之前，调用者会一直等待，直到该调用返回结果为止。</br>
这个消息通信机制是**调用者主动等待调用结果**（相当于一直在等待函数return值）

异步：指的是，在发出调用之后，这个调用就直接返回了，但是没有返回结果。</br>
这个消息通信机制是，**调用者发出调用之后，不会立刻得到结果，调用者也不会一直等待这个结果。被调用者会通过状态、通知来通知调用者，或者通过回调函数处理这个调用。**

## 二、asyncio用法
### 2.1 asyncio中的几个对象
* coroutine：协程对象，使用async关键字定义的函数，是一个协程函数，协程函数的调用不会立刻执行这个函数，而是返回一个协程对象，协程对象要注册到事件循环对象中，由事件循环去调用。
* event_loop:事件循环对象，事件循环对象会开启一个无限循环，把协程对象进行封装，当满足发生条件时，调用相应的协程函数。
* task：task对象是对协程对象的进一步封装，包含各种任务状态。

![](https://github.com/daacheng/PythonBasic/blob/master/pic/asyncio1.png)

### 2.2 基本用法
#### 两种方式将协程对象封装成task
#### loop.create_task(coroutine) 

    import asyncio
    import time

    # 通过async关键字定义一个协程函数
    async def do_some_thing(x):
        print('wait  ',x)
        
    # 协程函数的调用，不会立即执行函数，而是返回一个协程对象 <class 'coroutine'>
    coroutine = do_some_thing(2) 

    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 将协程对象封装成一个task
    task = loop.create_task(coroutine)

    # <Task pending coro=<do_some_thing() running at <ipython-input-4-ea4ea419b67b>:5>>
    # 加入事件循环之前是pending状态
    print(task)  
    loop.run_until_complete(task)
    # <Task finished coro=<do_some_thing() done, defined at <ipython-input-4-ea4ea419b67b>:5> result=None>
    # 执行之后是finished状态
    print(task)

#### asyncio.ensure_future(coroutine)

    import asyncio
    import time

    async def do_some_thing(x):
        print('wait  ',x)

    coroutine = do_some_thing(2) 
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)
    print('time  ',time.time()-start)

#### 给task绑定回调函数

    import asyncio
    import time

    async def do_some_thing(x):
        print('wait  ',x)
        return x

    # 回调函数
    def callback(task):
        print('callback:',task.result())

    coroutine = do_some_thing(2) 
    task = asyncio.ensure_future(coroutine)
    # 绑定回调函数
    task.add_done_callback(callback) 

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)
#### 阻塞与await
在协程函数中可以使用await关键字对耗时的操作进行挂起，如果事件循环在调用协程函数时遇到await，事件循环对象会挂起该协程，执行别的协程。

    import asyncio
    import time
    now = lambda: time.time()

    async def do_some_work(x):
        print('Waiting: ', x)
        await asyncio.sleep(x)
        return 'Done after {}s'.format(x)

    start = now()

    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(10)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print('Task ret: ', task.result())

    print('TIME: ', now() - start)
