# python异常处理机制
python主要支持5种异常机制
## 1.默认的异常处理
如果没有对异常做任何处理，程序执行过程中，发生了异常，就会中断，调用python默认的异常处理器，并在终端输出异常信息。
```python
if __name__ == '__main__':
    a = [1, 2]
    a[10] = 10
    print(a)

Traceback (most recent call last):
  File "C:/Users/daacheng.py", line 3, in <module>
    a[10] = 10
IndexError: list assignment index out of range
```

## 2.try...except...
利用try-except语句捕捉可能产生的异常并做相应的处理,之后程序继续向下执行
```python
if __name__ == '__main__':
    try:
        a = [1, 2]
        a[10] = 10
        print(a)
    except IndexError as e:
        # 捕捉异常并处理
        print('出现索引异常')
    print('over')

出现索引异常
over
```

## 3.try...except...finally...
无论是否发生异常，finally都会被执行
```python
if __name__ == '__main__':
    try:
        a = [1, 2]
        a[10] = 10
        print(a)
    except IndexError:
        print('出现索引异常')
    finally:
        print('执行finally')
    print('over')

出现索引异常
执行finally
over
```

## 4.assert语句
assert（断言）用于判断一个表达式，在表达式条件为 False 的时候触发异常,中断程序，表达式为True时继续向下执行。

```python
assert 表达式

或者

# 当表达式为False时，执行代码块，抛出异常
assert 表达式, 代码块
```

```python
if __name__ == '__main__':
    assert 1 == 2, print('1不等于2')

1不等于2
Traceback (most recent call last):
File "C:/Users/daacheng.py", line 2, in <module>
  assert 1 == 2, print('1不等于2')
AssertionError: None
```

## 5.with...as...
不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等
