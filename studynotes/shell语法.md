# shell语法
## 一、变量
**变量名和等号之间不可以有空格**

    name="aaa"
    # 删除变量
    unset name

## 二、shell字符串
 
    youname="bbb"
    greet="hello ${youname}"
    echo $greet
    # 获取字符串长度
    echo ${#youname}
    # 截取字符串
    echo ${youname:1:4}
## 三、数组

    arr=(2 3 3 4 5)
    # 读取元素
    echo ${arr[0]}
    # 获取数组长度
    echo ${#arr[*]}
## 四、参数传递
**$n,n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推.**
* $# : 参数个数
* $* : 显示所有参数

    echo "执行的文件名 $0"
    echo "第一个参数 $1"
    echo "第二个参数 $2"
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shell1.png)
