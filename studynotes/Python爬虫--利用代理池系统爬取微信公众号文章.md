# Python爬虫--利用代理池系统爬取微信公众号文章
## 写在前面
之前通过学习崔庆才老师的爬虫教程，也试着动手做了一个代理池系统，通过不停地爬取代理网站上的代理IP，循环检测IP的可用性，存储有效代理IP到redis中。
[代理池系统维护](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E4%BB%A3%E7%90%86%E6%B1%A0%E7%BB%B4%E6%8A%A4.md)

这次主要是在前面的代理池系统的基础之上，利用已经构建好的代理池系统，通过从代理池系统中获取代理IP，来爬取微信公众号文章。涉及到一些面向对象的知识与思想，很受用，值得慢慢啃。

## 一、整体思路
#### 1.1 构造请求对象WeixinRequests

![](https://github.com/daacheng/PythonBasic/blob/master/pic/weixinrequests.png)
为什么要在Request请求对象基础上添加callback回调函数？

**不同的url请求，对应不同的返回结果。访问每一页的url，得到的是文章列表；访问文章链接url，得到的是文章的具体内容。所以，针对不同的请求返回的结果，需要用到不同的解析函数，这个解析函数，也就是我们为每个请求对象WeixinRequests额外添加的回调函数callback。**
#### 1.2 利用redis的List实现一个队列
![](https://github.com/daacheng/PythonBasic/blob/master/pic/redisqueue.png)

#### 爬虫流程
大致整体流程如下，具体实现看下面代码

![](https://github.com/daacheng/PythonBasic/blob/master/pic/weixinspider2.png)

## 二、Prepared Request
首先还是要回顾之前的requests库，除了直接通过requests.get(url)这种方式发送请求，还有另一种方式：

**构造requests.Request对象，将Request对象作为参数传入requests.Session()对象的prepare_request()方法中，最后通过Session对象的send()方法发送请求。**

这样做的好处是，每次请求都是一个Request对象，可以对这个请求对象进行封装，或者添加一些额外的功能。也方便我们把Request对象存储在队列中，我们只需要去从队列中获取请求对象，发送http请求即可。

    import requests
    from requests import Request
    url = 'http://httpbin.org/get'
    # 创建Session对象
    s = requests.Session()
    # 构造Request对象
    req = Request('GET',url)
    # 将Request对象转换成 PreparedRequest对象
    prepped = s.prepare_request(req)
    # 利用Session对象的send()方法，发送PreparedRequest对象
    res = s.send(prepped)
    print(res.text)

## 三、利用redis的List结构，实现一个队列RedisQueue。

    class RedisQueue(object):
        """
        构造一个队列，先进先出
        队列中存放的是序列化之后的WeixinRequests对象
        因为redis中存放的是字节
        """
        def __init__(self):
            self.redisdb = redis.StrictRedis(host=host, port=port)

        def add(self, weixin_requests):
            if isinstance(weixin_requests, WeixinRequests):
                return self.redisdb.rpush(redis_key, pickle.dumps(weixin_requests))
            return False

        def pop(self):
            """
                如果redis中不为空，就取出一个
            """
            if self.redisdb.llen(redis_key):
                return pickle.loads(self.redisdb.lpop(redis_key))
            else:
                return False

        def is_empty(self):
            return self.redisdb.llen(redis_key) == 0

## 四、爬虫代码
[微信公众号爬虫代码](https://github.com/daacheng/PythonBasic/tree/master/spider_weixin)

    from requests import Request
    import requests
    import redis
    import pickle
    from pyquery import PyQuery as pq
    from pymongo import MongoClient

    """
        Python连接MongoDB数据库
    """
    client = MongoClient('localhost', 27017)
    weixin = client.weixin
    collection_article = weixin.article


    class WeixinRequests(Request):
        """
            构造一个请求对象
        """

        def __init__(self,
                     method='GET', url=None, headers=None, files=None, data=None,
                     params=None, auth=None, cookies=None, hooks=None, json=None,
                     callback=None, need_proxy=False, failtime=0, timeout=10):
            Request.__init__(self, method, url, headers)
            self.callback = callback
            self.need_proxy = need_proxy
            self.failtime = failtime
            self.timeout = timeout


    host = '127.0.0.1'
    port = 6379
    redis_key = 'req'


    class RedisQueue(object):
        """
        利用构造一个队列，先进先出
        队列中存放的是序列化之后的WeixinRequests对象
        因为redis中存放的是字节
        """
        def __init__(self):
            self.redisdb = redis.StrictRedis(host=host, port=port)

        def add(self, weixin_requests):
            if isinstance(weixin_requests, WeixinRequests):
                return self.redisdb.rpush(redis_key, pickle.dumps(weixin_requests))
            return False

        def pop(self):
            """
                如果redis中不为空，就取出一个
            """
            if self.redisdb.llen(redis_key):
                return pickle.loads(self.redisdb.lpop(redis_key))
            else:
                return False

        def is_empty(self):
            return self.redisdb.llen(redis_key) == 0


    class SpiderWeixin(object):
        url = 'http://weixin.sogou.com/weixin'
        keyword = 'Python'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Cookie': 'SUV=006B71D77139A84A5B5AE571AD5DA453; CXID=C8E5DA6273C95D22410632D4243944C9; SUID=4AA839713965860A5B626D580005DFD1; ABTEST=6|1537866610|v1; SNUID=6183125A2C2E5D8255231EE62CBD0949; IPLOC=CN4201; JSESSIONID=aaa3dqRqYyG42bbIkHHvw',
            'Host': 'weixin.sogou.com'
        }
        session = requests.Session()
        queue = RedisQueue()

        def get_proxy(self):
            """
                根据之前代理池系统，对外提供的web访问接口，从代理池获取代理
            """
            try:
                get_proxy_utl = 'http://127.0.0.1:5000/random'
                res = requests.get(get_proxy_utl)
                if res.status_code == 200:
                    print('从代理池中获取代理IP: %s' % res.text)
                    return res.text
                else:
                    return None
            except Exception as e:
                print('从代理池中获取代理IP出错了！！ %s' % e)
                return None

        def parse_index(self, res):
            """
                解析每一页的所有的文章url链接
            """
            doc = pq(res.text)
            items = doc('.news-box .news-list li .txt-box h3 a').items()
            weixin_req_list = []
            for item in items:
                text_url = item.attr('href')
                weixin_req = WeixinRequests(url=text_url, callback=self.parse_detail, need_proxy=True)
                weixin_req_list.append(weixin_req)
            # 获取下一页的url
            next = doc('#sogou_next').attr('href')
            if next:
                next_url = self.url + str(next)
                print('下一页：', next_url)
                weixin_req = WeixinRequests(url=next_url, callback=self.parse_index, need_proxy=True, headers=self.headers)
                weixin_req_list.append(weixin_req)
            return weixin_req_list

        def start(self):
            """
                初始化操作
            """
            start_url = self.url + '?query=' + self.keyword + '&type=2'
            weixin_req = WeixinRequests(url=start_url, callback=self.parse_index, need_proxy=True, headers=self.headers)
            self.queue.add(weixin_req)

        def parse_detail(self, res):
            """
                解析详情页,获取每篇文章的详细信息
            """
            doc = pq(res.text)
            title = doc('.rich_media_title').text()
            content = doc('.rich_media_content').text()
            date = doc('#publish_time').text()
            author = doc('#js_name').text()
            data = {
                'title': title,
                'content': content,
                'date': date,
                'author': author
            }
            return data

        def excute_request(self, weixin_req):
            """
                执行请求
            """
            try:
                if weixin_req.need_proxy:
                    proxy = self.get_proxy()
                    if proxy:
                        proxies = {
                            'http': 'http://' + proxy
                        }
                        prepare = self.session.prepare_request(weixin_req)
                        res = self.session.send(prepare, proxies=proxies)
                        return res
                    return self.session.send(self.session.prepare_request(weixin_req))
            except Exception as e:
                print('执行请求出错了！！ %s' % e)
                return False

        def error(self, weixin_req):
            """
                当请求发生错误时，就记录一次错误，重新将请求放入对列，等待下次重新发起请求，错误次数达到一定次数，就不再加入对列
            """
            weixin_req.failtime = weixin_req.failtime + 1
            print('Request Failed(次数：%s, url: %s)' % (weixin_req.failtime, weixin_req.url))
            if weixin_req.failtime < 10:
                self.queue.add(weixin_req)

        def control(self):
            """

            """
            while not self.queue.is_empty():
                weixin_req = self.queue.pop()
                callback_func = weixin_req.callback
                res = self.excute_request(weixin_req)

                if res and res.status_code == 200:
                    results = callback_func(res)
                    if isinstance(results, dict):
                        collection_article.insert_one(results)
                        print('数据入库。。', results)
                    elif isinstance(results, list):
                        for result in results:
                            print('请求结果, ', result)
                            if isinstance(result, WeixinRequests):
                                self.queue.add(result)
                    else:
                        self.error(weixin_req)
                else:
                    self.error(weixin_req)

            print('请求队列空了！！')   

        def run(self):
            self.start()
            self.control()


    if __name__ == '__main__':
        spider = SpiderWeixin()
        spider.run()
