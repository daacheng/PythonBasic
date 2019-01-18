# Linux命令
<a href="#jump1" target="_self">1、ls(查看)</a><br>
<a href="#jump2" target="_self">2、cd（切换目录）</a><br>
<a href="#jump3" target="_self">3、mkdir（创建目录）</a><br>
<a href="#jump4" target="_self">4、stat（查看文件/文件夹状态）</a><br>
<a href="#jump5" target="_self">5、cat（査看文件内容）</a><br>
<a href="#jump6" target="_self">6、more（查看大文件内容）</a><br>
<a href="#jump7" target="_self">7、head(显示文件开头的命令)</a><br>
<a href="#jump8" target="_self">8、tail(显示文件结尾的命令)</a><br>
<a href="#jump9" target="_self">9、rm(删除文件或目录)</a><br>
<a href="#jump10" target="_self">10、cp(复制文件)</a><br>
<a href="#jump11" target="_self">11、mv(移动文件)</a><br>
<a href="#jump12" target="_self">12、whereis(搜索命令)</a><br>
<a href="#jump13" target="_self">13、locate(按照文件名搜索普通文件)</a><br>

## <span id = "jump1">1、ls（list查看）</span>
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
## <span id = "jump2">2、cd（切换目录）</span>
#### 命令
* cd /usr/local : 切换到指定文件夹
* cd ~ : 切换到用户的家目录(root)
* cd - : 切换到上一次所在的目录
* cd ../: 切换到上级目录
## <span id = "jump3">3、mkdir（创建目录）</span>
#### 命令
* mkdir dirname : 创建单个文件目录
* mkdir -p /dir1/dir2/dir3 : 递归创建文件夹
## 4、<span id = "jump4">stat（查看文件/文件夹状态）</span>
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_stat.png)
## <span id = "jump5">5、cat（査看文件内容） </span>
**cat [选项] 文件名**
#### 选项
* -n：显示行数
* -A：显示所有隐藏字符，回车符 ($)、Tab 键 (^I)等 
## <span id = "jump6">6、more（查看大文件内容）</span>
**more是分屏显示文件的命令**
#### 命令
* 空格键：向下翻页
* b：向上翻页
* 回车：向下滚动一行
* / 字符串：搜索指定的字符串
* q：退出 
## <span id = "jump7">7、head(显示文件开头的命令)</span>
* head -n 20 filename:指定显示行数
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_head.png)
## <span id = "jump8">8、tail(显示文件结尾的命令)</span>
* tail -f filename: 监听文件新增的内容
## <span id = "jump9">9、rm(删除文件或目录)</span>
**rm [选项] 文件或目录**
#### 选项
* -f: 强制删除(force)
* -r: 递归删除，可以删除目录
#### 命令
* rm -rf 目录 ： 强制递归删除(不会提示，直接默认删除)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_rm.png)
## <span id = "jump10">10、cp(复制文件)</span>
**命令： cp 源文件 目标文件**
## <span id = "jump11">11、mv(移动文件)</span>
**命令： mv 源文件 目标文件**<br>
**命令： mv 1.txt 2.txt 如果源文件和目标文件在同一个目录下，就相当于改名字**
## <span id = "jump12">12、whereis(搜索命令)</span>
**whereis 命令不能搜索普通文件，而只能搜索系统命令**
## <span id = "jump13">13、locate(按照文件名搜索普通文件)</span>
**centOS7以上的系统中使用“locate”文件查找命令,需要先安装locate命令**
* yum install mlocate
* updatedb
* locate inittab

![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxcmd_locate.png)
