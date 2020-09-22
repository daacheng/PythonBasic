## 系统状态监测命令
系统状态监测命令(ifconfig,uname,uptime,free,who,last,history)

#### 1.ifconfig命令
**用于获取网卡配置与网络状态等信息。使用ifconfig，其实主要是查看网卡名称，inet参数后面的IP地址，ether参数后面的MAC地址，以及RX，TX的接收数据包与发送数据包的个数及累计流量。**
#### 2.uname命令(用于查看系统内核与系统版本等信息)
使用 uname -a查看当前系统的内核名称，主机名，内核发行版本，节点名，系统时间，硬件名称，硬件平台，处理器类型以及操作系统名称等。

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# uname -a
Linux iZ8vb6ughzbdqkfd58dowoZ 3.10.0-957.21.3.el7.x86_64 #1 SMP Tue Jun 18 16:35:19 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
```
查看当前系统的版本信息：

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# cat /etc/redhat-release
CentOS Linux release 7.6.1810 (Core)
```
#### 3.uptime命令
**查看系统的负载信息。显示当前系统时间，系统运行时间，启用终端数量，以及平均负载值。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# uptime
 21:09:22 up 192 days,  6:21,  2 users,  load average: 0.00, 0.02, 0.05
```
#### 4.free命令
**用于显示当前系统中内存的使用量信息。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# free -h
              total        used        free      shared  buff/cache   available
Mem:           991M        399M         61M        496K        529M        427M
Swap:            0B          0B          0B
```
#### 5.who命令
**查看当前登入主机的用户终端信息。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# who
root     pts/0        2020-02-16 19:23 (27.18.67.16)
root     pts/1        2020-02-16 19:23 (27.18.67.16)
```
#### 6.last命令
**查看所有系统的登录记录。**

```
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# last
root     pts/1        27.18.67.16      Sun Feb 16 19:23   still logged in   
root     pts/0        27.18.67.16      Sun Feb 16 19:23   still logged in   
root     pts/1        113.57.168.74    Thu Sep 19 16:35 - 17:32  (00:56)    
root     pts/0        113.57.168.74    Thu Sep 19 16:31 - 16:35  (00:04)
```
#### 7.history命令
**显示历史执行过的命令。历史命令会被保存到用户家目录中.bash_history文件中，.开头的均表示是隐藏文件，可以通过 "cat ~/.bash_history"查看，也可以通过"history -c"命令，清空当前用户在本机上执行的linux命令历史记录信息。**
