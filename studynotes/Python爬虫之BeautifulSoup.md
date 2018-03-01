## 一、创建BeautifulSoup对象

    from bs4 import BeautifulSoup
    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    soup = BeautifulSoup(html,'html.parser')
    print(soup.prettify())  #格式化html内容
    
**通过soup.prettify()可以使获取到的html文档格式化**
## 二、四大对象（Tag，NavigableString，BeautifulSoup，Comment）
### 1、Tag标签对象
利用soup加标签名的方式可以获取标签对象，它查找的是所有内容中第一个符合要求的标签。

    print(soup.head)
    #<head><title>The Dormouse's story</title></head>
    
Tag标签对象有两个重要属性，一个是name，一个是attrs。name是标签名，attrs是标签中的属性。

    print(soup.p.attrs)
    print(soup.p.name)
    #{'class': ['title'], 'name': 'dromouse'}
    #p
    
### 2、NavigableString
**通过soup.标签名.string就可以获取标签中的文字内容**

    print(soup.p.string)
    #The Dormouse's story
    
### 3、BeautifulSoup
BeautifulSoup可以看做是一个特殊的Tag

    print(soup.name) 
    # [document]
    print soup.attrs 
    #{} 空字典
    
### 4、Comment注释
Comment 对象是一个特殊类型的 NavigableString 对象.

    print(soup.a)
    print(soup.a.string)
    print(type(soup.a.string))
    #<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    #Elsie 
    #<class 'bs4.element.Comment'>
    
**a标签里的内容实际上是注释，但是如果我们利用.string 来输出它的内容，我们发现它已经把注释符号去掉了，所以，我们在使用前最好做一下判断是不是注释:**
 
    if type(soup.a.string)==bs4.element.Comment:
    
## 三、遍历文档树
### 1、获取子节点（.contents  .children属性）
tag的.content属性可以将tag的子节点以列表的方式返回，.children属性返回的是一个迭代器，这两个属性都是获取指定标签的**直接子节点**。

    print(soup.head.contents)
    #[<title>The Dormouse's story</title>]
    print(soup.head.children)
    #<listiterator object at 0x7f71457f5710>
    
### 2、所有子孙节点（.descendants属性）
.descendants属性可以对标签的子孙节点进行递归循环，返回的是一个生成器。

    print(soup.descendants)
    <generator object descendants at 0x00000202FB297A98>
    
### 3、节点内容（.string属性，不适用于具有多个子节点的标签）
如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个子标签了，那么 .string 也会返回最里面的内容。
如果tag包含了多个子节点,tag就无法确定，string 方法应该调用哪个子节点的内容, .string 的输出结果是 None。
### 4、多个内容（.strings  .stripped_strings 属性）
.strings  .stripped_strings 属性获取标签里面所有的文本内容，返回的是生成器，需要遍历获取。
输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容

    for s in soup.stripped_strings:
        print(s)
    The Dormouse's story
    The Dormouse's story
    Once upon a time there were three little sisters; and their names were
    ,
    Lacie
    and
    Tillie
    ;
    and they lived at the bottom of a well.
    ...

### 5、父节点（.parent）、全部父节点（.parents）

    content = soup.head.title.string
    for parent in  content.parents:
        print(parent.name)
        
### 6、兄弟节点（.next_sibling  .previous_sibling 属性）、全部兄弟节点（.next_siblings  .previous_siblings 属性）
### 7、前后节点（.next_element  .previous_element 属性）、所有前后节点（.next_elements  .previous_elements 属性）
## 四、搜索文档树
### 1、find_all( name , attrs , recursive , text , **kwargs ) 搜索当前Tag及其所有tag子节点,并判断是否符合过滤器的条件
**name参数可以是（字符串，正则表达式，列表，过滤器）**

    soup.find_all('b')
    soup.find_all(re.compile("^b"))
    soup.find_all(["a", "b"])
    
**keyword 参数（如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索）**

    soup.find_all(id='link2')
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
    soup.find_all(href=re.compile("elsie"))
    # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
    soup.find_all(href=re.compile("elsie"), id='link1')
    # [<a class="sister" href="http://example.com/elsie" id="link1">three</a>]
    
### 2、find()方法 
它与 find_all() 方法唯一的区别是 find_all() 方法的返回结果是值列表,而 find() 方法直接返回结果
## 五、css选择器（soup.select()）
### 1、通过标签名查找

    print(soup.select('title')) 
    #[<title>The Dormouse's story</title>]

### 2、通过类名查找

    print(soup.select('.sister'))
    #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

### 3、通过 id 名查找

    print(soup.select('#link1'))
    #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

### 4、组合查找

    print(soup.select('p #link1'))
    #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]

### 5.属性查找

    print(soup.select('a[href="http://example.com/elsie"]'))
    #[<a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>]



