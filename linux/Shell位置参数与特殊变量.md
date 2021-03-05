# Shell位置参数与特殊变量
## 1.位置参数
* $0:执行的shell脚本
* $n:n>0,表示第n个参数

```python
#!/bin/bash

echo "参数1:$1"
echo "参数2:$2"
echo "参数3:$3"
echo "参数0:$0"

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_2.sh xiaoming 18 man
参数1:xiaoming
参数2:18
参数3:man
参数0:/root/bin/shell_2.sh
```

**给函数传递参数：**
```python
#!/bin/bash

function func(){
    echo "函数参数1：$1"
    echo "函数参数2：$2"
    echo "函数参数0：$0"
}

func xiaoming 18岁

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_2.sh
函数参数1：xiaoming
函数参数2：18岁
函数参数0：/root/bin/shell_2.sh
```

## 2.特殊变量
* $0:当前脚本的文件名
* $n(n>0):传递给脚本或函数的参数。n 是一个数字，表示第几个参数
* $#:传递给脚本或函数的参数个数
* $*:传递给脚本或函数的所有参数
* $@:传递给脚本或函数的所有参数
* $?:上个命令的退出状态，或函数的返回值
* $$:当前 Shell 进程 ID

```python
#!/bin/bash

echo "当前脚本:$0"
echo "参数个数:$#"
echo "第一个参数:$1"
echo "所有参数:$*"
echo "所有参数:$@"
echo "进程ID:$$"

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_3.sh a1 a2 a3
当前脚本:/root/bin/shell_3.sh
参数个数:3
第一个参数:a1
所有参数:a1 a2 a3
所有参数:a1 a2 a3
进程ID:5333
```

**$* 和 $@的区别**
* 当 $* 和 $@ 不被双引号" "包围时，它们之间没有任何区别，都是将接收到的每个参数看做一份数据，彼此之间以空格来分隔
* 当 $* 被双引号包围时，会将所有的参数从整体上看做一份数据，而不是把每个参数都看做一份数据
* 当 $@ 被双引号包围时，仍然将每个参数都看作一份数据，彼此之间是独立的

```python
#!/bin/bash

echo '$*结果:'
for arg in $*
do
    echo $arg
done

echo '##############'
echo '$@结果:'

for arg in $@
do
    echo $arg
done

echo '##############'
echo '"$*"结果:'
for arg in "$*"
do
    echo $arg
done

echo '##############'
echo '"$@"结果:'
for arg in "$@"
do
    echo $arg
done


[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_3.sh a1 a2 a3
$*结果:
a1
a2
a3
##############
$@结果:
a1
a2
a3
##############
"$*"结果:
a1 a2 a3
##############
"$@"结果:
a1
a2
a3
```
