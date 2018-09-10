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

## 代码

    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from bs4 import BeautifulSoup
    from pymongo import MongoClient
    import time

    """
        Python连接MongoDB数据库
    """
    client = MongoClient('localhost',27017)
    taobao = client.taobao
    collection_product = taobao.products


    """
        插入数据到MongoDB数据库
    """
    def save_product_to_mongodb(product):
        try:
            if collection_product.insert_one(product):
                print('记录成功！')
        except Exception:
            print('记录失败！')


    """
        创建浏览器对象，这里用的是谷歌浏览器无界面模式，不用每一次请求都弹出浏览器
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options = chrome_options)
    wait = WebDriverWait(browser, 15)

    # 要爬取的url
    url = 'https://s.taobao.com/search?q=' + '小米mix'

    products = []

    # 爬取前9页的内容
    for i in range(1,10):
        try:

            """
                这段功能主要是，操作浏览器去执行页面跳转功能
            """
            # 发起请求
            browser.get(url)
            # 等待页码输入框加载出来，获取页码输入框
            page_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.form .J_Input')))
            # 等待提交按钮加载出来，获取按钮
            page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.form .J_Submit')))
            # 清空页码输入框
            page_input.clear()
            # 输入指定要跳转的页数
            page_input.send_keys(str(i))
            # 点击确定，跳转
            page_button.click()

            """
                页面跳转之后，获取页面html资源，用BeautifulSoup去解析，获取相关的商品信息(商品价格，销量，名称，店名，地址)，存入数据库。
            """
            # 等待商品列表加载出来
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
            html = browser.page_source
            soup = BeautifulSoup(html,'html.parser')
            items = soup.select('.m-itemlist .items .item')
            for item in items:
                """
                    BeautifulSoup解析html，获取商品信息
                """
                price_list = item.select('strong')
                price = price_list[0].string if len(price_list)>0 else ''
                # 销量
                volume_list = item.select('.deal-cnt')
                sales_volume = volume_list[0].string if len(volume_list)>0 else ''
                # 商品标题
                title_list = item.select('.title .J_ClickStat')
                title = title_list[0].get_text().replace('\n','').replace(' ','') if len(title_list)>0 else ''
                # 店铺名称
                shop_name_list = item.select('.shop .shopname')
                shop_name = shop_name_list[0].get_text().replace('\n','').replace(' ','') if len(shop_name_list)>0 else ''
                # 地点
                location_list = item.select('.location')
                location = location_list[0].string if len(location_list)>0 else ''


                """
                    将爬取到的商品信息，用字典存储，然后存入MongoDB数据库
                """
                product = {
                    'price':price,
                    'sales_volume':sales_volume,
                    'title':title,
                    'shopname':shop_name,
                    'location':location
                }
                products.append(product)
                save_product_to_mongodb(product)
        except Exception:
            print('连接超时，停5秒！')
            time.sleep(5)

    print(products)
    # 关闭浏览器
    browser.close()

## 结果
![](https://github.com/daacheng/PythonBasic/blob/master/pic/taobaores1.png)

![](https://github.com/daacheng/PythonBasic/blob/master/pic/taobaores2.png)
