# Python读取大文本文件
* read():一次读取文件的全部内容，可以指定size去读取
* readline():每次读取一行
* readlines():一次读取所有内容并按行返回list

## 按行读取
```python
with open('test.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        print(line)
```

## 按块读取
```python
def read_file_chunked(fr, block_size=1024):
    while True:
        chunk = fr.read(block_size)
        if not chunk:
            break
        yield chunk


if __name__ == '__main__':
    with open('test.txt', 'r', encoding='utf-8') as fr:
        for chunk in read_file_chunked(fr):
            print(chunk)
```

或者
```python
from functools import partial
def read_file_chunked(fr, block_size=1024 * 8):
    # 首先使用 partial(fr.read, block_size) 构造一个新的无需参数的函数
    # 循环将不断返回 fr.read(block_size) 调用结果，直到其为 '' 时终止
    for chunk in iter(partial(fr.read, block_size), ''):
        yield chunk
```
