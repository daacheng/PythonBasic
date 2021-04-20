# \_\_new__()和\_\_init__()方法
* \_\_new__():是类的构造方法，在实例创建前被调用，它的作用就是创建实例并返回实例对象，是一个静态方法
* \_\_init__():是类的初始化方法，当实例对象被创建后调用，然后初始化实例对象的属性值，是一个实例方法
* new()方法先被调用，创建实例对象，然后将实例对象传递给init()方法的self,进行初始化操作

## \_\_new__()实现单例
```python
class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print('s1:{}'.format(id(s1)))
    print('s2:{}'.format(id(s2)))
    print('s1 is s2:{}'.format(s1 is s2))
```
```python
s1:1891632871352
s2:1891632871352
s1 is s2:True
```

**以上看似实现了单例模式，但实际在多线程的情况下会有问题，多个线程同时创建单例对象，如果不加锁的情况下是不安全的。**

```python
import time
import threading

class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            time.sleep(0.05)
            cls.instance = super().__new__(cls)
        return cls.instance

def func():
    s = Singleton()
    print('s:{}'.format(id(s)))

if __name__ == '__main__':
    for _ in range(5):
        # 开启5个线程同时创建对象
        td = threading.Thread(target=func)
        td.start()
```
```python
s:1230297165896
s:1230297245008
s:1230297372152
s:1230297270648
s:1230297296176
```

**多线程下创建单例对象需要加锁**

```python
import threading

class Singleton:
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # 加锁
        with cls._instance_lock:
            if not hasattr(cls, 'instance'):
                cls.instance = super().__new__(cls)
        return cls.instance

def func():
    s = Singleton()
    print('s:{}'.format(id(s)))

if __name__ == '__main__':
    for _ in range(5):
        td = threading.Thread(target=func)
        td.start()
```
