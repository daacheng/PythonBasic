给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
示例：
```python
输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```
#### 方法一：累计求和，时间复杂度O(n),空间复杂度O(n)
* 遍历数组，计算原数组nums在索引i位置的累计和，存到新数组中
* 遍历新数组，计算索引 i 和 i-k位置的最大差值。

```python
def findMaxAverage(nums, k):
    sum_list = []
    sum_ = 0
    for index, item in enumerate(nums):
        sum_ += item
        sum_list.append(sum_)

    max_ = float('-inf')
    for i in range(k-1, len(sum_list)):
        if i == k-1:
            value = sum_list[i]
        else:
            value = sum_list[i] - sum_list[i-k]
        max_ = max(max_, value)
    return max_/k
```
#### 方法二：滑动窗口
```python
[1,2,3,4,5,6,7]
# 前4位和是 1+2+3+4 = 10
# 滑动遍历
2+3+4+5 = 10+5-1 = 14
3+4+5+6 = 14+6-2 = 18
# 每次滑动计算子数组的和 sum = sum + nums[i] - nums[i-k]
```
代码
```python
def findMaxAverage(nums, k):
    sum_ = sum(nums[:k])
    max_ = sum_
    for i in range(k, len(nums)):
        sum_ = sum_ + nums[i] - nums[i-k]
        max_ = max(sum_, max_)
    return max_/k
```
