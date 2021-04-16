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
    print(s1 is s2)  # True
```
