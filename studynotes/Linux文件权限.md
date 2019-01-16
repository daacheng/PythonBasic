# Linux文件权限
## 权限位
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxqx.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/linux/linuxqx2.png)
通过ls -l查看文件的详细信息，第一列就是权限位。<br>
* 第一位代表文件类型，"-":普通文件。
* 第二~四位表示文件所有者权限，-r读权限，-w写权限，-x执行权限
* 第五~七位表示文件所属组权限
* 第八~十位表示文件其他人的权限
## chmod(修改权限)
**chmod 命令的权限模式的格式是"[ugoa] [+-=] [rwx]"**
* u表示所有者 user
* g表示所属组 group
* o表示其他的 others

例如：<br>
* chmod u+x 1_1.txt
* chmod g+w,o+w 1_1.txt
* chmod u=rwx 1_1.txt

### 通过数字赋予权限是最简单的
* 4表示权限r
* 2表示权限w
* 1表示权限x

**例如  chmod 755 1_1.txt   第一个数字"7"：代表所有者的权限是"4+2+1"，也就是读、写和执行权限。第二个数字"5"：代表所属组的权限是"4+1"，也就是读和执行权限。第三个数字"5"：代表其他人的权限是"4+1"，也就是读和执行权限。**
