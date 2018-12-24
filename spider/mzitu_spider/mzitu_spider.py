import asyncio
import aiohttp
import time
from bs4 import BeautifulSoup
import re


async def get_albums(session, url):
    '''请求入口页面，BeautifulSoup解析返回的HTTP响应，从中获取所有图集的URL
    :return:
        find_albums: 本次请求入口页面后，一共找到多个图集
        new_albums: 有多少个是新增的（即数据库之前没有记录的）
    '''
    find_albums = 0  # 一共找到多个图集
    new_albums = 0  # 有多少个是新增的（即数据库之前没有记录的）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    # 获取入口页面的HTTP响应
    try:
        timeout = aiohttp.ClientTimeout(total=60)
        async with session.get(url, headers=headers, timeout=timeout) as response:
            html = await response.text()
            # print(html)
    except Exception as e:  # 如果访问入口页面失败，则返回None以便于结束整个应用
        print(e)
        return
    # 使用lxml解析器，解析返回的响应（HTML文档）
    soup = BeautifulSoup(html, 'lxml')
    # 每个图集按年份/月份被放在 <div class='all'></div> 下面的每个<a href="图集URL">图集标题<a> 中
    a_tags = soup.find('div', {'class': 'all'}).find_all('a')  # <class 'bs4.element.ResultSet'>

    for a in a_tags:
        # 判断每个<a></a>标签中的URL是不是符合图集URL格式，如果不是，则递归调用它看看它下面有没有相同URL
        # 因为有一个 http://www.mzitu.com/old/
        if re.match(r'https://www.mzitu.com/\d+', a['href']):
            data = {
                'album_title': a.get_text(),  # 每个图集的标题
                'album_url': a['href'],  # 每个图集的URL
                'created_at': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),  # 何时添加到MongoDB的
                'visited': 0  # 表明此图集URL没被访问过
            }
            print(data)
    return find_albums, new_albums


async def step01():
    # 入口页面
    start_url = 'http://www.mzitu.com/all/'
    # 不能为每个请求创建一个seesion，减少开销
    async with aiohttp.ClientSession() as session:
        t1 = time.time()
        result = await get_albums(session, start_url)
        print(result)
        if not result:  # 如果访问入口页面失败，则结束整个应用
            return
        else:
            print('success')
    await session.close()






if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Step 01: 访问入口页面，将所有图集信息保存到MongoDB
    loop.run_until_complete(step01())

    loop.close()