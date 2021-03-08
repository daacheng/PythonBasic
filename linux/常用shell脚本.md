# 常用shell脚本
#### 获取项目所在目录
```python
getPath()
{
    this_dir=`pwd`
    dirname $0 | grep "^/" >/dev/null
    if [ $? -eq 0 ]; then
        this_dir=`dirname $0`
    else
        dirname $0 | grep "^\." >/dev/null
        retval=$?
        if [ $retval -eq 0 ]; then
            this_dir=`dirname $0 | sed "s#^.#$this_dir#"`
        else
            this_dir=`dirname $0 | sed "s#^#$this_dir/#"`
        fi
    fi
    echo `dirname $this_dir`
}

getPath
echo "$this_dir"

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
/root  # 项目所在目录
/root/bin  # 脚本所在目录
```

#### kill指定程序进程
```python
PIDS=`ps -ef | grep "程序名称" | grep -v "grep" | awk '{print $2}'`

for i in ${PIDS}
do
    echo "kill $i"
    kill -9 $i
done
```

#### 输出登录用户，当前时间
```python
#!/bin/bash

echo "logname:$LOGNAME"
dt=`date "+%Y-%m-%d %H:%M:%S"`
echo "当前时间:$dt"

[root@iZ8vb6ughzbdqkfd58dowoZ bin]# shell_1.sh
logname:root
当前时间:2021-03-08 16:14:52
```

#### 查看指定开头结尾的文件
```python
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# ls
2  hello.sh  shell_1.sh  shell_2.sh  shell.txt
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# ls | grep "^shell"
shell_1.sh
shell_2.sh
shell.txt
[root@iZ8vb6ughzbdqkfd58dowoZ bin]# ls | grep "sh$"
hello.sh
shell_1.sh
shell_2.sh
```
