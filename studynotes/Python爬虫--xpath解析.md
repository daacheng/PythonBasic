# Python爬虫--xpath解析
XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。
## xpath常用规则
* nodename  节点名称
* /   从当前节点选取直接子节点
* //   从当前节点选取子孙节点
* .    选取当前节点
* ..   选取当前节点的父节点
* @    属性匹配

## Python中利用xpath语法来解析html文档

    from lxml import etree

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

    html = etree.HTML(text)
    print(etree.tostring(html).decode('utf-8'))

    # 选取所有节点
    """
    [<Element html at 0x268b5b36608>,
     <Element body at 0x268b5b3dd08>,
     <Element bookstore at 0x268b5b36e88>,
     <Element book at 0x268b5b36c88>,
     <Element title at 0x268b5b454c8>,
     <Element price at 0x268b5b45d88>,
     <Element book at 0x268b5b45dc8>,
     <Element title at 0x268b5b45e08>,
     <Element price at 0x268b5b45e48>]
    """
    html.xpath('//*')

    # 选取所有指定的节点
    # [<Element book at 0x268b5b3d848>, <Element book at 0x268b5b3d948>]
    html.xpath('//book')

    # 获取指定节点的所有直接子节点
    html.xpath('//book/title')

    # 获取指定节点的父节点  # [<Element book at 0x268b5bed448>, <Element book at 0x268b5bf1dc8>]
    html.xpath("//title/..")

    # 通过属性匹配选择节点  [<Element title at 0x268b5b10688>]
    html.xpath('//title[@lang="cn"]')

    # 获取文本
    html.xpath('//title[@lang="cn"]/text()')
    html.xpath('//price/text()')

    # 获取属性值 ['eng', 'cn']
    html.xpath('//title/@lang')

    # 属性多值匹配  [<Element aa at 0x268b5ba1fc8>]
    html.xpath('//aa[contains(@lang,aa)]')
    html.xpath('//aa[contains(@lang,bb)]')

    # 对于属性值有多个的节点，不用contains函数的话，匹配到的是空[]
    html.xpath('//aa[@lang="aa"]')

    # 运算符  [<Element aa at 0x268b5c81dc8>]
    html.xpath('//aa[contains(@lang,"aa") and @name="cc"]')
