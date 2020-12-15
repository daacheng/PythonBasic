## 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#### 示例
```python
     3
    / \
   9  20
     /  \
    15   7

返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
```

#### 代码
与[二叉树的最大深度](二叉树的最大深度.md)做法相似，遍历二叉树

广度优先搜索：
* 队列存放当前层所有节点
* 每次拓展下一层的时候，需要将当前队列中所有节点都取出来进行拓展
* 保证每次拓展完时候，队列中存放的都是当前层的所有节点
* 用列表保存每层的元素值

```python
def levelOrderBottom(root):
    if not root:
        return []
    queue_ = Queue()
    queue_.put(root)
    result = []
    while queue_.qsize():
        size = queue_.qsize()
        vals = []  # 用列表保存每层的节点值
        for _ in range(size):
            node = queue_.get()
            vals.append(node.val)
            left = node.left
            right = node.right
            if left:
                queue_.put(left)
            if right:
                queue_.put(right)
        result.append(vals)
    result.reverse()
    return result
```
