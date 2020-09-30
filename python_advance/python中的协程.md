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

#### 4.示例，使用协程计算移动平均值
```python
def averager():
    total = 0
    count = 0
    averager_ = 0
    while True:
        item = yield averager_
        total += item
        count += 1
        averager_ = total / count

if __name__ == '__main__':
    ave = averager()
    next(ave)
    print(ave.send(10))
    print(ave.send(20))
    print(ave.send(30))
```

#### 5.终止协程和异常处理
#### 终止协程 generator.close()
generator.close()使生成器在暂停的yield表达式处抛出GeneratorExit异常。
如果生成器没有处理这个异常，或者抛出了 StopIteration 异常（通常是指运行到结尾），调用方也不会报错。
```python
from inspect import getgeneratorstate

def simple_coroutine():
    print('coroutine start...')
    while True:
        x = yield
        print('receive x = {}'.format(x))

if __name__ == '__main__':
    coro = simple_coroutine()
    next(coro)
    print(getgeneratorstate(coro))  # GEN_SUSPENDED
    coro.send(10)  # receive x = 10
    coro.send(20)  # receive x = 20
    coro.close()
    print(getgeneratorstate(coro))  # GEN_CLOSED
```
#### 异常处理 generator.throw()
generator.throw()使协程在暂停的yield处抛出指定的异常，如果协程内部捕捉并处理了这个异常，代码会向前执行到下一个yield处，如果协程没有捕捉处理异常，异常会向上冒泡，传到调用方。
```python
from inspect import getgeneratorstate

def simple_coroutine():
    print('coroutine start...')
    while True:
        try:
            x = yield
            print('receive x = {}'.format(x))
        except ValueError:
            print('something error...')

if __name__ == '__main__':
    coro = simple_coroutine()
    next(coro)
    print(getgeneratorstate(coro))  # GEN_SUSPENDED
    coro.send(10)  # receive x = 10
    coro.send(20)  # receive x = 20
    # 此时抛出异常给协程，协程内部捕捉处理了，协程继续运行到下一个yield处暂停
    coro.throw(ValueError)  # something error...
    print(getgeneratorstate(coro))  # GEN_SUSPENDED
    coro.send(30)  # receive x = 30
```
#### 6.yield from <iterable>表达式
yield from 的主要功能是打开双向通道，把最外层的调用方与最内层的子生成器连接起来，这样二者可以直接发送和产出值，还可以直接传入异常，而不用在位于中间的协程中添加大量处理异常的样板代码。

#### 委派生成器
包含 yield from <iterable> 表达式的生成器函数。
#### 子生成器
从 yield from 表达式中 <iterable> 部分获取的生成器。
#### 调用方
调用委派生成器的客户端代码

```python
# 子生成器: yield from <iterable> 表达式中的<iterable>。
def averager():
    total = 0
    count = 0
    averager_ = 0
    while True:
        item = yield averager_
        if item is None:
            break
        total += item
        count += 1
        averager_ = total / count
    return averager_

# 委派生成器: 包含 yield from <iterable>表达式的生成器函数
def grouper(key):
    global results
    while True:
        results[key] = yield from averager()


if __name__ == '__main__':
    data = {
        'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
        'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    }
    results = {}
    for key, values in data.items():
        # 客户端调用委派生成器后，可以直接把数据传给子生成器
        group_coro = grouper(key)
        next(group_coro)
        for value in values:
            group_coro.send(value)
        group_coro.send(None)

    print(results)

```
