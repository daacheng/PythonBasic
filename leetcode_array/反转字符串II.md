# 541.反转字符串II
## 题目
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
* 如果剩余字符少于 k 个，则将剩余字符全部反转。
* 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
```python
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

    2k = 4
    1. 拆分"abcd" "efg"
    2. 翻转"bacd" "feg"
    3. 还原"bacdfeg"
```

## 分析
与[反转字符串](反转字符串.md)原理一样，这里只是对不同的部位进行翻转操作。
* 把字符串按照2k的长度遍历
* 长度大于等于k就只对前k个字符进行翻转，长度小于k就全部翻转

```python
def reverseStr(s, k):
    def reverseS(ss):
        ss = list(ss)
        L = 0
        R = len(ss) - 1
        while L < R:
            ss[L], ss[R] = ss[R], ss[L]
            L += 1
            R -= 1
        return ''.join(ss)

    for i in range(0, len(s), 2*k):
        # 按照2k的长度遍历字符串
        s1 = s[i:i+2*k]
        if len(s1) < k:
            # 全部翻转
            s1 = reverseS(s1)
        else:
            # 只反转前k个
            s1 = reverseS(s1[:k]) + s1[k:]
        s = s[:i] + s1 + s[i+2*k:]
    return s
```

**其实分组后无论长度是多少，都是翻转前k个字符串**
```python
def reverseStr(s, k):
    def reverseS(ss):
        ss = list(ss)
        L = 0
        R = len(ss) - 1
        while L < R:
            ss[L], ss[R] = ss[R], ss[L]
            L += 1
            R -= 1
        return ''.join(ss)

    for i in range(0, len(s), 2*k):
        s1 = s[i:i+2*k]
        # 反转前k个字符
        s1 = reverseS(s1[:k]) + s1[k:]
        s = s[:i] + s1 + s[i+2*k:]
    return s
```
