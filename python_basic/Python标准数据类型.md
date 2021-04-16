# Python标准数据类型
python3中有六种标准数据类型

* Number:数字，包含int，float，bool，complex（复数）
```python
# bool型也是数字
print(True + True)  # 2
```
* String:字符串
* List:列表
* Tuple:元组
* Set:集合
* Dict:字典

## 可变类型与不可变类型
* 可变类型：在id(内存地址)不变的情况下，值可以变化
* 不可变类型：值一旦发生变化，id(内存地址)也改变，意味着开辟了新的内存空间。
#### 可变数据类型：List，Set，Dict
#### 不可变数据类型：Number，String，Tuple

## type与isinstance的区别
* type()不认为子类是一种父类类型
* isinstance()认为子类是一种父类类型

```python
class A:
    pass

class B(A):
    pass

if __name__ == '__main__':
    a = A()  # 父类
    b = B()  # 子类
    print(type(a) is A)  # True
    print(type(b) is A)  # False, type()不认为子类是一种父类类型
    print(isinstance(a, A))  # True
    print(isinstance(b, A))  # True, isinstance()认为子类是一种父类类型
```
