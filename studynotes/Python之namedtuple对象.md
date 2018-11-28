# Python之namedtuple对象
## 一、namedtuple
在实现python中的特殊方法之前，先了解一下Python中命名元组对象，namedtuple.

**如果要构建一个只有少量属性，没有方法的类，这时候就可以使用namedtuple**

    import collections

    # 创建一个 namedtuple类，第一个参数是“类名”，第二个参数是“类的属性”
    Student = collections.namedtuple('Student', ['name', 'sex', 'age'])
    xiaoming = Student('小明', 'man', '20')

    # 查看所有属性
    print(xiaoming._fields)  #  ('name', 'sex', 'age')

    # 查看对象属性
    print(xiaoming)  # Student(name='小明', sex='man', age='20')
    print(xiaoming.name)  # 小明
    print(xiaoming.age)   # 20
    print(xiaoming.sex)   # man

    # 修改对象属性
    xiaoming = xiaoming._replace(sex='unknow')
    print(xiaoming)      # Student(name='小明', sex='unknow', age='20')

    # 将对象转换成字典，key是属性名，value是属性值
    xiaoming._asdict()   # OrderedDict([('name', '小明'), ('sex', 'unknow'), ('age', '20')])

## 二、利用namedtuple创建一副扑克牌
Python中实现 __len__方法的对象，可以直接通过len(object)调用，实现__getitem__方法的对象，是一个可迭代对象，该对象可以进行for循环遍历，可以通过[index]索引操作。

这里，通过命名元组namedtuple与特殊方法结合，实现一副扑克牌。

**如果要构建一个只有少量属性，没有方法的类，这时候就可以使用namedtuple**，这里扑克牌只有两个属性，一个是面值大小，一个是牌色(黑桃，方块，梅花，红心)

所以，创建一个扑克牌的类只需要一句话，

    Card = collections.namedtuple('Card', ['牌值', '牌色'])
    
现在创建一副扑克牌对象。

    class FrenchDeck():
        # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        ranks = [str(i) for i in range(2, 11)] + list('JQKA')
        # ['黑桃', '方块', '梅花', '红心']
        suits = '黑桃 方块 梅花 红心'.split(' ')

        def __init__(self):
            self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

        def __len__(self):
            return len(self._cards)

        def __getitem__(self, position):
            return self._cards[position]
    
![](https://github.com/daacheng/PythonBasic/blob/master/pic/namedtuple.jpg)
    
    
    
    
   
