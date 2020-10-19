from Crawler import Crawler
from RedisClient import RedisClient
import traceback
import time
import requests
import multiprocessing
from concurrent import futures

FULL_COUNT = 2000


class Getter(object):
    # 爬取代理网站的免费代理IP，存入redis
    def __init__(self):
        self.redis_client = RedisClient()
        self.crawler = Crawler()

    def is_full(self):
        # 判断代理池是否满了
        return self.redis_client.get_proxy_count() >= FULL_COUNT

    def run(self):
        # 将爬取到的代理存入redis
        if not self.is_full():
            proxys = self.crawler.get_crawler_proxy()
            for proxy in proxys:
                self.redis_client.add(proxy)


class Tester(object):
    """
        从redis中取出代理，测试代理是否可用，并调整代理IP的优先级
    """
    def __init__(self, test_url):
        self.redisdb = RedisClient()
        # 用来测试代理是否可用的地址
        self.test_url = test_url

    def test_proxy(self, proxy):
        try:
            if isinstance(proxy, bytes):
                proxy = proxy.decode('utf-8')
            proxies = {
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }
            print('正在检测:{}'.format(proxy))
            res = requests.get(self.test_url, proxies=proxies, timeout=10)
            if res.status_code == 200:
                return True, proxy
            else:
                return False, proxy
                # 代理不可用，就降低其优先级
        except Exception as e:
            return False, proxy
            # print('代理检测异常:{}  {}'.format(proxy, e))
            self.redisdb.decrease(proxy)
            print('代理不可用:{}'.format(proxy))


    def run(self):
        print('启动检测模块......')
        try:
            # 获取redis中所有爬取到的代理
            proxies = self.redisdb.get_all_proxy()
            for i in range(0, len(proxies), 50):
                test_proxies = proxies[i:i+50]
                workers = len(test_proxies)
                with futures.ThreadPoolExecutor(workers) as executor:
                    tasks_res = executor.map(self.test_proxy, test_proxies)
                    for res, proxy in tasks_res:
                        if not res:
                            # 代理不可用，就降低其优先级
                            self.redisdb.decrease(proxy)
                            print('代理不可用:{}'.format(proxy))
                        else:
                            # 代理可用,将其优先级置为最大
                            self.redisdb.max(proxy)
                            print('代理可用:{}'.format(proxy))

        except Exception as e:
            print(traceback.format_exc())
            print('检测模块出错！！！')


class Controller(object):
    def control_get(self):
        # 获取功能：爬取代理网站，将代理存储到redis
        getter = Getter()
        while True:
            try:
                getter.run()
            except:
                print(traceback.format_exc())
            time.sleep(30)

    def control_test(self):
        # 检测功能，检测redis中的代理是否可用
        tester = Tester(test_url='http://www.baidu.com')
        while True:
            try:
                tester.run()
            except:
                print(traceback.format_exc())
            time.sleep(30)

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

