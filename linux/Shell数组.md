# Shell数组
### 访问数组元素
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# arr=(11 22 33 aa bb cc)
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr[0]}
11
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr[1]}
22
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr[2]}
33
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr[3]}
aa
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr[*]}
11 22 33 aa bb cc
```

### 获取数组长度
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${#arr[*]}
6
```

### 合并数组
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# arr1=(a b c)
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# arr2=(d e f)
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# arr3=(${arr1[*]} ${arr2[*]})
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr3[*]}
a b c d e f
```

### 删除数组元素
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# unset arr[0]
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${arr[*]}
22 33 aa bb cc
```

### 关联数组(字典)
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# declare -A color
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${color[*]}

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# color["red"]="#ff0000"
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# color["green"]="#00ff00"
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# color["blue"]="#0000ff"

# 获取keys
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${!color[*]}
red blue green

# 获取values
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${color[*]}
#ff0000 #0000ff #00ff00
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${color["red"]}
#ff0000
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${color["blue"]}
#0000ff

# 获取数组长度
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${#color[*]}
3

```
