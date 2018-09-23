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
