# 347.前K个高频元素
## 题目
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
```python
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
```

## 分析
* 统计每个数字出现的次数
* 排序

```python
def topKFrequent(nums, k):
    times_dict = {}
    for num in nums:
        times_dict[num] = times_dict.get(num, 0) + 1

    res_list = sorted(times_dict.items(), key=lambda x:x[1], reverse=True)
    ans = []
    for i in range(0, k):
        ans.append(res_list[i][0])
    return ans
```
