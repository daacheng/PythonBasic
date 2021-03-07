# Shell数学计算
## 1.shell数学计算命令
* (( ))：用于整数运算，推荐使用
* let：用于整数运算，与(())类似
* $[]: 用于整数运算
* expr: 可用于整数运算，不推荐
* bc: linux下的计算器程序，可处理整数和小数，shell本身只支持整数运算，要计算小数得使用bc计算器
* declare -i: 将变量定义为整数，然后进行数学运算的时候就不会被当做字符串

## 2.shell(())
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# ((a=1+3))
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $a
4
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# a=$((2*4))
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $a
8
# 1表示真,0表示假
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $((a==8))
1
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $((a+10))
18
```

## 3.let "表达式"
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# let "a=1+1"
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $a
2
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# let b=3*4
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $b
12
```

## 4.declare
```python
# 除了将a,b定义为整数，还必须将c定义为整数，如果不这样做，在执行c=$a+$b时，Shell依然会将a、b视为字符串。
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# declare -i a b c
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# a=11
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# b=12
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# c=$a+$b
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $c
23

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# d=$a+$b
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $d
11+12
```
