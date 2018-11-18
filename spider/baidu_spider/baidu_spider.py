import requests
import json
from bs4 import BeautifulSoup
import re
import urllib
import datetime
import random
import csv
import time
from pymongo import MongoClient
from fake_useragent import UserAgent


"""
    数据库操作
"""
client = MongoClient('localhost', 27017)
baidu = client.baidu
collection = baidu.work_1117


def save_to_mongodb(work_info):
    try:
        if collection.insert_one(work_info):
            print('记录成功！')
    except Exception:
        print('记录失败！')

##########################################################


def get_proxy():
    """
        根据之前代理池系统，对外提供的web访问接口，从代理池获取代理
    """
    try:
        get_proxy_utl = 'http://127.0.0.1:5000/random'
        res = requests.get(get_proxy_utl)
        if res.status_code == 200:
            print('从代理池中获取代理IP: %s' % res.text)
            proxies = {'http': 'http://' + res.text}
            return proxies
        else:
            return None
    except Exception as e:
        print('从代理池中获取代理IP出错了！！ %s' % e)
        return None

##########################################################


"""
    读取文件信息info.csv(查询条件)
"""
info_list = []
with open('info.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        # print(row)
        info_list.append(row)
        # print(info_list)

###########################################################
"""
    初始化变量
"""
job_type_list = []
ua = UserAgent()


def crawl(job_type, city, province, token):
    headers = {
        'Accept': '*/*',
        'Cookie': 'BAIDUID=2176D64D05517AC3780B774A47F39EB6:FG=1; BIDUPSID=2176D64D05517AC3780B774A47F39EB6; PSTM=1539070163; BDUSS=1lsMWZKSFRUWjBzTDU0TjNJMWxCdnJmc0tOTUR4N2E2MDNxeGdINmZxSk5LdlZiQVFBQUFBJCQAAAAAAAAAAAEAAADi6c1PYmJveb-nt8jX0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2dzVtNnc1bb; MCITY=-218%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; H_PS_PSSID=26522_1446_21094_27400; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1541989917,1542350086; Hm_lpvt_da3258e243c3132f66f0f3c247b48473=1542350420',
        'Referer': 'https://zhaopin.baidu.com/',
        'User-Agent': ua.random
    }

    pn = 0
    for i in range(10):

        try:
            url = 'https://zhaopin.baidu.com/api/qzasync?query=%s&city=%s&is_adq=1&pcmod=1&token=%s&pn=%d&rn=10' % (
            urllib.parse.quote(job_type), urllib.parse.quote(city), token, pn)
            # url = 'https://zhaopin.baidu.com/api/qzasync?query=%s&city=%s&is_adq=1&pcmod=1&pn=%d&rn=10' % (urllib.parse.quote(job_type), urllib.parse.quote(city), pn)
            print(url)

            # 获取代理IP
            proxies = get_proxy()
            print('代理ip：', proxies)
            if not proxies:
                res = requests.get(url, headers=headers)
            else:
                res = requests.get(url, headers=headers, proxies=proxies)

            pn += 10
            print(res.status_code)
            data = res.json()

            for url in data['data']['urls']:
                detail_url = 'https://zhaopin.baidu.com/szzw?id=%s' % url
                print(detail_url)

                try:
                    if not proxies:
                        detail_res = requests.get(detail_url)
                    else:
                        detail_res = requests.get(detail_url, proxies=proxies)
                    print(detail_res.status_code)
                    if detail_res.status_code != 200:
                        continue
                    html = detail_res.text

                    company = ''  # 公司名称
                    title = ''  # 标题
                    job_desc = ''  # 工作描述
                    detail_address = ''  # 详细地址
                    release_time = ''  # 发布时间
                    valid_time = ''  # 有效时间
                    salary = ''  # 薪水

                    try:
                        company = re.compile(r'class="bd-tt" data-a-39d218aa>(.*?)<').findall(html)[0]
                        company = company.replace('class="bd-tt" data-a-39d218aa>', '').replace('<', '')
                    except:
                        company = ''

                    try:
                        title = re.compile(r'class="job-name">(.*?)</').findall(html)[0]
                    except Exception as e:
                        print(e)
                        title = '%s市招%s' % (city, job_type)

                    try:
                        job_desc = re.compile(r'<span>职位描述：(.*?)<!---->').findall(html)[0]
                        job_desc = job_desc.replace('<span>', '').replace('<p>', '').replace('</p>', '').replace(
                            '</span>', '')
                    except Exception as e:
                        print(e)
                        try:
                            job_desc = re.compile(r'><p>工作内容：(.*?)</p>').findall(html)[0]
                            job_desc = job_desc.replace('<span>', '').replace('<p>', '').replace('</p>', '').replace(
                                '</span>', '')
                        except:
                            job_desc = "招%s,要熟练工" % job_type

                    try:
                        detail_address = re.compile(r'工作地址：</p><p class="job-addr-txt">(.*?)</p><div').findall(html)[0]
                        detail_address = detail_address.replace('<p>', '').replace('</p>', '')
                    except Exception as e:
                        print(e)
                        try:
                            detail_address = re.compile(r'<p>工作地点：\D{2,6}</p>').findall(html)[0]
                            detail_address = detail_address.replace('<p>', '').replace('</p>', '')
                        except:
                            detail_address = "%s市" % city

                    try:
                        release_time = re.compile(r'<p>发布时间：(2018-\d{2}-\d{2}).*?</p>').findall(html)[0]
                        release_time = release_time.replace('<p>', '').replace('</p>', '')
                    except Exception as e:
                        release_time = str(datetime.datetime.now().strftime('%Y/%m/%d'))

                    try:
                        valid_time = re.compile(r'<p>有效日期：(.*?)</p>').findall(html)[0]
                        valid_time = valid_time.replace('<p>', '').replace('</p>', '')
                    except Exception as e:
                        valid_time = str((datetime.date.today() + datetime.timedelta(days=+61)).strftime("%Y/%m/%d"))

                    try:
                        salary = re.compile(r'(\d{3,5})-(\d{3,5})</span><span\sclass="unit"').findall(html)[0]
                        salary = salary.replace('</span><span\sclass="unit"', '')
                    except Exception as e:
                        salary = random.randint(50, 70) * 100

                    print('***************************************')
                    print('公司名称', company)
                    print('标题: ', title)
                    print('发布时间: ', release_time)
                    print('有效时间: ', valid_time)
                    print('薪水: ', salary)
                    print('地址: ', detail_address)
                    print('工作描述: ', job_desc)
                    print('***************************************')

                    info_dict = {
                        'province': province,
                        'city': city,
                        'title': title,
                        'company': company,
                        'job_desc': job_desc,
                        'detail_address': detail_address,
                        'job_type': job_type,
                        'release_time': release_time,
                        'valid_time': valid_time,
                        'require': job_desc,
                        'status': '审核通过',
                        'phone': '',
                        'public_time': ''
                    }
                    save_to_mongodb(info_dict)

                except:
                    print('error')
                    continue

        except Exception as e:
            print(e)
            print('等10秒~~~')
            time.sleep(10)


def main():
    job_type = '电工'
    city = '杭州'
    province = '浙江省'
    token = '==QmmCbqWu9oEqVZp1GaoVpaYWWlUdVmTGWccemaqFnl'

    crawl(job_type, city, province, token)


if __name__ == '__main__':
    main()

