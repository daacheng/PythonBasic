import requests
from bs4 import BeautifulSoup
import jieba
import pandas 
import re

commentlist=[]
for i in range(2):
    url='https://movie.douban.com/subject/26861685/comments?start='+str(i*20)+'&limit=20&sort=new_score&status=P&percent_type='
    res=requests.get(url)
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    for item in soup.select('.comment'):
        #print(item.p.text)
        commentlist.append(item.p.text)
#数据清洗  
commentStr=''
for c in commentlist:
    commentStr=commentStr+c.strip()
#print(commentStr)
#去除标点符号
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, commentStr)
cleaned_comments = ''.join(filterdata)
#print(cleaned_comments)

comment_=jieba.lcut(cleaned_comments)
words=pandas.DataFrame({'统计':comment_})
print(words)