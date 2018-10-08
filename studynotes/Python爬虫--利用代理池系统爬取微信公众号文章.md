# Python爬虫--利用代理池系统爬取微信公众号文章
## 写在前面
之前通过学习崔庆才老师的爬虫教程，也试着动手做了一个代理池系统，通过不停地爬取代理网站上的代理IP，循环检测IP的可用性，存储有效代理IP到redis中。
[代理池系统维护](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E4%BB%A3%E7%90%86%E6%B1%A0%E7%BB%B4%E6%8A%A4.md)

这次主要是在前面的代理池系统的基础之上，利用已经构建好的代理池系统，通过从代理池系统中获取代理IP，来爬取微信公众号文章。
