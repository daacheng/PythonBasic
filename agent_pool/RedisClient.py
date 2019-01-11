import random
import redis


REDIS_HOST = '127.0.0.1'
# REDIS_HOST = '132.232.146.31'
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
            # self.redisdb.zadd(REDIS_KEY, score, proxy)
            self.redisdb.zadd(REDIS_KEY, {proxy: score})

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
            # self.redisdb.zincrby(REDIS_KEY, proxy, -1)
            self.redisdb.zincrby(REDIS_KEY, -1, proxy)
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
        # self.redisdb.zadd(REDIS_KEY, MAX_SCORE, proxy)
        self.redisdb.zadd(REDIS_KEY, {proxy: MAX_SCORE})

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


