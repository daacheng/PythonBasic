import requests
from bs4 import BeautifulSoup
import jieba
import pandas 
import re
import numpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
import warnings
warnings.filterwarnings("ignore")
%matplotlib inline
#%matplotlib inline是jupyter notebook里的命令, 意思是将那些用matplotlib绘制的图显示在页面里而不是弹出一个窗口
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
commentlist=[]
for i in range(10):
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

#分词
comment_=jieba.lcut(cleaned_comments)
words=pandas.DataFrame({'segment':comment_})
#print(words)
#读取停用词文件
stopwords=pandas.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
#print(stopwords)
#去除分词中所包含的停用词
words=words[~words.segment.isin(stopwords.stopword)]
#print(words)
#词频统计
words_stat=words.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)
#print(words_stat)

#用词云进行显示
wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
#for x in words_stat.head(1000).values:
    #print(x[0],":",x[1])

word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

frequencies = []
for key in word_frequence:
    temp = (key,word_frequence[key])
    frequencies.append(temp)


#print(word_frequence_list)
wordcloud=wordcloud.fit_words(dict(frequencies))
plt.imshow(wordcloud)