1. [目录相关操作（cd, pwd, mkdir, rmdir）](#1)
2. [文件与目录管理（ls, cp, rm, mv, dirname, basename）](#2)
3. [查看文件内容（cat, less, more, head, tail）](#3)
4. [指令与文件的查找（which, locate, find）](#4)

## <span id="1">1.目录相关操作（cd, pwd, mkdir, rmdir）</span>
### cd:切换工作目录(change directory)
```python
. : 当前目录
.. : 上一层目录
- ： 前一个工作目录
~ : “目前使用者身份”所在的主文件夹
```

### pwd:显示当前所在的目录(print working directory)
* -P: 显示出真实的路径，而不是使用链接(link)路径。

```python
[root@iZ8vb6ughzbdqkfd58dowoZ mail]# pwd
/var/mail
[root@iZ8vb6ughzbdqkfd58dowoZ mail]# pwd -P
/var/spool/mail
```

### mkdir:创建新目录
-p:默认不加参数只能一层一层创建目录，加了-p可以直接递归创建

```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# mkdir d1
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ll
total 4
drwxr-xr-x 2 root root 4096 Feb 12 17:42 d1
[root@iZ8vb6ughzbdqkfd58dowoZ test]# mkdir d2/d3/d4
mkdir: cannot create directory ‘d2/d3/d4’: No such file or directory
[root@iZ8vb6ughzbdqkfd58dowoZ test]# mkdir -p d2/d3/d4
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
d1  d2
```

### rmdir:删除空目录
rmdir只能删除空目录，被删除的目录中肯定不能存在其他目录或者文件。
-p: 连同上层的空目录也一起删除

```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
d1  d2
[root@iZ8vb6ughzbdqkfd58dowoZ test]# rmdir d1
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
d2
[root@iZ8vb6ughzbdqkfd58dowoZ test]# rmdir d2
rmdir: failed to remove ‘d2’: Directory not empty
[root@iZ8vb6ughzbdqkfd58dowoZ test]# rmdir -p d2
rmdir: failed to remove ‘d2’: Directory not empty
[root@iZ8vb6ughzbdqkfd58dowoZ test]# rmdir -p d2/d3/d4/
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
```

## <span id="2">2.文件与目录管理（ls, cp, rm, mv, dirname, basename）</span>
**包括查看属性，复制、删除文件，移动文件或目录。**
### ls：查看
```python
-a : 查看全部文件，包括隐藏文件
-h : 将文件大小以易读的方式显示出来
-l : 显示文件的属性与权限等数据
```

### cp：复制文件或目录

```python
# 复制文件
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# cp ~/test.py test
cp: overwrite ‘test/test.py’?
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ls

# 复制整个目录到另一个目录
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# cp -r ~/py_test/ test
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ls test/
py_test  test.py

# 复制目录下所有文件到另一个目录下
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# cp -r ~/py_test/* test
cp: overwrite ‘test/test.py’? y
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ls test/
log  nohup.out  test.py
```

### rm: 移除文件或目录
```python
-f：force,强制删除
-i：删除之前会询问
-r：递归删除
```

### mv：移动文件或目录
```python
# 重命名
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ll
total 20
-rw------- 1 root root 12980 Feb 12 18:20 nohup.out
-rw-r--r-- 1 root root  1984 Feb 12 18:20 test.py
[root@iZ8vb6ughzbdqkfd58dowoZ test]# mv test.py test.py.bak
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ll
total 20
-rw------- 1 root root 12980 Feb 12 18:20 nohup.out
-rw-r--r-- 1 root root  1984 Feb 12 18:20 test.py.bak

# 移动文件
[root@iZ8vb6ughzbdqkfd58dowoZ test]# mv ~/test.py ~/test
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ll
total 76
-rw------- 1 root root 12980 Feb 12 18:20 nohup.out
-rw-r--r-- 1 root root 55288 Jan  6 11:55 test.py
-rw-r--r-- 1 root root  1984 Feb 12 18:20 test.py.bak
```
### 获取路径的文件名称和目录名
```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# dirname ~/test/nohup.out
/root/test
[root@iZ8vb6ughzbdqkfd58dowoZ test]# basename ~/test/nohup.out
nohup.out
```

## <span id="3">3.查看文件内容（cat, less, more, head, tail）</span>
* cat: 从第一行开始显示文件内容，文件行数比较少时适用，-n参数显示行号。
* more: 一页一页显示文件内容。
* less: 和more类似，less可以使用方向键上下移动，加载速度比more快。
* head：只看头几行，head -n 20 filename,只看前几行。
* tail: 只看后几行，tail -f filename持续输出。

### more的指令
* Enter: 下翻一行
* 空格键：下翻一页
* b: 向上翻页
* q: 退出

### less的指令
* Enter: 下翻一行
* 空格键：下翻一页
* b: 向上翻页
* q: 退出
* /字符串：向下查找字符串
* n: 重复前一个查找的字符串
* N: 反向查找

### 文件的时间
* modification time （mtime）：文件内容数据变化时，会更新这个时间，ll显示出来的就是这个时间。
* status time （ctime）：文件的权限与属性发生变化时会更新。
* access time （atime）：文件内容被取用时更新，如cat读取文件内容。

### 查看文件类型
```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# file test.py
test.py: Python script, UTF-8 Unicode text executable
```

## <span id="4">4.指令与文件的查找（which, locate, find）</span>
### which 寻找可执行文件
```python
# -a ：将所有由 PATH 目录中可以找到的指令均列出，而不止第一个被找到的指令名称
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# which python
/usr/bin/python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# which -a python
/usr/bin/python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# which -a ls
alias ls='ls --color=auto'
	/usr/bin/ls
```
### whereis(从一些特定的目录中查找文件文件名)
whereis主要是针对 /bin /sbin 下面的可执行文件，以及 /usr/share/man 下面的 man page 文
件，跟几个比较特定的目录来查找文件。
* whereis -l: 查看whereis查找的是哪些目录

### locate(利用数据库来查找)
locate 寻找的数据是由“已创建的数据库 /var/lib/mlocate/” 里面的数据所
搜寻到的，所以不用直接在去硬盘当中存取数据.

数据库不是实时更新的，如果需要手动更新，可以用updatedb指令。

```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# locate regular_express.txt
/root/regular_express.txt
```

### find(通过硬盘查找，速度较慢)
```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# find /root -name rootfile.txt
/root/rootfile.txt
```
