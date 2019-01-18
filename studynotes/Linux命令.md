# Linux命令
<a href="#jump" target="_self">1、ls(查看)</a>


## <span id = "jump">1、ls（list查看）</span>
**ls [选项][文件名/目录名]**
#### [选项]
* -a：显示所有文件
* -l：显示目录下文件的详细信息（权限、所有者、大小、时间等）
* -d：显示目录信息，而不是目录下的文件
* -h：人性化显示，按照我们习惯的单位显示文件大小
#### 命令
* ls -a : 显示所有文件(包含隐藏文件)
* ls -l : 显示目录下文件的详细信息
* ls -ld : 显示某个文件夹的详细信息
* ls -lh : 人性化的方式显示文件详细信息
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_ls.png)
## 2、cd（切换目录）
#### 命令
* cd /usr/local : 切换到指定文件夹
* cd ~ : 切换到用户的家目录(root)
* cd - : 切换到上一次所在的目录
* cd ../: 切换到上级目录
## 3、mkdir（创建目录）
#### 命令
* mkdir dirname : 创建单个文件目录
* mkdir -p /dir1/dir2/dir3 : 递归创建文件夹
## 4、stat（查看文件/文件夹状态）
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_stat.png)
## 5、cat（査看文件内容） 
**cat [选项] 文件名**
#### 选项
* -n：显示行数
* -A：显示所有隐藏字符，回车符 ($)、Tab 键 (^I)等 
## 6、more（查看大文件内容）
**more是分屏显示文件的命令**
#### 命令
* 空格键：向下翻页
* b：向上翻页
* 回车：向下滚动一行
* / 字符串：搜索指定的字符串
* q：退出 
## 7、head(显示文件开头的命令)
* head -n 20 filename:指定显示行数
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_head.png)
## 8、tail(显示文件结尾的命令)
* tail -f filename: 监听文件新增的内容
## 9、rm(删除文件或目录)
**rm [选项] 文件或目录**
#### 选项
* -f: 强制删除(force)
* -r: 递归删除，可以删除目录
#### 命令
* rm -rf 目录 ： 强制递归删除(不会提示，直接默认删除)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_rm.png)
## 10、cp(复制文件)
**命令： cp 源文件 目标文件**
## 11、mv(移动文件)
**命令： mv 源文件 目标文件**<br>
**命令： mv 1.txt 2.txt 如果源文件和目标文件在同一个目录下，就相当于改名字**
## 12、whereis(搜索命令)
**whereis 命令不能搜索普通文件，而只能搜索系统命令**
## 13、locate(按照文件名搜索普通文件)
**centOS7以上的系统中使用“locate”文件查找命令,需要先安装locate命令**
* yum install mlocate
* updatedb
* locate inittab

![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_locate.png)
