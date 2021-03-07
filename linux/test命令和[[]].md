## test命令
test是shell内置命令，用来检测条件是否成立，通常和if一起用
```python
test 表达式
# 或者简写，表达式和[] 之间必须有空格
[ 表达式 ]
```

### test文件检测
* test -e filename: 判断文件是否存在
* test -r filename: 判断文件是否存在，并且是否拥有读权限
* -w filename: 判断文件是否存在，并且是否拥有写权限
* -x filename: 判断文件是否存在，并且是否拥有执行权限
* filename1 -nt filename2: 判断 filename1 的修改时间是否比 filename2 的新
* filename -ot filename2: 判断 filename1 的修改时间是否比 filename2 的旧
* filename1 -ef filename2: 判断 filename1 是否和 filename2 的 inode 号一致，可以理解为两个文件是否为同一个文件,这个判断用于判断硬链接是很好的方法

### test数值比较
* num1 -eq num2：判断 num1 是否和 num2 相等
* num1 -ne num2：判断 num1 是否和 num2 不相等
* num1 -gt num2：判断 num1 是否大于 num2
* num1 -lt num2：判断 num1 是否小于 num2
* num1 -ge num2：判断 num1 是否大于等于 num2
* num1 -le num2：判断 num1 是否小于等于 num2

### test字符串判断
* -z str：判断字符串 str 是否为空
* -n str：判断宇符串 str 是否为非空
* str1 = str2，str1 == str2：=和==是等价的，都用来判断 str1 是否和 str2 相等
* str1 != str2：判断 str1 是否和 str2 不相等

### 逻辑运算
* expression1 -a expression:逻辑与，表达式 expression1 和 expression2 都成立，最终的结果才是成立的
* expression1 -o expression2	: 	逻辑或，表达式 expression1 和 expression2 有一个成立，最终的结果就成立
* !expression:逻辑非，对 expression 进行取反。


## [[]]用法
[[]]是shell内置关键字，也是用来检测条件是否成立，可以认为是test的升级版
```python
# 表达式成立时退出状态为 0，否则为非 0 值
[[ 表达式 ]]
```

```python
#!/bin/bash

read -p "请输入s1: " s1
read -p "请输入s2: " s2

if [[ -z $s1 ]] || [[ -z $s2 ]]
then
    echo "字符串不能为空"
else
    echo "s1:$s1  s2:$s2"
fi

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入s1: aaa
请输入s2:
字符串不能为空
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
请输入s1: aaa
请输入s2: bbb
s1:aaa  s2:bbb
```

#### [[]]支持正则表达式
```python
[[ str =~ regex ]]
```

```python
#!/bin/bash

read tel
if [[ $tel =~ ^1[0-9]{10}$ ]]
then
    echo "手机号：$tel"
else
    echo "手机号格式不正确"
fi

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
13000010002
手机号：13000010002
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
123456qwer
手机号格式不正确
```

**使用if条件时，用(())来判断数值，用[[]]来处理字符串或者文件**
