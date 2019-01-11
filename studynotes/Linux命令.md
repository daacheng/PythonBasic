# Linux命令
## 1、ls（list查看）
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
