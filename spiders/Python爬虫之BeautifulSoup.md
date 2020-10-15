#### 格式化输出
```python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister bro" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
```

#### find_all(name , attrs , recursive , string , **kwargs)
```python
# 查找所有的a标签
res = soup.find_all('a')
# # 查找所有的a标签和p标签
res = soup.find_all(['a', 'p'])

# 查找class=title的p标签
res = soup.find_all('p', 'title')

# 指定属性查找  可支持字符串，正则表达式，或者函数
# 指定id查找元素
res = soup.find_all(id="link1")
# 指定href查找 [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
res = soup.find_all(href=re.compile('elsie'))
# 指定多个属性查找
res = soup.find_all(id='link1', href=re.compile('elsie'))
# 指定多个属性查找 attrs参数
res = soup.find_all(attrs={'id': 'link1', 'href': re.compile('elsie')})

# 通过css搜索
res = soup.find_all(class_="sister bro")
# 通过函数过滤,查找类名长度大于6的元素
res = soup.find_all(class_=lambda x: x is not None and len(x) > 6)

# recursive参数，如果只想搜索直接子节点  recursive=False
res = soup.find_all('title', recursive=False)

# find_all() 方法的返回结果是值包含一个元素的列表
# 而find()方法直接返回第一个结果，没有则返回None.
res = soup.find('a')
```

#### CSS选择器
```python
# 类查找
res = soup.select('.sister')
# ID查找
res = soup.select('#link1')
res = soup.select('a#link1')
# 通过是否存在某个属性查找
res = soup.select('a[href]')
# 指定属性值查找
res = soup.select('a[href="http://example.com/tillie"]')

# 查找返回第一个元素
res = soup.select_one('a[href]')

# 获取元素的属性值
res = soup.select_one('a[href]').get('href')
# 获取元素的文本
res = soup.select_one('a[href]').text
```
