## ==与is的区别
* ==：运算符比较两个对象的值（对象中保存的数据）
* is：is 比较对象的id标识

```python
a = [1,2,3]
b = [1,2,3]
print(a == b)  # True
print(a is b)  # False
```
