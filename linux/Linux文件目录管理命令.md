## 文件目录管理命令
(touch,mkdir,cp,mv,rm,dd,file)
#### 1.touch命令
**用于创建空白文件或设置文件时间。touch -d file：同时修改文件的读取时间和修改时间。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ls -l test.txt
-rw-r--r-- 1 root root 857 Feb 17 20:02 test.txt
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# vim test.txt
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ls -l test.txt
-rw-r--r-- 1 root root 863 Feb 17 20:30 test.txt
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# touch -d "2019-02-17 11:10" test.txt
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ls -l test.txt
-rw-r--r-- 1 root root 863 Feb 17  2019 test.txt
```
#### 2.mkdir命令
**用于创建空白目录。-p:递归创建**
#### 3.cp命令
**用于复制文件或目录。**
- 如果目标文件是目录，则会把源文件复制到该目录中。
- 如果目标文件是普通文件，则提示是否要覆盖。
- 如果目标文件不存在，则执行正常的复制操作。

```
[root@iZ8vb6ughzbdqkfd58dowoZ test]# touch install.log
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
install.log
[root@iZ8vb6ughzbdqkfd58dowoZ test]# cp install.log X.log
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
install.log  X.log
```
#### 4.mv命令
**用于剪切文件或重命名。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
install.log  X.log
[root@iZ8vb6ughzbdqkfd58dowoZ test]# mv X.log linux.log
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
install.log  linux.log
```
#### 5.rm命令
**删除文件或目录。**
#### 6.dd命令
**用于按照指定大小和个数的数据块来复制文件或转换文件。**

参数 | 作用
---|---
if | 输入的文件
of | 输出的文件
bs | 设置每个块的大小
count | 设置要复制块的个数

#### 7.file命令
**用于查看文件的类型。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# file test.txt
test.txt: ASCII text
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# file Python-3.6.4
Python-3.6.4: directory
```
