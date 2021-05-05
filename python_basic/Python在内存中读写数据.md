# Python在内存中读写数据
有时候数据不一定要读写到文件中，可以再内存中进行读写操作。

有些场景本地不保存数据，从远程读取文件数据到本地内存中进行处理后，再把数据流推送到远程，从头到尾本地并不生成文件。

**比如读取服务器一个加密文件数据流到内存中，在内存中进行解析处理，最终将解密后的数据流推送到服务器，中间不需要在本地保存加密文件，直接在内存中处理，减少了IO操作。**
## StringIO
```python
from io import StringIO

if __name__ == '__main__':
    s = StringIO()
    s.write('123\n')
    s.write('456\n')
    s.write('aaa\n')
    s.write('bbb')
    print(s)  # <_io.StringIO object at 0x0000022F7440F9D8>
    # 获取写入的内容
    print(s.getvalue())  # '123\n456\naaa\nbbb'
    # tell()方法返回文件指针当前位置
    print(s.tell())  # 15

    # seek(offset, whence)方法用于移动文件读取指针到指定位置
    # offset:代表需要移动偏移的字节数
    # whence:默认0，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    s.seek(0, 0)

    print(s.tell())  # 0
    print(s.readlines())  # ['123\n', '456\n', 'aaa\n', 'bbb']

    print(s.tell())  # 15
    print(s.readlines())  # []
```

## BytesIO
```python
from io import BytesIO

if __name__ == '__main__':
    f = BytesIO()

    fr = open('test.mp4', 'rb')
    f.write(fr.read())
    fr.close()

    # 对视频流解析处理

    with open('local_test.mp4', 'wb') as fw:
        fw.write(f.getvalue())
```
