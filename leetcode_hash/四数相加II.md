# 454.四数相加II
## 题目
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
```python
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
输出:
2
解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

## 分析
* 与[两数之和](两数之和.md)有点相似,将四个数组分成两组，AB一组，CD一组
* 对于A和B，使用二重循环对它们进行遍历，得到所有A[i]+B[j]的值并存入哈希映射中。每个键表示一种A[i]+B[j]，对应的值为 A[i]+B[j]出现的次数。
* 对于C和D，同样使用二重循环对它们进行遍历。当遍历到C[k]+D[l] 时，如果-(C[k]+D[l])出现在哈希映射中，那么将 -(C[k]+D[l])对应的值累加进答案中。
* 时间复杂度O(n^2), 空间复杂度O(n^2)

```python
def fourSumCount(A, B, C, D):
    # 记录AB两个数组元素两两相加之和及其次数
    hash_1 = dict()
    for index_1, item_1 in enumerate(A):
        for index_2, item_2 in enumerate(B):
            sum_ = item_1 + item_2
            hash_1[sum_] = hash_1.get(sum_, 0) + 1

    ans = 0
    for index_1, item_1 in enumerate(C):
        for index_2, item_2 in enumerate(D):
            sum_ = item_1 + item_2
            if 0-sum_ in hash_1:
                ans += hash_1[0-sum_]

    return ans
```
