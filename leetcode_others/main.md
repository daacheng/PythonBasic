## 牛客网刷题
### 1.字符串最后一个单词的长度
输入一行，代表要计算的字符串，非空，长度小于5000。
输出一个整数，表示输入字符串最后一个单词的长度。
```python
s_ = input()
last_word = s_.split(' ')[-1]
print(len(last_word))
```

### 2.计算某字母出现次数
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写。
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字母。
输出输入字符串中含有该字符的个数。
```python
s_ = input()
word_ = input().upper()
times = 0
for w in s_.upper():
    if w == word_:
        times += 1
print(times)
```

### 3.明明的随机数
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据(用于不同的调查)，希望大家能正确处理)。

第一组是3个数字，分别是：2，2，1。
第二组是11个数字，分别是：10，20，40，32，67，40，20，89，300，400，15。

**先输入N，再输入N个整数，然后对N个整数去重排序后输出**
```python
while True:
    try:
        N = int(input())
        input_set = set()
        for _ in range(N):
            random_ = int(input())
            input_set.add(random_)
        input_list = list(input_set)
        input_list.sort()
        for s in input_list:
            print(s)
    except:
        break
```

### 4.字符串分隔
* 连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
* 长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

```python
while True:
    try:
        s = input()
        for i in range(0, len(s), 8):
            s_sub = s[i:i+8]
            if len(s_sub) < 8:
                s_sub += '0' * (8-len(s_sub))
            print(s_sub)
    except:
        break
```

### 5.进制转换
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。输入一个十六进制的数值字符串。输出该数值的十进制字符串。
```python
while True:
    try:
        s_16 = input()
        print(eval(s_16))
    except:
        break
```

### 6.质数因子
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格
```python
def find(number):
    flag = True
    for i in range(2, int(number ** 0.5 + 2)):
        if number % i == 0:
            flag = False
            print(str(i), end=" ")
            find(int(number / i))
            break
    if flag:
        print(number, end=' ')


num = int(input())
find(num)
```

### 7.取近似值
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
```python
num = eval(input())
if num - int(num)>=0.5:
    print(int(num) + 1)
else:
    print(int(num))
```

### 8.合并表记录
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出合并后的键值对（多行）

```python
N = int(input())
dict_ = {}
for _ in range(N):
    k, v = input().split(' ')
    dict_[int(k)] = dict_.get(int(k), 0) + int(v)

for item in sorted(dict_):
    print('{} {}'.format(item, dict_[item]))
```

### 9.提取不重复的整数
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
```python
s = input()
ans = list()

for i in range(len(s)-1, -1, -1):
    if s[i] not in ans:
        ans.append(s[i])
print(''.join(ans))
```

### 10.字符个数统计
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串abaca而言，有a、b、c三种不同的字符，因此输出3。
```python
s = input()
ans = set()
for item in s:
    if ord(item) >= 0 and ord(item) <= 127:
        ans.add(item)
print(len(ans))
```
### 11.数字颠倒
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
```python
s = input()
ans = []
for i in range(len(s)-1, -1, -1):
    ans.append(s[i])
print(''.join(ans))
```

### 12.字符串反转
接受一个只包含小写字母的字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
```python
s = input()
ans = []
for i in range(len(s)-1, -1, -1):
    ans.append(s[i])
print(''.join(ans))
```

### 13.句子逆序
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
```python
s = input()
s = s.split(' ')
ans = []
for i in range(len(s)-1, -1, -1):
    ans.append(s[i])
print(' '.join(ans))
```

### 14.字符串排序
给定n个字符串，请对n个字符串按照字典序排列。

输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。

数据输出n行，输出结果为按照字典序排列的字符串。

```python
N = int(input())
ans = []
for i in range(N):
    s = input()
    ans.append(s)
ans.sort()
for item in ans:
    print(item)
```

### 15.二进制中1的个数
输入一个int型的正整数，计算出该int型数据在内存中(这个数转换成2进制后，输出1的个数)存储时1的个数。
```python
num = int(input())
s = str(bin(num))
times = 0
for i in range(2, len(s)):
    if s[i] == '1':
        times+=1
print(times)
```

### 16.购物单
### 17.坐标移动
### 18.识别有效的IP地址和掩码并进行分类统计
### 19.简单错误记录
### 20.密码验证合格程序
### 21.简单密码破解
密码是我们生活中非常重要的东东，我们的那么一点不能说的秘密就全靠它了。哇哈哈. 接下来渊子要在密码之上再加一套密码，虽然简单但也安全。

假设渊子原来一个BBS上的密码为zvbo9441987,为了方便记忆，他通过一种算法把这个密码变换成YUANzhi1987，这个密码是他的名字和出生年份，怎么忘都忘不了，而且可以明目张胆地放在显眼的地方而不被别人知道真正的密码。

他是这么变换的，大家都知道手机上的字母： 1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0,就这么简单，渊子把密码中出现的小写字母都变成对应的数字，数字和其他的符号都不做变换，

声明：密码中没有空格，而密码中出现的大写字母则变成小写之后往后移一位，如：X，先变成小写，再往后移一位，不就是y了嘛，简单吧。记住，z往后移是a哦。
```python
dict_ = {'1': '1', '0': '0', 'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4', 'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7', 't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}
ans = []
password = input()
for s in password:
    if s.isupper():
        # 大写转换为小写 向后推一位
        s = s.lower()
        if s == 'z':
            s = 'a'
        else:
            s = chr(ord(s) + 1)
        ans.append(s)
    elif s.islower():
        # 小写转换为数字
        s = dict_.get(s)
        ans.append(s)
    elif s.isdigit():
        # 数字不变
        ans.append(s)
print(''.join(ans))
```

### 22.汽水瓶
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？
```python
while True:
    try:
        nums = int(input())
        ans = 0
        while nums >= 3:
            m = nums % 3
            n = nums // 3
            ans += n
            nums = m + n
        if nums == 2:
            ans += 1
        if ans:
            print(ans)      
    except:
        break
```
### 23.删除字符串中出现最少的字符
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
```python
输入
abcdd
aabcddd

输出
dd
aaddd
```
**统计字符串中每个字符出现的次数，对字典进行value排序，确定要删除的字符**
```python
import sys
lines = sys.stdin.readlines()
for line in lines:
    line = line.replace('\n', '')
    s_count = {}
    for s in line:
        s_count[s] = s_count.get(s, 0) + 1

    l = sorted(s_count.items(), key=lambda x: x[1])
    min_ = l[0][1]
    for item in l:
        if min_ != item[1]:
            break
        line = line.replace(item[0], '')
    print(line)
```
### 24.合唱队
### 25.数据分类处理
### 26.字符串排序
### 27.查找兄弟单词
定义一个单词的“兄弟单词”为：交换该单词字母顺序，而不添加、删除、修改原有的字母就能生成的单词。
兄弟单词要求和原来的单词不同。例如：ab和ba是兄弟单词。ab和ab则不是兄弟单词。
现在给定你n个单词，另外再给你一个单词str，让你寻找str的兄弟单词里，字典序第k大的那个单词是什么？
注意：字典中可能有重复单词。本题含有多组输入数据。
```python
输入
3 abc bca cab abc 1
输出
2
bca
```

```python
line = input()
list_ = line.split(' ')
K = int(list_[-1])
s_ = list_[-2]

def is_brother(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2:
        return False
    s1_dict = {}
    for s in s1:
        s1_dict[s] = s1_dict.get(s, 0) + 1
    s2_dict = {}
    for s in s2:
        s2_dict[s] = s2_dict.get(s, 0) + 1
    if s1_dict == s2_dict:
        return True
    return False

ans = []
for word in list_[1:-2]:
    if is_brother(word, s_):
       ans.append(word)
ans.sort()
print(len(ans))

# 非常重要，注意审题
if len(ans) >= K:
    print(ans[K-1])
```

### 28.素数伴侣
### 29.字符串加密
1、对输入的字符串进行加解密，并输出。

2、加密方法为：

当内容是英文字母时则用该英文字母的后一个字母替换，同时字母变换大小写,如字母a时则替换为B；字母Z时则替换为a；

当内容是数字时则把该数字加1，如0替换1，1替换2，9替换0；

其他字符不做变化。

3、解密方法为加密的逆过程。

**注意奇数输入为加密，偶数输入为解密**
```python
def encode_s(s):
    ans = []
    for item in s:
        if item.isdigit():
           ans.append(str((int(item) + 1) % 10))
        elif item.isupper():
            if item == 'Z':
                ans.append('a')
            else:
                ans.append(chr(ord(item) + 1).lower())
        elif item.islower():
            if item == 'z':
                ans.append('A')
            else:
                ans.append(chr(ord(item) + 1).upper())
    return ''.join(ans)

def decode_s(s):
    ans = []
    for item in s:
        if item.isdigit():
            if item == '0':
                ans.append('9')
            else:
                ans.append(str(int(item) - 1))
        elif item.isupper():
            if item == 'A':
                ans.append('z')
            else:
                ans.append(chr(ord(item) - 1).lower())
        elif item.islower():
            if item == 'a':
                ans.append('Z')
            else:
                ans.append(chr(ord(item) - 1).upper())
    return ''.join(ans)

count = 0
while True:
    try:
        s = input()
        count += 1
        if count % 2 == 0:
            print(decode_s(s))
        else:
            print(encode_s(s))     
    except:
        break
```
