# Shell变量
## 1.声明变量、使用变量、删除变量
#### 声明变量
```python
# 方式一
var=abc
# 方式二
var='abc'
# 方式三
var="abc"
```
#### 使用变量
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var=abc
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $var
abc
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo ${var}
abc
```
#### 单引号与双引号区别
* 用单引号包围变量值时，单引号里内容是什么就输出什么，原样输出字符串
* 用双引号包围变量值时，输出时会先解析里面的变量和命令，再输出解析后的字符串

```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var=abc
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# info='var is ${var}'
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $info
var is ${var}
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# info="var is ${var}"
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $info
var is abc
```
#### 只读变量
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# readonly var
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# var=def
-bash: var: readonly variable
```
#### 删除变量
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $info
var is abc
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# unset info
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $info

```
#### 把命令的结果赋值给变量
* 方式一,反引号
* 方式二，$()
* 如果被替换的命令的输出内容包括多行，或者含有多个连续的空白符，那么在输出变量时应该将变量用双引号包围，否则系统会使用默认的空白符来填充，这会导致换行无效，以及连续的空白符被压缩成一个。

```python
# 方式一,反引号
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# cmd=`ls`
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $cmd
hello.sh shell_1.sh shell_2.sh shell_3.sh shell_4.sh shell_5.sh shell_6.sh
# 方式二，$()
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# cmd=$(ll -lh)
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo $cmd
total 28K -rw-r--r-- 1 root root 145 Feb 24 16:50 hello.sh -rwxrwxrwx 1 root root 149 Mar 3 16:23 shell_1.sh -rwxrwxrwx 1 root root 333 Mar 3 16:40 shell_2.sh -rwxrwxrwx 1 root root 67 Mar 3 16:46 shell_3.sh -rwxrwxrwx 1 root root 79 Mar 3 17:05 shell_4.sh -rwxrwxrwx 1 root root 78 Mar 4 11:30 shell_5.sh -rwxrwxrwx 1 root root 114 Mar 4 13:41 shell_6.sh
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# echo "$var"
total 32K
-rw-r--r-- 1 root root 145 Feb 24 16:50 hello.sh
-rwxrwxrwx 1 root root 149 Mar  3 16:23 shell_1.sh
-rwxrwxrwx 1 root root 333 Mar  3 16:40 shell_2.sh
-rwxrwxrwx 1 root root  67 Mar  3 16:46 shell_3.sh
-rwxrwxrwx 1 root root  79 Mar  3 17:05 shell_4.sh
-rwxrwxrwx 1 root root  78 Mar  4 11:30 shell_5.sh
-rwxrwxrwx 1 root root 114 Mar  4 13:41 shell_6.sh
-rwxrwxrwx 1 root root  79 Mar  4 16:02 shell_7.sh
```

## 2.变量的作用域
#### 局部变量：只在函数内部使用，定义时要用local声明，如果不加local，则是表示全局变量
```python
#!/bin/bash

function func(){
    a=123  # 全局变量
    local b=333  # 局部变量
}
func
echo $a  # 123
echo $b  # 空
```
#### 全局变量
**shell中定义的变量默认就是全局变量，仅在当前shell进程中有效。**
#### 环境变量
**全局变量只在当前shell进程中有效，对其他shell进程和子进程无效。如果通过export命令将全局变量导出，就是环境变量，在子进程中也有效。**
通过export导出的环境变量只对当前进程及其子进程有效，如果顶层的父进程被关闭，环境变量也就消失了。如果要让一个变量在所有的shell中都有效，可以将变量写入shell配置文件中，shell进程每次启动时候进行初始化。
