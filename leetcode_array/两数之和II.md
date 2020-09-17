## 两数之和II
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
示例：
```python
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```
#### 方法一：哈希表，时间复杂度O(n),空间复杂度O(n)
```python
def twoSum(numbers, target):
    num_dict = {}
    for i, item in enumerate(numbers):
        other = target - item
        if other not in num_dict:
            num_dict[item] = i
            continue
        else:
            return [num_dict[other]+1, i+1]
    return []
```

#### 方法二：利用两个指针，同时利用数组已经排序的这个特点
* 一个指针指向头部，一个指针指向尾部
* 如果和大于目标值，尾部的指针向前运动
* 如果和小于目标值，头部指针向后运动

```python
def twoSum(numbers, target):
    left_index = 0
    right_index = len(numbers)-1
    while left_index < right_index:
        if numbers[left_index] + numbers[right_index] > target:
            right_index -= 1
        elif numbers[left_index] + numbers[right_index] < target:
            left_index += 1
        else:
            return [left_index+1, right_index+1]
    return []
```
