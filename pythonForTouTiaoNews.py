from bs4 import BeautifulSoup
import requests
import json
import csv

# 获取爬取到的数据，并保存成csv格式文件
def get_data(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    content = json.loads(res.text)
    data = content['data']
    title = ''
    comment_count = ''
    article_url = ''
    keywords = ''

    for news in data:
        # print(news)
        content = []
        if 'extra' in news:
            if 'titles_terms' in news['extra']:
                title = news['extra']['titles_terms'].replace(' ', '')
        if 'comments_count' in news:
            comment_count = news['comments_count']
        if 'article_url' in news:
            article_url = news['article_url']
            # print('标题：',title,'  评论数:',comment_count,'   文章链接：',article_url)
        if 'keywords' in news:
            keywords = news['keywords']
        content = [title, article_url, keywords, str(comment_count)]
        # print(content)
        with open('toutiao_news.csv', 'a', newline='', encoding='utf-8') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(content)
            f.close()

pkeywords = '''阿里巴巴
人工智能
AI
腾讯
王者荣耀
小米
马云
雷军
无人汽车
机器人'''.split('\n')
print(pkeywords)

for keywords in pkeywords:
    for i in range(9):
        url = 'https://www.toutiao.com/search_content/?offset=' + str(
            i * 20) + '&format=json&keyword=' + keywords + '&autoload=true&count=20&cur_tab=1&from=search_tab'
        get_data(url)
