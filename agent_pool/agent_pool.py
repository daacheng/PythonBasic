from Crawler import Crawler
from RedisClient import RedisClient

FULL_COUNT = 2000


class Getter(object):
    def __init__(self):
        self.redis_client = RedisClient()
        self.crawler = Crawler()

    def is_full(self):
        # 判断代理池是否满了
        if self.redis_client.get_proxy_count() >= FULL_COUNT:
            return True
        else:
            return False

    def run(self):
        # 将爬取到的代理存入redis
        if not self.is_full():
            proxys = self.crawler.get_crawler_proxy()
            for proxy in proxys:
                self.redis_client.add(proxy)

