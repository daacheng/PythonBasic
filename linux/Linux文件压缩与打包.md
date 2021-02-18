## 常见的压缩指令
* .z: compress程序压缩的文件
* .zip: zip程序压缩的文件
* .gz: gzip程序压缩的文件
* .bz2: bzip2程序压缩的文件
* .xz: xz程序压缩的文件
* .tar: tar程序打包的数据，并没有压缩
* .tar.gz: tar程序打包的文件并且经过gzip压缩
* .tar.bz2: tar程序打包的文件并且经过bzip2压缩
* .tar.xz: tar程序打包的文件并且经过xz压缩

**gzip，bzip2, xz压缩指令只能针对一个文件进行压缩与解压，如果要一次压缩一堆文件，需要先对这些文件进行打包后压缩。**
（gzip, bzip2, xz 也能够针对目录来进行压缩，不过， 这两个指令对目录的压缩指的是“将目录内的所有文件 "分别" 进行压缩”的动作）

### gzip压缩
**gzip应用最广泛，可以解开compress,zip,gzip压缩的文件。使用gzip压缩，默认情况源文件会被压缩成.gz的文件名，原始文件也就不再存在。**

gzip -d：解压缩

```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ll
total 112
-rw-r--r-- 1 root root 55288 Feb 12 19:09 test.py
-rw-r--r-- 1 root root 55288 Feb 18 10:15 test.py.bak
[root@iZ8vb6ughzbdqkfd58dowoZ test]# gzip test.py
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py.bak  test.py.gz
[root@iZ8vb6ughzbdqkfd58dowoZ test]# gzip -d test.py.gz
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py  test.py.bak
```

### bzip2压缩
```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py
[root@iZ8vb6ughzbdqkfd58dowoZ test]# bzip2 test.py
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py.bz2
[root@iZ8vb6ughzbdqkfd58dowoZ test]# bzip2 -d test.py.bz2
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py
```

### xz压缩
```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# xz test.py
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py.xz
[root@iZ8vb6ughzbdqkfd58dowoZ test]# xz -d test.py.xz
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
test.py
```

## 打包指令 tar
* -v: 在压缩/解压的过程中，将正在处理的文件名显示出来
* -c：创建打包文件
* -t：查看打包文件内容包含哪些文件名
* -x：解打包或解压缩（-c，-t，-x不可同时出现）
* -z：通过gzip进行压缩，此时文件名为‘xxx.tar.gz’
* -j：通过bzip2进行压缩，此时文件名为‘xxx.tar.bz2’
* -J：通过xz进行压缩，此时文件名为‘xxx.tar.xz’（-z，-j，-J不可同时出现）
* -C 目录：解压缩到指定目录
* -f 文件名：指定文件名

#### 打包压缩
1. tar -zcv -f xxx.tar.gz 要被压缩的文件或目录名称: 使用gzip打包压缩
2. tar -jcv -f xxx.tar.bz2 要被压缩的文件或目录名称: 使用bzip2打包压缩
3. tar -Jcv -f xxx.tar.xz 要被压缩的文件或目录名称: 使用xz打包压缩

```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
bin
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -zcv -f bin.tar.gz bin/
bin/
bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -jcv -f bin.tar.bz2 bin/
bin/
bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -Jcv -f bin.tar.xz bin/
bin/
bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# ls
bin  bin.tar.bz2  bin.tar.gz  bin.tar.xz
```

#### 查看打包的文件名
1. tar -ztv -f bin.tar.gz：查看使用gzip压缩打包的文件内容
2. tar -jtv -f bin.tar.bz2: 查看使用bzip2压缩打包的文件内容
3. tar -Jtv -f bin.tar.xz: 查看使用xz压缩打包的文件内容

```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -ztv -f bin.tar.gz
drwxr-xr-x root/root         0 2021-02-18 11:25 bin/
-rw-r--r-- root/root       145 2021-02-18 11:25 bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -jtv -f bin.tar.bz2
drwxr-xr-x root/root         0 2021-02-18 11:25 bin/
-rw-r--r-- root/root       145 2021-02-18 11:25 bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -Jtv -f bin.tar.xz
drwxr-xr-x root/root         0 2021-02-18 11:25 bin/
-rw-r--r-- root/root       145 2021-02-18 11:25 bin/hello.sh
```

#### 解打包解压缩
1. tar -zxv -f bin.tar.gz: 解压缩由gzip打包压缩的文件
2. tar -jxv -f bin.tar.bz2：解压缩由bz2打包压缩的文件
3. tar -Jxv -f bin.tar.xz：解压缩由xz打包压缩的文件
4. tar -zxv -f bin.tar.gz -C /tmp：解压缩到指定目录

```python
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -zxv -f bin.tar.gz
bin/
bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -jxv -f bin.tar.bz2
bin/
bin/hello.sh
[root@iZ8vb6ughzbdqkfd58dowoZ test]# tar -Jxv -f bin.tar.xz
bin/
bin/hello.sh
```
