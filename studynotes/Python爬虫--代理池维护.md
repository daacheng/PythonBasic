# Python爬虫--代理池维护
## 写在前面
以前爬取拉勾网数据的时候，爬了几十条数据之后就因为IP访问频繁而被封，那时候去网上查的可以使用代理IP，网上有很多免费的代理IP，稳定性虽然不高但是可用，用requests
发送请求时，只需要把代理IP以字典的形式传入参数即可，那时候使用代理，直接去网上复制粘贴的几个代理IP就拿来用了。

最近学习崔庆才老师的爬虫教程接触到了代理池系统，才认识到，对于一个高效的爬虫系统，直接利用数据结构封装一下网上复制粘贴的代理IP来进行爬虫真的是小打小闹，
构建一个高效的代理池系统也是爬虫工程的一部分。代理池系统主要实现：自动去网上获取代理，自动存储，自动检测，向爬虫提供获取接口。

大致思路：
1. 去代理网站上爬取大量代理IP，并将其存储在redis数据库。
2. 定时获取redis中的所有代理IP，检测每一个代理IP是否可用。
3. 通过flask，对外提供获取代理IP的接口，如果想要使用代理池中的代理IP，只需要访问我们提供的接口即可。

## 代理池系统具体实现思路
![](https://github.com/daacheng/PythonBasic/blob/master/pic/proxypool.png)
### 1、存储模块
存储模块：主要实现的功能是，去一些免费代理网站爬取大量的代理IP，并存储至redis数据库中。redis的Sorted Set结构是一个有序集合，我们会对每一个爬取到的代理IP
设置一个初始化的优先级10，Sorted Set也是通过这个优先级来进行排序的。</br>
该模块中主要写三个脚本：
1. Crawler.py: 爬取各代理网站中的代理IP的脚本。
2. RedisClient.py:自定义一个redis的客户端类，封装一些操作redis数据库的方法。比如添加、删除、查询等操作。
3. Getter.py: 主要是利用(或者说是调度)Crawler，RedisClient这两个对象，实现存储模块的功能（获取IP+存储）
#### Crawler.py

    import requests
    from pyquery import PyQuery as pq
    """
        爬取代理网站的免费代理并返回
    """


    class Crawler(object):

        def get_crawler_proxy(self):
            proxy_list = self.crawl_xici()
            return proxy_list

        def crawl_xici(self):
            """
                爬取西刺代理
            """
            proxy_list = []
            for i in range(1, 20):

                url = 'http://www.xicidaili.com/nn/' + str(i)

                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.xicidaili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                doc = pq(res.text)
                for odd in doc('.odd').items():
                    info_list = odd.find('td').text().split(' ')
                    if len(info_list) == 11:
                        proxy = info_list[5].lower().strip() + '://' + info_list[1].strip() + ':' + info_list[2].strip()
                        proxy_list.append(proxy)
            return proxy_list

#### RedisClient.py

    import random
    import redis


    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # redis的Sorted Set结构的key
    REDIS_KEY = 'proxies'
    # 初始化优先级的值为10
    INITAL_SCORE = 10
    # 优先级最小值
    MIN_SCORE =0
    # 优先级最大值
    MAX_SCORE = 100


    """
        利用redis的Sorted Set结构, 从redis中添加、查询、获取代理,以及修改代理的优先级
    """


    class RedisClient(object):

        def __init__(self, host=REDIS_HOST, port=REDIS_PORT):
            print('redis连接成功......')
            self.redisdb = redis.StrictRedis(host=host, port=port)

        def add(self, proxy, score=INITAL_SCORE):
            """
                添加代理,利用redis的Sorted Set结构存储
                zadd函数的三个参数：key是'proxies',按照score确定代理的优先级排序，value为代理proxy
                如果proxy已经存在redis中，就不添加; 新添加进来的代理proxy默认优先级为10
            """
            if not self.redisdb.zscore(REDIS_KEY, proxy):
                self.redisdb.zadd(REDIS_KEY, score, proxy)

        def get_proxy(self):
            """
                先获取优先级最高的代理，如果有，就从优先级最高的代理中挑一个，如果没有，就按优先级前十的proxy中随便选一个
            """
            # 返回key为REDIS_KEY的zset结构中score在给定区间(100,100)的元素
            res = self.redisdb.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
            if len(res):
                proxy = random.choice(res)
            else:
                if self.redisdb.zrevrange(REDIS_KEY, 0, 10):
                    proxy = random.choice(self.redisdb.zrevrange(REDIS_KEY, 0, 10))
                else:
                    raise Exception
            return proxy

        def decrease(self, proxy):
            """
                降低代理proxy的优先级score的值
                检测到代理proxy不可用是，就降低这个代理的优先级,优先级降低至0，就删除该代理proxy
            """
            score = self.redisdb.zscore(REDIS_KEY, proxy)
            if score and score > MIN_SCORE:
                self.redisdb.zincrby(REDIS_KEY, proxy, -1)
            else:
                self.redisdb.zrem(REDIS_KEY, proxy)

        def exist(self, proxy):
            """
                判断代理是否存在
            """
            score = self.redisdb.zscore(REDIS_KEY, proxy)
            if score:
                return True
            else:
                return False

        def max(self, proxy):
            """
                检测到代理可用，就将其优先级设置成最大100
            """
            self.redisdb.zadd(REDIS_KEY, MAX_SCORE, proxy)

        def get_proxy_count(self):
            """
                获取redis中代理数量
            """
            return self.redisdb.zcard(REDIS_KEY)

        def get_all_proxy(self):
            """
                获取全部代理proxy
            """
            return self.redisdb.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE)

#### Getter.py

    from Crawler import Crawler
    from RedisClient import RedisClient

    FULL_COUNT = 2000


    class Getter(object):

        def __init__(self):
            self.redis_client = RedisClient()
            self.crawler = Crawler()

        def is_full(self):
            """
                判断代理池是否满了
            """
            if self.redis_client.get_proxy_count() >= FULL_COUNT:
                return True
            else:
                return False

        def run(self):
            """
                将爬取到的代理存入redis
            """
            if not self.is_full():
                proxy_list = self.crawler.get_crawler_proxy()
                for proxy in proxy_list:
                    self.redis_client.add(proxy)

### 2、检测模块
检测模块：主要是针对爬取到的大量的代理IP，去检测这些代理IP是否可用，在存储模块中，初始抓取到的代理IP存储至redis的有序集合中，初始优先级为10，通过检测模块，
检测每一个代理IP，如果IP可用，及将其优先级设置为100，如果不可用，就将其优先级减1，如果优先级为0时，就将其从redis有序集合中删除。

检测模块利用的是异步http请求库aiohttp，其实用requests请求也是可以的，对于大量的代理IP检测，异步请求只需要将请求发送，不需要等待结果，效率会高一些。

Tester.py

    import RedisClient
    import asyncio
    import aiohttp
    import traceback
    import time

    """
        检测模块
    """

    # 用来测试代理是否可用的地址
    test_url = 'http://www.baidu.com'


    class Tester(object):

        def __init__(self):
            self.redisdb = RedisClient.RedisClient()

        """
            通过async关键字创建一个协程函数
        """
        async def test_proxy(self, proxy):
            """
                检测代理的可用性
            """
            # conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.ClientSession() as session:
                try:
                    if isinstance(proxy, bytes):
                        proxy = proxy.decode('utf-8')
                    print('正在检测 : %s' % proxy)
                    async with session.get(test_url, proxy=proxy, timeout=15) as res:
                        if res.status == 200:
                            # 说明代理可用,将其优先级置为最大
                            self.redisdb.max(proxy)
                            print('代理可用 : %s' % proxy)
                        else:
                            # 代理不可用，就降低其优先级
                            self.redisdb.decrease(proxy)
                            print('代理不可用 : %s' % proxy)
                except Exception as e:
                    self.redisdb.decrease(proxy)
                    print('代理不可用 : %s (%s)' % (proxy, e))

        def run(self):
            print('启动检测模块......')
            try:
                # 获取redis中所有爬取到的代理
                proxies = self.redisdb.get_all_proxy()
                loop = asyncio.get_event_loop()

                # 分批检测
                for i in range(0, len(proxies), 50):
                    test_proxies = proxies[i:i+50]
                    tasks = []
                    for test_proxy in test_proxies:
                        # 调用协程函数，返回协程对象
                        coroutine = self.test_proxy(test_proxy)
                        tasks.append(coroutine)
                    loop.run_until_complete(asyncio.wait(tasks))
                    time.sleep(5)
            except Exception as e:
                print('检测模块出错！！！')
### 3、通过flask向外提供获取代理IP的接口
通过flask可以很简单的创建一个web服务器，对外提供url接口，用户只需要请求指定的url，即可获取redis中的代理IP。

其实我们也可以直接在爬虫代码中连接redis获取优先级最高的代理IP拿来用，为什么要通过接口的形式去获取redis中的数据呢？这主要是一种设计思想吧，接口的方式
比较灵活，同时也能隐藏redis的连接信息，比较安全。

#### WebAPI_to_get_proxy.py

    from flask import Flask, g
    import RedisClient

    """
        对外提供web接口，通过提供的web接口，来获取redis中的代理
        g是上下文对象，处理请求时，用于临时存储的对象，每次请求都会重设这个变量。比如：我们可以获取一些临时请求的用户信息。
    """


    app = Flask(__name__)


    @app.route('/')
    def index():
        return '<h2>欢迎来到daacheng代理池系统</h2>'


    def get():
        if not hasattr(g, 'redis'):
            g.redis = RedisClient.RedisClient()
        return g.redis


    @app.route('/random')
    def get_random_proxy():
        # 从代理池中返回一个代理
        redisdb = get()
        return redisdb.get_proxy()


    @app.route('/count')
    def count():
        # 查询代理池中代理的个数
        redisdb = get()
        return str(redisdb.get_proxy_count())


    @app.route('/all')
    def get_all():
        # 查询代理池中代理的个数
        redisdb = get()
        return str(redisdb.get_all_proxy())


    if __name__ == '__main__':
        app.run()

## 4、调度模块
调度模块：主要是调度获取模块，和检测模块。启动两个进程，一个进程定时去爬取代理IP+存储，一个进程定时去检测获取到的代理IP是否可用。

controller.py

    from Getter import Getter
    from Tester import Tester
    import multiprocessing
    import time

    """
        调度模块
    """
    class Controller(object):

        """
            获取功能：爬取代理网站，将代理存储到redis
        """
        def control_get(self):
            getter = Getter()
            while True:
                getter.run()
                time.sleep(20)

        """
            检测功能，检测redis中的代理是否可用
        """
        def control_test(self):
            tester = Tester()
            while True:
                tester.run()
                time.sleep(20)

        def run(self):
            print('代理池开始运行了......')
            # 两个进程
            get = multiprocessing.Process(target=self.control_get)
            get.start()
            test = multiprocessing.Process(target=self.control_test)
            test.start()


    if __name__ == '__main__':
        control = Controller()
        control.run()



