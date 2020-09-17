## 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
```python
[
     [1],      0
    [1,1],     1
   [1,2,1],    2
  [1,3,3,1],   3
 [1,4,6,4,1]   4
]
```
示例：
```python
输入: 3
输出: [1,3,3,1]
```

代码：
```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            list_ = self.getRow(rowIndex-1)
            res = []
            for i in range(1, len(list_)):
                res.append(list_[i]+list_[i-1])
            res = [1] + res + [1]
            return res
```
