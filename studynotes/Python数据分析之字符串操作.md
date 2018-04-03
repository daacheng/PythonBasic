# Python数据分析之字符串操作
## 字符串对象方法

        #字符串对象方法
        #split（），分割字符串，返回一个列表
        var = 'a,b  ,c  '.split(',')        #['a', 'b  ', 'c  ']
        #strip（）去除空白符   lstrip()   rstrip()
        pieces = [x.strip() for x in var]
        pieces                   #['a', 'b', 'c']

        #join()列表转换成字符串
        ''.join(pieces)             #'abc'

        #子串的定位find（）、index（）
        'abc'.find(':')      #find()方法，如果没有返回-1
        'abc'.find('a')      #find()方法如果有，返回索引
        'abc'.index('b')     #index()方法如果有返回索引，没有抛异常

        #count（）记录子串出现的次数
        'aaabc'.count('a')           #3

        #replace()替换
        'abcaddd'.replace('d','')             #'abca'
