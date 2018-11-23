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
import threading

"""
    该脚本主要是 爬取百度招聘网站上的招聘信息，并将数据存入MongoDB数据库。
    主要内容:
    (省, 市, 区, 工程标题, 工程描述, 详细地址, 工种, 开工日期, 完工日期, 
     薪酬金额, 接包要求 , 发布状态, 发布日期)
"""


"""
    数据库操作
"""
client = MongoClient('localhost', 27017)
baidu = client.baidu
collection = baidu.work_1123


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


###########################################################
"""
    初始化变量
"""
ua = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
      'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
      'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
      'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
      'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
      'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)']


def crawl(job_type, city, province, token, cookie):
    headers = {
        'Accept': '*/*',
        'Cookie': cookie,
        'Referer': 'https://zhaopin.baidu.com/',
        'User-Agent': random.choice(ua)
    }

    pn = 0
    for i in range(10):

        try:
            url = 'https://zhaopin.baidu.com/api/qzasync?query=%s&city=%s&is_adq=1&pcmod=1&token=%s&pn=%d&rn=10' % (
            urllib.parse.quote(job_type), urllib.parse.quote(city).replace('%', '%25'), token, pn)

            # url = 'https://zhaopin.baidu.com/api/qzasync?query=%E6%96%87%E5%91%98&city=%25E6%25AD%25A6%25E6%25B1%2589&is_adq=1&pcmod=1&token=%3D%3DAmS3tqY%2BaoEqFbtxmabe5aspJaXt1Zqd2kYS5kst5l&pn=10&rn=10'
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

            for disp_data in data['data']['disp_data']:
                url = disp_data.get('loc', '')
                district = disp_data.get('district', '')  # 区县

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
                    public_time = str(datetime.datetime.now().strftime('%Y/%m/%d'))  # 采集时间

                    try:
                        company = re.compile(r'class="bd-tt" data-a-39d218aa>(.*?)<').findall(html)[0]
                        company = company.replace('class="bd-tt" data-a-39d218aa>', '').replace('<', '')
                    except:
                        company = ''

                    try:
                        title = re.compile(r'class="job-name">(.*?)</').findall(html)[0]
                    except Exception as e:
                        print(e)
                        title = '招%s' % (job_type)

                    if '管理培训生' in title \
                            or '销售' in title \
                            or '风控岗' in title \
                            or '临床推广' in title \
                            or 'android' in title \
                            or '推广专员' in title:
                        continue

                    # title = '招' + job_type

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
                    print('区县', district)
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
                        'district': district,
                        'title': title,
                        'company': company,
                        'job_desc': job_desc,
                        'detail_address': detail_address,
                        'job_type': job_type,
                        'release_time': release_time,
                        'valid_time': valid_time,
                        'salary': salary,
                        'require': job_desc,
                        'status': '审核通过',
                        'phone': '',
                        'public_time': public_time
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

    job_type_list = ['工长', '电工', '木工', '油漆工', '焊工', '安装工', '水电工', '普工杂工', '工程监理']  # 常见工种

    city = '广州'
    province = '广东'
    token = '%3D%3Dgll2K2XC%2BpJS1ZqZGZpx5aktplZZoaZKGbUimZm92Y'
    cookie = 'BAIDUID=2176D64D05517AC3780B774A47F39EB6:FG=1; BIDUPSID=2176D64D05517AC3780B774A47F39EB6; PSTM=1539070163; BDUSS=1lsMWZKSFRUWjBzTDU0TjNJMWxCdnJmc0tOTUR4N2E2MDNxeGdINmZxSk5LdlZiQVFBQUFBJCQAAAAAAAAAAAEAAADi6c1PYmJveb-nt8jX0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2dzVtNnc1bb; MCITY=-218%3A; Hm_lvt_4b55f5db1b521481b884efb1078a89cc=1542350600; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1541989917,1542350086,1542592345; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=26522_1446_21094; ZD_ENTRY=baidu; pgv_pvi=143252480; pgv_si=s6975098880; delPer=0; PSINO=2'

    for job_type in job_type_list:
        td = threading.Thread(target=crawl, args=(job_type, city, province, token, cookie))
        td.start()


if __name__ == '__main__':
    main()

