## utf8-BOM文件处理
#### 如果文件是utf8-BOM开头，会对文件转换造成影响，需要处理。
```python
import codecs  
# b'\xef\xbb\xbf'  
codecs.BOM_UTF8  
with open(dev_filepath, 'r+b') as f:  
    data = f.read()  
    if data[:3] == codecs.BOM_UTF8:  
        data = data[3:]  
        # seek()方法用于移动文件读取指针到指定位置  
        f.seek(0)  
        # truncate() 方法用于截断文件，  
        # 如果指定了可选参数size，则表示截断文件为size个字符。   
        # 如果没有指定 size，则从当前位置起截断
         # 截断之后 size 后面的所有字符被删除  
        f.truncate()  
        f.write(data) 
```
