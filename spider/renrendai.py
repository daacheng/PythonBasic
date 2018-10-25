from selenium import webdriver
import time
import json
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options  #use headless browser login
import requests
from pandas import DataFrame
time_start = time.clock()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
#headers according to push F12 in browser
#enter the user information you have signed
username = u"1857"      #在此填入你的用户名
password = "b"     #在此填入你的密码
#driver = webdriver.Firefox()

#使用Firefox自带的无头浏览器登录
options = webdriver.ChromeOptions()
options.add_argument('-headless')
driver = webdriver.Chrome(chrome_options=options)  #use headless firefox to login

def LoginRRD(username, password):
    try:
        print(u'准备登录人人贷网站...')
        driver.get("https://www.we.com/pc/passport/index/login")
        elem_user = driver.find_element_by_name("j_username")
        elem_user.send_keys(username)
        time.sleep(2)  #设置等待时间，不用修改
        elem_pwd = driver.find_element_by_name("j_password")
        elem_pwd.send_keys(password)
        time.sleep(5)   #设置等待时间，以防止用户名下拉菜单挡住登录按钮
        driver.find_element_by_xpath(r"""//*[@id="form-login"]/div/div[2]""").click() #点击登录
        time.sleep(10) #设置等待几秒，以进入用户主界面，如不等待而直接进入爬虫会提示未登录
        print(u'登录成功！')
    except Exception as e:
        print("Error:", e)
    finally:
        print(u'End Login!\n')
loanid_e =[]
def parse_userinfo(loanid,idx):
    """用于提取借款人各项信息数据"""
    global loanid_e
#    print(str(loanid))
    urll="https://www.renrendai.com/loan-%s.html" % str(loanid)
    driver.get(urll)
    html = BeautifulSoup(driver.page_source,'lxml')

    info = html.findAll('div',class_="loan-user-info")   #这个地方的命名经常修改
    userinfo = {}
    try:
        items = info[0].findAll('span',{"class":"pr20"})
    except IndexError as e:
        LoginRRD(username, password)
        loanid_e.append(loanid)
    else:
        for item in items:
            var = item.get_text()
            value = item.parent.text.replace(var,"")
            userinfo[var]=value
        data = pd.DataFrame(userinfo,index=[idx])
        return data

def get_loanId():
    table=DataFrame(np.array(['allowAccess', 'amount', 'amountPerShare', 'beginBidTime', 'borrowerId',
                              'borrowerLevel', 'currentIsRepaid', 'displayLoanType', 'finishedRatio',
                              'forbidComment', 'interest', 'interestPerShare', 'leftMonths', 'loanId',
                              'loanType', 'months', 'nickName', 'oldLoan', 'openTime', 'overDued',
                              'picture', 'principal', 'productId', 'readyTime', 'repaidByGuarantor',
                              'startTime', 'status', 'surplusAmount', 'title', 'utmSource']).reshape(1,30),columns=['allowAccess',
        'amount', 'amountPerShare', 'beginBidTime', 'borrowerId',
        'borrowerLevel', 'currentIsRepaid', 'displayLoanType', 'finishedRatio',
        'forbidComment', 'interest', 'interestPerShare', 'leftMonths', 'loanId',
        'loanType', 'months', 'nickName', 'oldLoan', 'openTime', 'overDued',
        'picture', 'principal', 'productId', 'readyTime', 'repaidByGuarantor',
        'startTime', 'status', 'surplusAmount', 'title', 'utmSource'])#网页源码获取
    i=1
    for i in range(1,101):    #当前101散标信息页面一共只有101页，所以填的是101，可根据具体情况修改
        url = "https://www.renrendai.com/loan/list/loanList?startNum=%s&limit=10"%str(i) #resourse of data
        resp=requests.get(url,headers=headers)    #获取页面源代码
        html=resp.text
        data_dic = json.loads(html)
        data=DataFrame(data_dic['data']['list'])
        table=pd.concat([table,data])
        i += 1
    #save file
    table.to_csv('人人贷11.csv',header=False) #保存贷款人信息到人人贷.csv文件夹中
    loanId=table['loanId']
    return loanId


if __name__ == '__main__':
    LoginRRD(username, password)   #login renrendai website
    loanId = get_loanId()     #获取借款人ID
    # user_info = ['昵称', '信用评级','姓名','身份证号','年龄', '学历', '婚姻','申请借款', '信用额度',
    #              '逾期金额', '成功借款', '借款总额', '逾期次数','还清笔数', '待还本息',
    #              '严重逾期','收入', '房产', '房贷', '车产', '车贷','其他','公司行业',
    #              '公司规模', '岗位职位', '工作城市', '工作时间']
    # table2 = pd.DataFrame(np.array(user_info).reshape(1, 27), columns=user_info)


    # i = 1
    # idx = 0
    # for loanid in loanId[1:10]:
    #     """
    #     后面的数值用来设置需要爬取多少个借款人信息，如全部需要就输入len(loanId +1)替代1000，
    #     建议先输入5来进行爬虫测试，以避免爬虫时间太长，而实际没有抓取到数据
    #     """
    #     table2 = pd.concat([table2, parse_userinfo(loanid,idx)])
    # #    print(loanid)
    #     print(i)
    #     idx += 1
    #     i += 1   #check how many times of this program loop
    #
    # table2.to_csv('borrowerinfo1.csv',header=False)
    #
    # time_end = time.clock()  #this scarpy use of total time
    # print("\nElapsed time: %s seconds"%(str(time_end -time_start)))
