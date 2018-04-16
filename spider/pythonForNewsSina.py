import requests
import json
import pandas
from datetime import datetime
from bs4 import BeautifulSoup
url='http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1511263184507'
commentUrl='http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1511189047225_94708810'
def getCommentCount(url):
    newsid=url.split('/')[-1].lstrip('doc-i').rstrip('.shtml')
    jd=json.loads(requests.get(commentUrl.format(newsid)).text.lstrip('var loader_1511189047225_94708810='))
    return jd['result']['count']['total']
#获取新闻所有信息方法封装
def getNewsDetails(url):
    result={}
    res=requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    #标题
    result['title']=soup.select('#artibodyTitle')[0].text
    timesource=soup.select('.time-source')[0].contents[0].strip()
    #日期 字符串转时间strptime 时间转字符串strftime
    result['dt']=datetime.strptime(timesource,'%Y年%m月%d日%H:%M').strftime('%Y-%m-%d')
    #来源
    result['source']=soup.select('.time-source span a')[0].text
    #正文
    article=[]
    for p in soup.select('.article p')[:-1]:
        article.append(p.text.strip())
        txt=''.join(article)
    result['txt']=txt
    #编辑人
    result['editor']=soup.select('.article-editor')[0].text.lstrip('责任编辑：')
    result['comments']=getCommentCount(url)
    return result
#获取每个分页下的所有新闻链接item['url'],获取每个连接下的明细
def parseListUrl(url):
    newsdetails=[]
    res=requests.get(url)
    jd=json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
    for item in jd['result']['data']:
        newsdetails.append(getNewsDetails(item['url']))
    return newsdetails
#爬取前三页的所有新闻明细
news_total=[]
for i in range(1,2):
    newsurl=url.format(i)
    newsary=parseListUrl(newsurl)
    news_total.extend(newsary)
df=pandas.DataFrame(news_total)
df.head(15)