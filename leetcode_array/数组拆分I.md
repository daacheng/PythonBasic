给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大。
示例：
```python
输入: [1,4,3,2]
输出: 4
解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
```
#### 方法一：排序 求和
```python
如果是min(a,b)总和最大，那排序后分组一定是相邻的两个一组。
大数跟大数分一起，小数跟小数分一起。
[1,2,3,4,5,6,7,8]
[(1,2),(3,4),(5,6),(7,8)]
```
代码
```python
def arrayPairSum(nums):
    nums.sort()
    sum_ = 0
    for i in range(0, len(nums), 2):
        sum_ += nums[i]
    return sum_
```
