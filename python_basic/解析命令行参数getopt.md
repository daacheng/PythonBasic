## 解析命令行参数(getopt)
```python
import getopt  
import sys  
print(sys.argv[1:])  # ['-h', '-t', 'bb', '-i', 'cc']  
opts, args = getopt.getopt(sys.argv[1:], 'i:o:e:c:f:t:h', ['check','output='])  
print(opts)  
print(args)  

# getopt中需要三个参数  
# 1、使用sys.argv[1:]过滤掉第一个参数（执行的脚本的名字，这个不需要）  
# 2、短格式分析串：'i:o:e:c:fh' 分别代表 -i -o -e -c -f 命令。后面有":"表示需要带参数。  
# 3、长格式分析串列表： ['check','output='] 表示 "help"命令 和 "output"命令，"="表示需要带参数。  
# 函数返回两个列表  opts, args     
# args为不属于格式信息的剩余的命令行参数,即不是按照getopt()里面定义的长或短选项字符和附加参数以外的信息。  
# 例如： 运行命令     python .\test.py -h  -t bb -i cc  
# opts = [('-h', ''), ('-t', 'bb'), ('-i', 'cc')]  
# args = []  

```
