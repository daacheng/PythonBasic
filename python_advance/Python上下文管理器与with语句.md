# 上下文管理器与with语句
## 1.上下文管理器
* 上下文管理器的任务是：代码块执行前的准备工作，代码块执行后的收尾操作，比如文件关闭，数据库连接关闭操作
* 上下文管理器类实现了__enter__和__exit__两个方法
* 上下文管理器与with语句结合
* with语句开始运行时，会在上下文管理器上调用__enter__方法，with语句运行结束后，会在上下文管理器上调用__exit__方法

## 2.with语句
**with语句的目的是为了简化try...finally模式。**

读取文件内容的操作，需要先打开文件，然后读取文件内容，最后关闭文件，为了保证文件一定关闭，需要用try...finally..语句。
```python
try:
    f = open('zhibi.py', 'r', encoding='utf-8')
    f.read(10)
    print(f)
except Exception as e:
    print('文件读取异常:{}'.format(e))
finally:
    f.close()
```

可以将打开文件操作(open)，和关闭文件操作(close)，交给上下文管理器去处理
* with语句执行的时候，上下文管理器打开文件，并将返回值与as绑定
* with语句执行结束后，上下文管理器执行关闭文件的操作

```python
with open('zhibi.py', 'r', encoding='utf-8') as f:
    f.read(10)
    print(f)
```

## 3.上下文管理器类实现
```python
class MyOpen:
    def __init__(self, filename):
        self.f = open(filename, 'r', encoding='utf-8')

    def __enter__(self):
        print('2.执行上下文管理器的__enter__')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('4.执行上下文管理器的__exit__')
        self.f.close()

if __name__ == '__main__':
    print('1.start...')
    with MyOpen('zhibi.py') as f:
        f.read(10)
        print('3.执行代码块内容')
    print('5.over!!!')
```
```python
1.start...
2.执行上下文管理器的__enter__
3.执行代码块内容
4.执行上下文管理器的__exit__
5.over!!!
```

## 4.contextmanager装饰器实现上下文管理器
使用@contextmanager装饰器实现的上下文管理器中，yield语句的作用是把函数体分为两部分
* yield前面的语句在with开始的时候执行(等同于__enter__方法)
* yield后面的语句在with结束时执行(等同于__exit__方法)

```python
from contextlib import contextmanager

@contextmanager
def open_file(filename):

    print('2.代码块执行前')
    f = open(filename, 'r', encoding='utf-8')

    yield f

    print('4.代码块执行后')
    f.close()

if __name__ == '__main__':
    print('1.start...')
    with open_file('zhibi.py') as f:
        f.read(10)
        print('3.执行代码块内容')
    print('5.over!!!')
```

```python
1.start...
2.代码块执行前
3.执行代码块内容
4.代码块执行后
5.over!!!
```
