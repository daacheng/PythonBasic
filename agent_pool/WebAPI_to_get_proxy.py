from flask import Flask,g
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


if __name__ == '__main__':
    app.run()
