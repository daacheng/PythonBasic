## Python中的下划线
#### 单下划线
* _XXX: “单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入.

**@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。**

```python
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

if __name__ == '__main__':
    p = Person('王大锤', 12)
    """
    '单下划线'的保护变量
    大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
    本类之外的代码在访问这样的属性时应该要保持慎重。
    这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
    """
    print(p._age)
    # 通过定义的接口访问保护变量
    print(p.age)
```
#### 双下划线
* \_\_XXX: “双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。通过对象名._类名__xxx这样的方式可以访问.

```python
class Person(object):   
    def __init__(self,name,age):  
        self.name = name  
        self.__age = age  
    def play(self):  
        print(self.name,self.__age)  

def main():  
    p = Person('王大锤',12)  
    p.play()  
    # ‘双下划綫’的私有变量，只能通过  对象名._类名__XXX才能访问，只有类自己能访问  
    print(p._Person__age)  

if __name__ == '__main__':  
    main()  
```

#### \_\_XXX__
* \_\_XXX__: 系统定义的名字,用来区别其他用户自定义的命名,通过 类.\_\_XXX__查看。

```python
Class1.__name__ # 类型名称 'Class1'   
Class1.__module__ # 类型所在模块 '__main__'   
Class1.__bases__ # 类型所继承的基类 (<type 'object'>,)   
Class1.__dict__ # 类型字典，存储所有类型成员信息。 <dictproxy object at 0x00D3AD70>   
Class1().__class__ # 类型 <class '__main__.Class1'>   
Class1().__module__ # 实例类型所在模块 '__main__'  
Class1().__dict__ # 对象字典，存储所有实例成员信息。 {'i': 1234}  
```
