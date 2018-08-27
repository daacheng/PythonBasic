# Python爬虫--猫眼电影top100基本信息
**简单的静态页面爬虫，利用requests,和BeautifulSoup库，只爬取了电影的基本信息，猫眼电影票房信息有点棘手，暂时先不爬**

    import requests
    from bs4 import BeautifulSoup
    import re
    import pandas
    from pandas import DataFrame

    movies =[]
    for i in range(10):
        num = str(i*10)
        url = 'http://maoyan.com/board/4?offset='+num 
        # 不加请求头，会被服务器识别为爬虫，禁止访问
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }

        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text,'html.parser')
        movies_info = soup.select('.board-wrapper dd')

        for info in movies_info:
            movies_dict = {}
            # 电影名称
            movie_name = info.select('.name')[0].string
            # 主演
            movie_star = info.select('.star')[0].string.replace(' ','').strip('\n')
            # 上映时间,通过正则表达式 提取 1993-01-01 时间
            movie_releasetime = info.select('.releasetime')[0].string.split('：')[1]
    #         releasetime = re.search(r'\d{4}-\d{2}-\d{2}',movie_releasetime).group()
            # 评分
            movie_score = info.select('.score .integer')[0].string + info.select('.score .fraction')[0].string
            # 电影Id，通过Id，进入电影详细页面，获取更多相关的信息
            movie_id = info.select('a')[0].attrs['data-val']
            m_id = re.search(r'\d+',movie_id).group()

            movie_detail_url = 'http://maoyan.com/films/'+m_id
            movies_dict['movie_name'] = movie_name
            movies_dict['movie_star'] = movie_star
            movies_dict['releasetime'] = movie_releasetime
            movies_dict['movie_score'] = movie_score
            movies_dict['movie_detail_url'] = movie_detail_url
            movies.append(movies_dict)

    df = DataFrame(movies)
    # 数据写成 csv文件
    df.to_csv('movies_maoyan.csv')
    df
    
![](https://github.com/daacheng/PythonBasic/blob/master/pic/maoyan.png) 
