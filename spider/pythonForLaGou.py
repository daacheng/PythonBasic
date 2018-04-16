from bs4 import BeautifulSoup
import requests
from pandas import DataFrame
import pandas
import time
from random import randint
from fake_useragent import UserAgent
ua = UserAgent()
#UserAgent存放list，用于随机使用UserAgent
list_userAgent=[ua.google,ua.chrome,ua.msie,ua.firefox,ua.ie]

proxies=[{},{'http':'http://110.73.8.39:8123'},{'http':'http://182.114.245.108:8118'},{'http':'http://61.135.217.7:80'},{'http':'http://182.90.95.206:8123'},{'http':'http://115.46.96.47:8123'}]
cookies={
    'Cookie':'_ga=GA1.2.1413047706.1520953710; user_trace_token=20180313230829-62fea120-26d0-11e8-b1e3-5254005c3644; LGUID=20180313230829-62fea687-26d0-11e8-b1e3-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; WEBTJ-ID=20180321132726-1624706bb64413-0b0ed73765b2d6-3c604504-1049088-1624706bb6541e; _gid=GA1.2.688187489.1521610047; X_HTTP_TOKEN=27a5fd2cb6628e574e166861f7dade83; _putrc=885EA8E56D03CEEB; JSESSIONID=ABAAABAABEEAAJA936A7AEF45B03719456B98C390C98E38; login=true; unick=%E5%8D%A2%E5%BF%97%E8%AF%9A; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; hideSliderBanner20180305WithTopBannerC=1; TG-TRACK-CODE=index_search; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521442326,1521610047,1521610834,1521613002; LGSID=20180321141642-6c387727-2ccf-11e8-b566-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; gate_login_token=2d17ce4f70ab6a072ad4e7a8910160441bda7998e7295e58; SEARCH_ID=12f43395ffde4b10b10d69b8fa28ca2b; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521613017; LGRID=20180321141657-754ac93c-2ccf-11e8-b566-5254005c3644'
}
list_url=[]
list_fullname=[]
list_shortname=[]
list_companysize=[]
list_industryfield=[]
list_label=[]

for i in range(1,6): 
    headers={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent':list_userAgent[randint(0,4)]
    }
    data={
        'first':True,
        'pn':i,
        'kd':'python'
    }
    time.sleep(20)
    url="https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false&isSchoolJob=0"
    res=requests.post(url,headers=headers,cookies=cookies,data=data,proxies=proxies[i])
    res_json=res.json()
    print(res_json)
    items=res_json['content']['positionResult']['result']
    
    for item in items:
        companyFullName = item['companyFullName']       #公司全名
        companyShortName = item['companyShortName']     #公司简称
        companySize = item['companySize']               #公司规模
        industryField = item['industryField']           #行业领域
        companyLabel = ''.join(item['companyLabelList'])#公司标签
        url = "https://www.lagou.com/jobs/"+str(item['positionId'])+".html"
        list_fullname.append(companyFullName)
        list_shortname.append(companyShortName)
        list_companysize.append(companySize)
        list_industryfield.append(industryField)
        list_label.append(companyLabel)
        list_url.append(url)
companyInfo={
    '公司全称':list_fullname,
    '公司简称':list_shortname,
    '公司规模':list_companysize,
    '行业领域':list_industryfield,
    '公司标签':list_label,
    '链接':list_url
}
df = DataFrame(companyInfo)
#df.to_csv('拉勾.csv',index=False)
df
