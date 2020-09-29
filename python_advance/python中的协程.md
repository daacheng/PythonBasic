## python中的协程
**协程是一种比线程更加轻量级的存在，最重要的是，协程不被操作系统内核管理，协程是完全由程序控制的。**
* 运行效率极高，协程的切换完全由程序控制，不像线程切换需要花费操作系统的开销，，线程数量越多，协程的优势就越明显。
* 协程不需要多线程的锁机制，因为只有一个线程，不存在变量冲突。
* 对于多核CPU，利用多进程+协程的方式，能充分利用CPU，获得极高的性能。

#### 1.一个简单的协程

```python
def simple_coroutine():
    print('coroutine start...')
    x = yield
    print('receive x = {}'.format(x))
    y = yield
    print('receive y = {}'.format(y))


if __name__ == '__main__':
    # 1. 调用协程函数，函数并不执行，而是返回一个生成器（协程对象）
    # <generator object simple_coroutine at 0x0000023E051A2360>
    coro = simple_coroutine()
    print(coro)
    # 2. 预激协程,激活协程，程序在下一个yield处停止，等待接收数据
    next(coro)
    # 3. 给协程发送数据
    coro.send(10)
    coro.send(20)
    # 4. 控制权流动到协程定义体的末尾，导致生成器像往常一样抛出StopIteration异常。
```
运行结果
```python
<generator object simple_coroutine at 0x000001C8604323B8>
coroutine start...
receive x = 10
receive y = 20
Traceback (most recent call last):
  File "E:/code/web_request/fluent_python/fluent_python_4.py", line 21, in <module>
    coro.send(20)
StopIteration
```

#### 2.协程的状态
通过 inspect.getgeneratorstate(my_corou) 查看协程的4种状态<br>
1. GEN_CREATED ：等待开始执行
2. GEN_RUNNING ：解释器正在执行
3. GEN_SUSPENDED ：在yield表达式处暂停
4. GEN_CLOSED ：执行结束

```python
from inspect import getgeneratorstate

def simple_coroutine():
    print('coroutine start...')
    x = yield
    print('receive x = {}'.format(x))
    y = yield
    print('receive y = {}'.format(y))

if __name__ == '__main__':
    coro = simple_coroutine()
    print(getgeneratorstate(coro))  # 被创建 GEN_CREATED
    next(coro)
    print(getgeneratorstate(coro))  # 在yield表达式处暂停 GEN_SUSPENDED
    coro.send(10)
    try:
        coro.send(20)
    except StopIteration:
        print('coroutine end...')
    print(getgeneratorstate(coro))  # 协程执行结束 GEN_CLOSED
```

#### 3.yield关键字
yield可以看做是流程控制工具，主要是产出和让步两个作用。
1. yield关键字会产生出返回值给协程的调用者
2. yield关键字会做出让步，暂停执行，把控制器让步给中心调度程序（调用者）。

主要理解yield的两个作用:
```python
b = yield a 可以看成两步:
1. return a  # 返回yield右边的表达式
2. b = yield  # 暂停协程，等待接收数据
```

```python
def simple_coroutine2(a):
    print('coroutine start...')
    b = yield a
    print('receive b = {}'.format(b))
    c = yield b
    print('receive c = {}'.format(c))


if __name__ == '__main__':
    coro = simple_coroutine2(5)
    a = next(coro)
    print('a = {}'.format(a))
    print('此时协程做出让步，暂停了，主程序继续向下执行....')
    b = coro.send(10)
    try:
        c = coro.send(20)
    except StopIteration:
        print('coroutine end...')
```
运行结果
```python
coroutine start...
a = 5
此时协程做出让步，暂停了，主程序继续向下执行....
receive b = 10
receive c = 20
coroutine end...
```
