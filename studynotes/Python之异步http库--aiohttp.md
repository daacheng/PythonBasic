# Python之异步http库--aiohttp
官方文档解释： aiohttp是基于asyncio的一个异步http客户端和服务器
总结官方文档：https://aiohttp.readthedocs.io/en/stable/client_quickstart.html

这里主要介绍的是aiohttp客户端的操作
## 一、发送http请求
### get请求

    import aiohttp
    import asyncio

    """
        aiohttp:发送http请求
        1.创建一个ClientSession对象
        2.通过ClientSession对象去发送请求（get, post, delete等）
        3.await 异步等待返回结果
    """

    async def main():
        url = 'http://httpbin.org/get'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                print(res.status)
                print(await res.text())
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
### post请求

    import aiohttp
    import asyncio

    """
        aiohttp:发送POST请求
    """

    async def main():
        data = {'key1': 'value1', 'key2': 'value2'}
        url = 'http://httpbin.org/post'
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data) as res:
                print(res.status)
                print(await res.text())
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
## 二、传递参数

    import aiohttp
    import asyncio

    """
        aiohttp:传递参数
        方式一：通过字典的形式  params = {'key1': 'value1', 'key2': 'value2'}
        方式二：通过二元组的形式  params = [('key', 'value1'), ('key', 'value2')]

    """

    async def main():
        url = 'http://httpbin.org/get'
        params = {'key1': 'value1', 'key2': 'value2'}  
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as res:
                # http://httpbin.org/get?key1=value1&key2=value2
                print(res.url)
                print(await res.text())
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
## 三、状态码与响应内容

    import aiohttp
    import asyncio

    """
        aiohttp:相应内容与状态码
        状态码：res.status
        响应内容：res.text() 或者 res.text(encoding='utf-8')
        二进制内容：res.read()
        json响应内容：res.json()
        读取流：res.content.read(size)
    """

    async def main():
        url = 'https://api.github.com/events'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                print(res.status)
                print(await res.text())
                print('**********************************')
                print(await res.read())
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
## 四、流式响应内容（Streaming Response Content）

    import aiohttp
    import asyncio

    """
        res.content.read(size)
    """

    async def main():
        url = 'https://api.github.com/events'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as res:
                # <StreamReader 8202 bytes>
                print(res.content)
                print(await res.content.read())
                with open('test.txt', 'wb') as fd:
                    while True:
                        chunk = await res.content.read()
                        if not chunk:
                            break
                        fd.write(chunk)
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
## 五、超时设置

    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
