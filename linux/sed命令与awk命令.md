## sed命令
#### sed [-nefri] [动作]
* -n: 使用安静模式，一般sed中，所有来自STDIN的数据都会输出在屏幕上，加上-n后，只有经过sed处理的那一行才会显示出来
* -e: 直接在命令行界面进行sed动作编辑
* -f filename: 直接将sed的动作写在一个文件内，-f filename则可以执行filename内的动作
* -r: 支持延伸正则表达式语法（默认支持基础正则表达式语法）
* -i: 直接修改文件内容
* 动作：'n1,n2动作'，表示对n1-n2行的数据进行处理，sed后面接的动作要用单引号包起来
```python
a: 新增，a后面接的字符串会新增在当前行的下一行
c: 取代，c后面接的字符串会替代n1,n2之间的行
d：删除
i: 插入，i后面接的字符串会新增在当前行的上一行
p: 打印，配合-n使用
s: 取代，搭配正则表达式'1,20s/old/new/g'
```

#### 以行为单位新增/删除/取代/显示
* sed '10,21d': 删除10-21行的数据
* sed '1a 6666666666new line'：在第一行下面新增一行
* sed '1,21c 111111111111': 替换1-21行之间的内容，多行用反斜杠换行
* sed -n '2,4p'：打印第2-4行
```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# nl regular_express.txt
     1	"Open Source" is a good mechanism to develop programs.
     2	apple is my favorite food.
     3	Football game is not use feet only.
     4	this dress doesn't fit me.
     5	However, this dress is about $ 3183 dollars.
     6	GNU is free air not free beer.
     7	Her hair is very beauty.
     8	I can't finish the test.
     9	Oh! The soup taste good.
    10	motorcycle is cheap than car.
    11	This window is clear.
    12	the symbol '*' is represented as start.
    13	Oh!	My god!
    14	The gd software is a library for drafting programs.
    15	You are the best is mean you are the no. 1.
    16	The world <Happy> is the same with "glad".
    17	I like dog.
    18	google is the best tools for search keyword.
    19	goooooogle yes!
    20	go! go! Let's go.
    21	# I am VBird
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# nl regular_express.txt | sed '10,21d'
     1	"Open Source" is a good mechanism to develop programs.
     2	apple is my favorite food.
     3	Football game is not use feet only.
     4	this dress doesn't fit me.
     5	However, this dress is about $ 3183 dollars.
     6	GNU is free air not free beer.
     7	Her hair is very beauty.
     8	I can't finish the test.
     9	Oh! The soup taste good.
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# nl regular_express.txt | sed '1a 6666666666new line'
     1	"Open Source" is a good mechanism to develop programs.
6666666666new line
     2	apple is my favorite food.
     3	Football game is not use feet only.
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# nl regular_express.txt | sed '1,21c 111111111111 \
> 222222222 \
> 333333333'
111111111111
222222222
333333333
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# nl regular_express.txt | sed -n '2,4p'
     2	apple is my favorite food.
     3	Football game is not use feet only.
     4	this dress doesn't fit me.
```

#### 部分数据的搜寻与取代
**获取ip地址**
```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ifconfig eth0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.26.207.57  netmask 255.255.240.0  broadcast 172.26.207.255
        ether 00:16:3e:02:7d:8e  txqueuelen 1000  (Ethernet)
        RX packets 6154955  bytes 1792889184 (1.6 GiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 7192355  bytes 1144293676 (1.0 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ifconfig eth0 | grep inet
        inet 172.26.207.57  netmask 255.255.240.0  broadcast 172.26.207.255

# 去掉ip前面的字符
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ifconfig eth0 | grep inet | sed 's/^.*inet //g'
172.26.207.57  netmask 255.255.240.0  broadcast 172.26.207.255

# 去掉ip后面的字符
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# ifconfig eth0 | grep inet | sed 's/^.*inet //g' | sed 's/ *netmask.*$//g'
172.26.207.57
```

## 2.awk命令
sed以行为单位处理数据，awk倾向于将一行分成多个字段来处理。格式： awk '条件1{动作1} 条件2{动作2}' filename

* 获取最近5位登录者信息及IP： last -n 5 | awk '{print $1 "\tIP: " $3}'
* awk命令默认分隔符是空白键/tab，每一行的每一个字段都有变量名称，$1就表示第一个字段, $3表示第三个字段， $0表示当前行
* awk内置变量：NF表示每一行的字段总数，NR表示当前行数，FS表示分隔字符

```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# last -n 5
root     pts/0        219.140.224.23   Mon Feb 22 09:44   still logged in   
root     pts/0        219.140.224.23   Thu Feb 18 10:13 - 14:21  (04:08)    
root     pts/0        39.149.216.245   Tue Feb 16 21:25 - 21:43  (00:17)    
root     pts/1        39.149.216.245   Tue Feb 16 19:11 - 20:02  (00:50)    
root     pts/0        39.149.216.245   Tue Feb 16 18:50 - 19:11  (00:20)    

wtmp begins Thu Jul 11 11:10:20 2019
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# last -n 5 | awk '{print $1 "\tIP: " $3}'
root	IP: 219.140.224.23
root	IP: 219.140.224.23
root	IP: 39.149.216.245
root	IP: 39.149.216.245
root	IP: 39.149.216.245
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# last -n 5 | awk '{print "line: " NR "; columns: " NF "; "$1}'
line: 1; columns: 10; root
line: 2; columns: 10; root
line: 3; columns: 10; root
line: 4; columns: 10; root
line: 5; columns: 10; root
```

#### awk命令处理流程
1. 读入第一行数据，并将第一行的数据填入变量$0,$1,$2,...
2. 依据条件判断是否执行条件后面的动作
3. 做完所有的条件与动作
4. 读取下一行，重复1-3

#### awk条件
获取/etc/paswd中uid大于3的用户：cat /etc/passwd | awk 'BEGIN {FS=":"} $3 > 10{print $1 "\t" $3}'
```python
[root@iZ8vb6ughzbdqkfd58dowoZ ~]# cat /etc/passwd | awk '{FS=":"} $3 > 10{print $1 "\t" $3} '
operator	11
games	12
ftp	14
nobody	99
```
