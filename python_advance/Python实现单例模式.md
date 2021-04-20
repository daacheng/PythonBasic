# Python实现单例模式
**单例模式的主要目的是保证在系统中，某个类只能有一个实例存在。比如保存系统基本配置信息的类，在很多地方都要用到，没有必要频繁创建实例与销毁实例，只需要保存一个全局的实例对象即可，这样可以减少对内存资源的占用。**

## 1.Python模块实现单例
Python模块在第一次被导入的时候会生成.pyc文件，当第二次导入的时候就会直接加载.pyc文件而不会再次执行模块代码，所以可以在模块中定义单例类并实例化对象，在用的时候直接导入这个模块的实例对象即可。
```python
class GlobalConfig:
    host = 'xxx.xxx'
    port = 3306
    username = 'username'
    password = '123123'

g = GlobalConfig()
```

## 2.利用\_\_new__()方法实现单例
**\_\_new__()是类的构造方法，在实例创建前被调用，它的作用就是创建实例并返回实例对象，是一个静态方法**

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

## 3.利用装饰器实现单例
```python
import threading

def singleton(cls):
    isntance_dict = {}
    lock_ = threading.Lock()

    def wrap(*args, **kwargs):
        with lock_:
            if 'instance' not in isntance_dict:
                isntance_dict['instance'] = cls(*args, **kwargs)
        return isntance_dict['instance']

    return wrap


@singleton
class Singleton:
    pass


def func():
    s = Singleton()
    print(s)

if __name__ == '__main__':
    for _ in range(5):
        td = threading.Thread(target=func)
        td.start()
```
