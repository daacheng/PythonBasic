# Python爬虫--scrapy爬虫框架入门
## 写在前面
之前写爬虫从来没用到过爬虫框架，其实之前写的都是学习爬虫写的小练手的demo，只能说是去网上抓取一点数据，直接一个python脚本解决完成爬虫所有的功能，利用for循环去抓取更多页面的数据。
后面学习到了代理池系统，稍微了解了一下爬虫其实是可以当做一个项目来看待，项目又是分模块的，不同的模块负责不同的功能，有的模块负责封装http请求，
有的模块负责处理请求（数据的抓取），有的模块负责数据的解析，有的模块负责数据的存储，这样一个框架的雏形就显现出来的，能够帮助我们更加专注和高效地进行数据的爬取。
对于scrapy，最开始并不想解释太多scrapy框架的各部分组成以及作用，直接在实际操作中去感受这个框架是如何分工合作的，每个模块负责什么样的功能，最后再去关注这个框架
的一些原理，应该是scrapy框架学习最好的方式了。
## scrapy爬虫的基本步骤
1. 创建一个scrapy爬虫项目。
2. 创建一个Spider爬虫类抓取网页内容并解析。
3. 定义数据模型（Item），将抓取到的数据封装到Item中。
4. 利用Item Pipeline存储抓取Item,即数据实体对象。
## 一、创建一个scrapy爬虫项目
安装好scrapy之后，运行命令**scrapy startproject 项目名**，就可以创建一个scrapy爬虫项目。
比如，运行 scrapy startproject test1,会生成一个test1的文件夹，目录结构如图：

![](https://github.com/daacheng/PythonBasic/blob/master/pic/scrapy1.png)
## 二、创建一个Spider爬虫类，抓取网页内容并解析。
爬虫的代码是写在spider文件夹下面的，所以在spider目录下创建一个python文件，这里爬取房天下的数据，所以创建个python文件就命名为ftx_spider.py.</br>
![](https://github.com/daacheng/PythonBasic/blob/master/pic/scrapy2.png)

接下来开始在ftx_spider.py中写爬虫代码：

        import scrapy    
        class FtxSpider(scrapy.Spider):
            """
            一、创建一个爬虫类，继承scrapy.Spider
            二、通过name属性，给爬虫类定义一个名称
            三、指定要抓取的网页链接urls，发送http请求
                方式一：
                    1.继承scrapy.Spider的start_requests()方法。
                    2.指定要爬取的url，通过scrapy.Request(url=url, callback=self.parse)发送请求，callback指定解析函数。
                方式二(简化)：
                    1.直接通过start_urls常量指定要爬取的urls。
                    2.框架会自动发送http请求，这里框架默认html解析函数parse().
            四、针对http请求的response结果，编写解析方法，parse()
            """

            name = 'ftx'

            # 方式一：通过scrapy.Request(url=url, callback=self.parse)发送请求，指定解析函数
            # def start_requests(self):
            #     urls = ['http://wuhan.esf.fang.com/house-a013126/i3']
            #     for url in urls:
            #         yield scrapy.Request(url=url, callback=self.parse)
            #
            # def parse(self, response):
            #     # 这里对抓取到的html页面进行解析
            #     print(response.url)

            # 方式二(简化版)：通过start_urls，框架自动发送请求，默认解析函数为parse()
            start_urls = ['http://wuhan.esf.fang.com/house-a013126/i3']

            def parse(self, response):
                print(response.url)

## 三、数据模型Item，定义爬取数据的数据结构
这个Item相当于java中的domain实体，或者说是javabean。在items.py中定义了一个类，继承scrapy.Item.这样我们就可以把我们抓取到的数据封装到一个对象中去。

    import scrapy

    class FtxSpiderItem(scrapy.Item):
        # define the fields for your item here like:
        title = scrapy.Field()  # 标题
        huxing = scrapy.Field()  # 户型
        size = scrapy.Field()  # 面积
        floor = scrapy.Field()  # 楼层
        fangxiang = scrapy.Field()  # 方向
        year = scrapy.Field()  # 建房时间
        shop_community = scrapy.Field()  # 小区
        address = scrapy.Field()  # 地址
        total_price = scrapy.Field()  # 总价（万）
        price = scrapy.Field()  # 单价（万/m2）

## 四、利用Item Pipeline存储抓取Item,将数据存入MongoDB
Item Pipeline为项目管道，当Item生成后，会自动被送到Item Pipeline进行处理。
#### 首先要在setting.py中添加MongoDB数据库连接信息
    # MongoDB
    HOST = 'localhost'
    PORT = 27017
    DB_NAME = 'ftx'
    COLL_NAME = 'roomprice'
#### 然后在pipelines.py中创建一个类，连接数据库，进行数据插入

    import pymongo
    from scrapy.conf import settings
    class FtxSpiderPipeline(object):

        def __init__(self):
            # 连接MongoDB
            self.client = pymongo.MongoClient(host=settings['HOST'], port=settings['PORT'])
            # 获取数据库
            self.db = self.client[settings['DB_NAME']]
            # 获取集合
            self.collection = self.db[settings['COLL_NAME']]

        def process_item(self, item, spider):
            self.collection.insert(dict(item))
#### 最后在setting.py中指定Item Pipeline用到的类，及优先级
    ITEM_PIPELINES = {
       'ftx_spider.pipelines.FtxSpiderPipeline': 300
    }
#### 运行命令行 scrapy crawl '爬虫名称name' ，就可以发现数据成功存入到数据库中了    

## [完整代码地址](https://github.com/daacheng/PythonBasic/tree/master/spider/ftx_spider)
https://github.com/daacheng/PythonBasic/tree/master/spider/ftx_spider
