# Python爬虫--顺企网企业信息爬取
## 写在前面
最近接触一个项目，需要大量的企业相关的数据，类似企业基本信息，工商信息，招聘信息，投资信息等。
顺企网是供企业发布产品供求信息的B2B电子商务平台，收录了342 个城市，92373445 家公司信息。

顺企网下有差不多80个公司行业分类（大类），80个大类下包含了差不多1800多个行业细分类别，每个细分类别下有最多40页的公司列表，每一页下有约40个公司链接。
顺企网没有什么特别的反爬措施，只有访问过频繁会封IP，比较简单，这里用之前搭建好的代理池系统就行（[代理池系统](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E4%BB%A3%E7%90%86%E6%B1%A0%E7%BB%B4%E6%8A%A4.md)），差不多1000个代理IP，我要做的是尽可能爬取网站所有的企业基本信息。

![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi1.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi2.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi3.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi4.png)

## 思路
#### crawl_company_urls.py
1. 从主页（http://b2b.11467.com/）获取80个行业大类的链接url，保存到main_category.csv.
2. 爬取80个公司行业分类(大类)下每个细分类型的url(共1868个),保存到detail_category.csv.
3. 每一个细分类型url下都有最多40页公司信息，爬取这40页的所有公司url,保存到company文件夹下，1800多个csv文件，每个文件名代表一个细分类型。(队列+多线程)
#### company_info_spider.py
1. 读取company文件夹下所有的csv文件路径到all_files_queue队列中。
2. 处理all_files_queue队列，从csv文件中获取公司URL，放到队列中(company_url_queue)
3. 从队列(company_url_queue)中取出公司URL,发送http请求，得到请求结果html,将html放到队列中（html_queue）
4. 从队列中取出请求结果html，进行解析，入库。

**三个队列，每个队列对应10个线程处理，最后速度还可以。用三个队列主要是把“url的获取”、“url的请求”、“url的解析”，全部分开处理，尽量减少因http请求引起的阻塞时间，每次请求最多等待3秒，请求失败会重新获取代理IP发送请求，同一个url最多请求5次，提高容错率，以及http请求效率**
