# Python爬虫--selenium爬取淘宝商品信息
## 写在前面
最近几天在看崔庆才老师的selenium教程，selenium是一个自动化测试工具，它可以模拟人去操作浏览器，让浏览器执行特定的动作，比如查询，下拉，页面跳转等。
在做爬虫的时候，很容易碰到网页是通过JavaScript渲染生成的，我们通过requests请求一个url，返回的结果会是一大段js代码，而不是真正页面显示的内容。
这时候通过selenium去模拟浏览器执行url请求，获取到的网页资源便是页面真实显示的html资源，然后通过解析库去解析这些html便可以得到我们想要的页面显示的数据了。

了解selenium一些基础操作之后，跟着教程试着做一下淘宝商品的爬取。这里主要用到的selenium相关的操作有：
* selenium创建浏览器对象。
* selenium节点查找，主要是通过By.CSS_SELECTOR,css选择器去查找。
* 显式等待，利用selenium的WebDriverWait对象，以及相关的等待条件，比如 等待指定节点加载出来：presence_of_element_located();等待按钮可点击：element_to_be_clickable()。
* selenium节点交互，清空input输入框，input输入框传值，点击按钮。

除了用selenium去模拟操作浏览器，获取页面HTML资源之外，HTML解析库用的是BeautifulSoup,主要是对这个解析库稍微熟悉一点。

[selenium基础操作文档](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--selenium%E5%9F%BA%E7%A1%80%E6%93%8D%E4%BD%9C.md)

[BeautifulSoup基础操作文档](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB%E4%B9%8BBeautifulSoup.md)
