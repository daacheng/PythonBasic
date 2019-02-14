# Python之装饰器
参考：
[万字长文深度解析Python装饰器](https://zhuanlan.zhihu.com/p/53837833)<br>
[python装饰器-博客园](https://www.cnblogs.com/mingo724/p/7158189.html)
## 一、装饰器两大原则
**装饰器可以理解为让其他函数在不需要做任何代码变动的前提下增加额外功能(为已经存在的函数或对象添加额外的功能)。装饰器有两大原则：**
* 原则一：不能修改“被装饰函数”的源代码。
* 原则二：不能修改“被装饰函数”的调用方式。
## 二、实现一个最简单的装饰器
### 2.1、场景
测试一个函数的运行时间。比如:测试foo()函数的运行时间

    def foo():
        time.sleep(2)
        print('in the foo!')
**下面两种方式都可以实现测试函数运行时间的功能，但都不满足装饰器原则**
#### 方式一

    def foo():
        """
            违反原则一，不能修改“被装饰函数”的源代码。
        """
        start_time = time.time()
        time.sleep(2)
        print('in the foo!')
        end_time = time.time()
        print('run time is ', end_time-start_time)

    if __name__ == '__main__':
        foo()

#### 方式二

    def foo():
        time.sleep(2)
        print('in the foo!')

    def count_time(func):
        """
        这样做虽然并不改变“被装饰函数”的源代码，但是，
        违反原则二：不能修改“被装饰函数”的调用方式。
        """
        start_time = time.time()
        func()
        end_time = time.time()
        print('run time is ', end_time - start_time)

    if __name__ == '__main__':
        count_time(foo)

### 2.2、思考
* **方式二已经比较接近了，它并没有修改“被装饰函数”的源代码，只是改变了函数的调用方式（count_time(foo)）。**<br>
* **为了同时满足装饰器两大原则，我们希望，在执行foo()时候，实际执行的是count_time中的这段代码：**

      start_time = time.time()
      func()
      end_time = time.time()
      print('run time is ', end_time - start_time)
* **这样，既没有修改“被装饰函数”的调用方式，也没有修改“被装饰函数”的源代码。**
### 2.3、实现
**我们把上面那段代码封装到deco嵌套函数中，变成这样：**

        def count_time(func):
            def deco():
                start_time = time.time()
                func()
                end_time = time.time()
                print('run time is ', end_time - start_time)
            return deco
**对于原函数，改变：**

        @count_time
        def foo():
            time.sleep(2)
            print('in the foo!')
**python中，通过@语法糖实现。在调用foo()的时候，@count_time语法实际上是相当于:**

        deco = count_time(foo)
        deco()
**所以调用foo(),实际执行的是嵌套函数deco().**<br>
**这样，既没有修改“被装饰函数”的源代码，也没有修改“被装饰函数”的调用方式。**
### 2.4、这样就实现一个简单的装饰器了

    def count_time(func):
        def deco():
            start_time = time.time()
            func()
            end_time = time.time()
            print('run time is ', end_time - start_time)
        return deco

    @count_time
    def foo():
        time.sleep(2)
        print('in the foo!')

    if __name__ == '__main__':
        foo()
### 2.5、“被装饰函数”带参数的情况
**如果“被装饰函数”带有参数，可以利用python的可变参数和关键字参数解决**

    def count_time(func):
        def deco(*args, **kwargs):
            start_time = time.time()
            func(*args, **kwargs)
            end_time = time.time()
            print('run time is ', end_time - start_time)
        return deco

    @count_time
    def foo(arg):
        time.sleep(2)
        print('in the foo! ', arg)

    if __name__ == '__main__':
        foo('aaa')
## 三、带参数的装饰器
**对于带参数的装饰器，需要多一层嵌套关系。比如，实现一个装饰器，控制"被装饰函数"的执行次数。**

    def repeat(num):
        def actual_deco(func):
            def deco(*args, **kwargs):
                for _ in range(num):
                    print('执行第%d次' % num)
                    func(*args, **kwargs)
            return deco
        return actual_deco

    @repeat(num=3)
    def foo(arg):
        print('in the foo! ', arg)

    if __name__ == '__main__':
        foo('aaa')
## 四、类装饰器
**类装饰器必须实现__call__()方法**

    class count_time:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            start_time = time.time()
            self.func()
            end_time = time.time()
            print('run time is ', end_time - start_time)

    @count_time
    def foo():
        time.sleep(2)
        print('in the foo!')

    if __name__ == '__main__':
        foo()
