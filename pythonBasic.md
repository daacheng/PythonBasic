# PythonBasic
python基础知识
## 11. python类变量和实例变量
类变量：类的所有实例之间共享的值，它们不是单独分配给每个实例的。

实例变量： 实例化之后，每个实例单独拥有的变量。

    class Test(object):  
    
        num_of_instance = 0
        
        def __init__(self, name):
        
            self.name = name  
              
            Test.num_of_instance += 1  

    if __name__ == '__main__':  
          
        print（Test.num_of_instance）   # 0
          
        t1 = Test('jack')  
          
        print（Test.num_of_instance）   # 1
          
        t2 = Test('lucy')  
          
        print（t1.name , t1.num_of_instance） # jack 2
          
        print（t2.name , t2.num_of_instance）  # lucy 2
## 12. python自省
自省： 检查某些事物以确定它是什么、它知道什么以及它能做什么。

    dir(obj): 方法将返回包含obj大多数属性名的列表.

    hasattr(obj, attr): 用于检查obj是否有一个名为attr的属性，返回一个布尔值。

    getattr(obj, attr): 调用这个方法将返回obj中名为attr的属性的值，例如如果attr为'bar'，则返回obj.bar。

    setattr(obj,attr,value):设置obj的attr属性的值为value。

    type():判断obj的类型。

    isinstance():  isinstance("ass",str) #True
## 13. python中的下划线
_XXX  不能用from module import * 导入

__XXX  类中的私有变量名，只有本类能访问，子类也不能访问。

    __XXX__  系统定义的名字,用来区别其他用户自定义的命名  Class1.__doc__ # 类型帮助信息 'Class1 Doc.' 
    
    >>> Class1.__name__ # 类型名称 'Class1' 
    
    >>> Class1.__module__ # 类型所在模块 '__main__' 
    
    >>> Class1.__bases__ # 类型所继承的基类 (<type 'object'>,) 
    
    >>> Class1.__dict__ # 类型字典，存储所有类型成员信息。 <dictproxy object at 0x00D3AD70> 
    
    >>> Class1().__class__ # 类型 <class '__main__.Class1'> 
    
    >>> Class1().__module__ # 实例类型所在模块 '__main__'
    
    >>> Class1().__dict__ # 对象字典，存储所有实例成员信息。 {'i': 1234}


“单下划线” 开始的成员变量叫做保护变量，意思是只有类对象和子类对象自己能访问到这些变量；单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入

“双下划线” 开始的是私有成员，意思是只有类对象自己能访问，连子类对象也不能访问到这个数据。通过对象名._类名__xxx这样的方式可以访问.

        class A:
            def _method1(self): # 不能通过from module import * 导入，只能通过类对象，或者子类对象访问。
                print("A")
            def __method2():#私有方法 ，只有A类能访问，子类也不能访问 通过对象._A__method2()访问
                pass
        class B(A):
            def __method2():
                pass
        #dir(A)  #['_A__method2','_method1']
        #dir(B)#['_A__method2', '_B__method2','_method1']
        a=A()
        b=B()
        a._method1()#A
        b._method1()#A
## 14. python中格式化字符串
%d 整数

%f 浮点数

%s 字符串

%x 十六进制整数

        print('hello %s,you are %d' %('aaa',11))

## 15. python可迭代对象（Iterable）迭代器（iterator）和生成器（generator）
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象（Iterable）。可迭代对象包含一个__iter__方法，或__getitem__方法，其中__iter__方法返回一个迭代器(iterator).可迭代对象一类是集合数据类型，如list，tuple，dict，set，str；一类是生成器generator。

迭代器：可以作用于next()方法的对象都是迭代器对象。迭代器对象必须实现__next__()方法。

生成器：实现了__iter__()方法和__next__()方法，生成器是Iterable也是iterator。可以作用于for循环。

生成器函数：在函数中如果出现了yield关键字，那么这个函数就是生成器函数。yield的作用就是生成一个生成器generator。生成器函数返回一个生成器generator。

### 原理
for循环的时候，如果循环的是Iterable可迭代对象，会调用Iterable的__iter__()方法，返回一个迭代器，然后调用迭代器的__next__()方法，直到遇到StopIteration异常跳出循环。
如果循环的是iterator迭代器，直接调用他的__next__()方法，直到遇到StopIteration异常跳出循环。
### 实现一个迭代器和一个可迭代对象

        from collections import Iterator
        class AIterator(Iterator):
            def __init__(self,s,e):
                self.current=s
                self.end=e
              def __next__(self):
                if self.current<self.end:
                    self.index=self.current
                    self.current+=1
                    return self.index
                else:
                    raise StopIteration
        class AIterable():
            def __init__(self,s,e):
                self.s=s
                self.e=e
            def __iter__(self):
                return AIterator(self.s,self.e)
        a=AIterable(2,5)
        print(a) #<__main__.AIterable object at 0x0000023877599A90>
        for x in a:
            print(x)
### 实现一个生成器
1. 把列表的[]换成(),就创建了一个生成器。
        
        l=[x for x in range(10)]
        g=(x for x in range(10))
2. 通过yield关键字。生成器函数返回一个生成器。节省开销。

    Python生成器是创建迭代器的简单方法。

    1、调用生成器函数，返回一个生成器。

    2、调用生成器的next()方法时，生成器才开始执行生成器函数，直到遇到yield时暂停执行（挂起），并且yield的参数将作为此次next方法的返回值。

    3、之后每次调用生成器的next方法，生成器将从上次暂停执行的位置恢复执行生成器函数，直到再次遇到yield时暂停，并且同样的，yield的参数将作为next方法的返回值。
## python中的参数（位置参数，默认参数，可变参数，关键字参数，命名关键字参数）
1. 位置参数
        
        def power(x,n): # x,n是位置参数，传入的值按照位置依次赋值给x，n
            pass
2. 默认参数

        def power(x,n=2): # n是默认参数，默认值为2
            pass
3. 可变参数\*args，当不确定函数里要传入多少参数时，可以用可变参数\*args
    
        def methoda(*numbers):
            pass
        methoda(1,2,3) # 可以传入任意个数参数（包括0个），参数numbers接收到的是一个tuple。
        methoda(1,2,3,4,5,6)

4. 关键字参数\**Kwargs,允许你使用没有事先定义的参数名

  可变参数允许传入0或多个参数，这些参数在函数调用时自动组成一个tuple。

  关键字参数运行传入0或多个值，这些关键字参数在函数调用时自动组成一个dict。

    def table_things(**kwargs):
        pass
    table_things(apple = 'fruit', cabbage = 'vegetable')
5. 参数顺序。 必选参数，默认参数，可变参数，命名关键字参数，关键字参数。
