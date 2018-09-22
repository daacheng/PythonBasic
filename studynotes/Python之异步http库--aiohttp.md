# Python之异步http库--aiohttp
官方文档解释： aiohttp是基于asyncio的一个异步http客户端和服务器
## 一、发送http请求

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
