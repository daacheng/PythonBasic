给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j), 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k。
示例：
```python
输入: [3, 1, 4, 1, 5], k = 2
输出: 2
数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个 1，但我们只应返回不同的数对的数量。
```
方法：
1. 遍历数组，两个集合，一个集合(diff)保存diff对中最小的元素，一个集合(saw)保存已经遍历过的元素。
2. 如果x-k in saw,保存x-k到diff中。
3. 如果x+k in saw,保存x到diff中。
4. 返回diff的长度.
```python
def findPairs(nums, k):
    if k < 0:
        return 0
    diff = set()
    saw = set()
    for item in nums:
        if (item-k) in saw:
            diff.add(item-k)
        if (item+k) in saw:
            diff.add(item)
        saw.add(item)
    return len(diff)
```
