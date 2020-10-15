## xpath解析
* // :从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
* / : 匹配当前目录下的直接子节点。
* .. : 匹配当前节点的父节点。
* @：选取属性。
* //* : 选取文档中所有元素

```python
text = """
            <?xml version="1.0" encoding="UTF-8"?>
            <bookstore>
            <book>
              <title lang="eng">Harry Potter</title>
              <price>29.99</price>
            </book>
            <book>
              <title lang="cn">Learning XML</title>
              <price>39.95</price>
              <aa lang="cn eng aa bb" name="cc">Learning XML</aa>
            </book>
            </bookstore>
"""
from lxml import etree
html = etree.HTML(text)
# print(etree.tostring(html).decode('utf-8'))

# 选取所有指定的节点
res = html.xpath('//book')

# 获取指定节点的所有直接子节点
res = html.xpath('//book/aa')

# 获取指定节点的父节点
res = html.xpath("//aa/..")

# 通过属性匹配选择节点
res = html.xpath('//title[@lang="cn"]')

# 获取文本值
res = html.xpath('//title[@lang="cn"]/text()')
res = html.xpath('//price/text()')

# 获取属性值 ['eng', 'cn']
res = html.xpath('//title/@lang')

# 属性多值匹配
res = html.xpath('//aa[contains(@lang,"aa")]')
# 对于属性值有多个的节点，不用contains函数的话，匹配到的是空[]
res = html.xpath('//aa[@lang="aa"]')

# 文本匹配
res = html.xpath('//title[contains(text(), "XML")]')

# 运算符
res = html.xpath('//aa[contains(@lang,"aa") and @name="cc"]')
```
