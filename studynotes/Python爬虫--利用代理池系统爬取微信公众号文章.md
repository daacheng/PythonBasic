# Python爬虫--利用代理池系统爬取微信公众号文章
## 写在前面
之前通过学习崔庆才老师的爬虫教程，也试着动手做了一个代理池系统，通过不停地爬取代理网站上的代理IP，循环检测IP的可用性，存储有效代理IP到redis中。
[代理池系统维护](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E4%BB%A3%E7%90%86%E6%B1%A0%E7%BB%B4%E6%8A%A4.md)

这次主要是在前面的代理池系统的基础之上，利用已经构建好的代理池系统，通过从代理池系统中获取代理IP，来爬取微信公众号文章。

## 一、整体思路
#### 构造请求对象WeixinRequests

![](https://github.com/daacheng/PythonBasic/blob/master/pic/weixinrequests.png)

#### 利用redis的List实现一个队列
![](https://github.com/daacheng/PythonBasic/blob/master/pic/redisqueue.png)

#### 爬虫流程



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

## 四、爬虫类
