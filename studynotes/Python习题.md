## 1、列表（list）和元组（tuple）的区别
相同：两者都可以包含任意类型的元素
不同：列表是可变的，元组是不可变的；可以通过namedtuple给元组的每个位置的元素命名；元组可以作为字典的key，列表不行。
## 2、set集合
set集合是无序不重复的元素集合；集合成员可以做字典的键；支持用in或not in检查成员；len()得到集合大小；for循环迭代；因为集合无序，所以不支持索引和切片，
也没有keys来获取集合中元素的值。
## 3、浮点数比较相等的情况不能通过== 或者 !=，应该是一个范围
        x=0.6
        while x<1.0:
            print(x)
            x+=0.1
        #0.6
        #0.7
        #0.7999999999999999
        #0.8999999999999999
        #0.9999999999999999

## 4、sorted的根据key排序
    students=[('a',23),('b',46),('c',24),('d',12)]
    sorted(students,key = lambda x : x[1])
## 5、map，filte，reduce与匿名函数
    from functools import reduce
    list(map(lambda x : x+1,[2,3,4]))     #[3,4,5]
    list(filter(lambda x : x>2,[2,3,4]))  #[3, 4]
    reduce(lambda x,y:x+y,[2,3,4])  #9
## 6、双端队列 deque（double-ended queue）
        from collections import deque
        d = deque([],3)
        d.append(1)
        d.append(2)
        d.append(3)
        d.append(4)
        d     #deque([2, 3, 4])
        d.appendleft(5)
        d   #deque([5, 2, 3])
