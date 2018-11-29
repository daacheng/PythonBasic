# Python中的单下划线与双下划线
#### 单下划线 保护变量

    class Person(object):

        def __init__(self,name,age):
            self.name = name
            self._age = age

        def play(self):
            print(self.name,self._age)

    def main():
        p = Person('王大锤',12)
        p.play()
        """
        '单下划线'的保护变量
        大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，
        本类之外的代码在访问这样的属性时应该要保持慎重。
        这种做法并不是语法上的规则，单下划线开头的属性和方法外界仍然是可以访问的，所以更多的时候它是一种暗示或隐喻
        """
        print(p._age)

    if __name__ == '__main__':
        main()
#### 双下划线 私有变量

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
#### 私有变量可以通过装饰器@property访问

    class Person(object):

        def __init__(self,name,age):
            self.name = name
            self.__age = age

        @property
        def age(self):
            # 相当于get_age()
            return self.__age

        @age.setter
        def age(self,age):
            # 相当于set_age()
            self.__age = age

        def play(self):
            print(self.name,self.__age)

    def main():
        p = Person('王大锤',12)
        p.play()
        print(p.age)
        p.age = 13
        # ‘双下划綫’的私有变量，只能通过  对象名._类名__XXX才能访问，只有类自己能访问
        print(p._Person__age)
        # 加了装饰器之后，私有变量可以直接通过对象名访问
        print(p.age)

    if __name__ == '__main__':
        main()
