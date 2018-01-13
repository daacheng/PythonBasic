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
