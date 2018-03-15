from bs4 import BeautifulSoup
import requests
from pandas import DataFrame
import pandas
headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'www.lagou.com',
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
cookies={
    'Cookie':'user_trace_token=20171204223844-d432635e-d900-11e7-8374-525400f775ce; LGUID=20171204223844-d432666e-d900-11e7-8374-525400f775ce; _ga=GA1.2.898165162.1512398325; _gid=GA1.2.1123443679.1521029908; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; index_location_city=%E5%85%A8%E5%9B%BD; _putrc=885EA8E56D03CEEB; JSESSIONID=ABAAABAAAIAACBIF9289465F8AC96984F4016B2FB73CA3C; login=true; unick=%E5%8D%A2%E5%BF%97%E8%AF%9A; gate_login_token=ab1ae76c0baa54e418cb053fe63a144ad65d737916507a13; LGSID=20180315212655-87f3bc1d-2854-11e8-b1ed-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3DUTF-8%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; hideSliderBanner20180305WithTopBannerC=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521029909,1521029913,1521120422; TG-TRACK-CODE=index_search; SEARCH_ID=e305506bbf8c4a6798cf113c8d5a1075; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1521120453; LGRID=20180315212733-9e3cd161-2854-11e8-b1ed-5254005c3644'
}
data={
    'first':True,
    'pn':1,
    'kd':'python'
}
url="https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false&isSchoolJob=0"
res=requests.post(url,headers=headers,cookies=cookies,data=data)
res_json=res.json()
items=res_json['content']['positionResult']['result']
list_url=[]
list_fullname=[]
list_shortname=[]
list_companysize=[]
list_industryfield=[]
list_label=[]
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
df
