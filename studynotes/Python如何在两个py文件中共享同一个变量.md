# Python如何在两个py文件中共享同一个变量
**工作中碰到在两个python文件中，操作同一个数据结构，最开始的想法是用import的方式导入，测试发现这种方法行不通，测试如下：**

### py1.py代码：

    from py2 import *
    # 这里定义一个列表，我们希望这个列表在py2.py中操作之后，在py1.py中也能继续使用，也就是两个文件共享一个列表。
    global_list = []
    if __name__ == '__main__':
        # 这里调用py2.py的方法，往列表中添加元素
        do_something()
        print('py1.py')
        print(global_list)
        

### py2.py代码

    from py1 import global_list

    def do_something():
        global global_list
        global_list.append('a')
        global_list.append('b')
        print('py2.py')
        print(global_list)

### 打印结果，并没有实现变量的共享

    py2.py
    ['a', 'b']
    py1.py
    []

## 方法一
**然后自己试了下，通过参数的形式传过去，可以实现共享的功能**
### py1.py代码：

    from py2 import *

    global_list = []
    if __name__ == '__main__':
        # 通过参数的形式传入
        do_something(global_list)
        print('py1.py')
        print(global_list)
        
### py2.py代码

    def do_something(global_list):
        global_list.append('a')
        global_list.append('b')
        print('py2.py')
        print(global_list)

### 打印结果

    py2.py
    ['a', 'b']
    py1.py
    ['a', 'b']
## 方法二
**我去网上找到另一种方法，通过第三个文件，以类变量的方式，实现共享**
### glabalVal.py

    class globalVal:
        global_list = []
        
### py1.py

    from py2 import *
    from globalVal import globalVal

    global_list = globalVal.global_list
    if __name__ == '__main__':
        do_something()
        print('py1.py')
        print(global_list)

### py2.py

    from globalVal import globalVal

    def do_something():
        globalVal.global_list.append('a')
        globalVal.global_list.append('b')
        print('py2.py')
        print(globalVal.global_list)
        
### 打印结果
    py2.py
    ['a', 'b']
    py1.py
    ['a', 'b']
