给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
示例：

```python
输入: nums = [1,2,3,1], k = 3
输出: true

输入: nums = [1,0,1,1], k = 1
输出: true
```

利用哈希表：

```python
def containsNearbyDuplicate(nums, k):
    hash_ = {}
    for index, item in enumerate(nums):
        if item not in hash_:
            # 元素不存在，就保存元素及索引信息
            hash_[item] = index
        else:
            if index - hash_[item] <= k:
                # 遇到重复的且索引差满足条件直接返回True
                return True
            else:
                # 遇到重复的，但索引差不满足条件，更新索引
                hash_[item] = index
    return False
```
