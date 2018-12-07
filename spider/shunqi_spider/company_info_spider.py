from bs4 import BeautifulSoup
import traceback
import os
import csv
import requests
from queue import Queue
from pymongo import MongoClient
import threading
#############################################################################
"""
    读取csv文件路径到队列中
"""
base_dir = r'E:\code\PythonBasic\spider\shunqi_spider\company_after_clear'
all_files_queue = Queue()
html_queue = Queue()
company_url_queue = Queue()
for root, dirs, files in os.walk(base_dir):
    for file in files:
        all_files_queue.put(os.path.join(root, file))
##############################################################################
"""
    连接数据库
"""
client = MongoClient('localhost', 27017)
shunqi = client.shunqi
collection = shunqi.company_info_more            # 公司信息表


def save_to_mongodb(info):
    try:
        if collection.insert_one(info):
            print('记录成功！')
    except Exception:
        print('记录失败！')


def get_proxy():
    """
        根据之前代理池系统，对外提供的web访问接口，从代理池获取代理
    """
    try:
        get_proxy_utl = 'http://127.0.0.1:5000/random'
        res = requests.get(get_proxy_utl)
        # print(res.status_code)
        if res.status_code == 200:
            # print('从代理池中获取代理IP: %s' % res.text)
            proxies = {'http': 'http://' + res.text}
            return proxies
        else:
            return None
    except Exception as e:
        print('从代理池中获取代理IP出错了！！ %s' % e)
        return None


def parse_html():
    while True:
        html, url = html_queue.get(block=True)
        company_info = {
            '公司名称': '',
            '主营产品': '',
            '经营范围': '',
            '营业执照': '',
            '发证机关': '',
            '核准日期': '',
            '经营期限': '',
            '经营状态': '',
            '成立时间': '',
            '注册资本': '',
            '职员人数': '',
            '所属分类': '',
            '所属城市': '',
            '类型': '',
            '公司地址': '',
            '固定电话': '',
            '经理手机': '',
            '电子邮件': '',
            '公司URL': url
        }
        try:
            soup = BeautifulSoup(html, 'html.parser')
            # 爬取工商信息
            tr_list = soup.select('.boxcontent .codl tr')
            for tr in tr_list:
                td_list = tr.select('td')
                # print(td_list[0].text)
                # print(td_list[1].text)
                # print('######################')
                if '法人名称' in td_list[0].text:
                    company_info['公司名称'] = td_list[1].text.replace(' ', '')
                elif '经营产品' in td_list[0].text:
                    company_info['主营产品'] = td_list[1].text.replace(' ', '')
                elif '经营范围' in td_list[0].text:
                    company_info['经营范围'] = td_list[1].text.replace(' ', '')
                elif '营业执照' in td_list[0].text:
                    company_info['营业执照'] = td_list[1].text.replace(' ', '')
                elif '发证机关' in td_list[0].text:
                    company_info['发证机关'] = td_list[1].text.replace(' ', '')
                elif '核准日期' in td_list[0].text:
                    company_info['核准日期'] = td_list[1].text.replace(' ', '')
                elif '经营期限' in td_list[0].text:
                    company_info['经营期限'] = td_list[1].text.replace(' ', '')
                elif '经营状态' in td_list[0].text:
                    company_info['经营状态'] = td_list[1].text.replace(' ', '')
                elif '成立时间' in td_list[0].text:
                    company_info['成立时间'] = td_list[1].text.replace(' ', '')
                elif '注册资本' in td_list[0].text:
                    company_info['注册资本'] = td_list[1].text.replace(' ', '')
                elif '职员人数' in td_list[0].text:
                    company_info['职员人数'] = td_list[1].text.replace(' ', '')
                elif '所属分类' in td_list[0].text:
                    company_info['所属分类'] = td_list[1].text.replace(' ', '')
                elif '所属城市' in td_list[0].text:
                    company_info['所属城市'] = td_list[1].text.replace(' ', '')
                elif '类型' in td_list[0].text:
                    company_info['类型'] = td_list[1].text.replace(' ', '')
                else:
                    pass

            # 爬取联系方式
            contact_info_list = soup.select('#contact .boxcontent .codl')
            for item in contact_info_list:
                dt_list = item.select('dt')
                dd_list = item.select('dd')
                for i in range(0, len(dt_list)):
                    if '公司地址' in dt_list[i].text:
                        company_info['公司地址'] = dd_list[i].text
                    elif '固定电话' in dt_list[i].text:
                        company_info['固定电话'] = dd_list[i].text
                    elif '经理手机' in dt_list[i].text:
                        company_info['经理手机'] = dd_list[i].text
                    elif '电子邮件' in dt_list[i].text:
                        company_info['电子邮件'] = dd_list[i].text
                    else:
                        pass

            if company_info['公司名称']:
                print(company_info)
                save_to_mongodb(company_info)
        except Exception as e:
            print(e)
            print('* 解析HTML失败！！！！！！！！')


def send_request():
    while True:
        url = company_url_queue.get(block=True)
        html = ''
        request_time = 0

        """
            一个url请求失败后，重新发送请求，最多请求5次
        """
        while True:
            try:
                proxies = get_proxy()
                print('代理IP: %s' % proxies)
                res = requests.get(url, proxies=proxies, timeout=3)
                print('返回值: %s, url: %s' % (res.status_code, url))
                if res.status_code == 200:
                    html = res.text
                    break
                else:
                    request_time += 1
                    if request_time > 5:
                        break
            except Exception as e:
                print('请求次数: %s (%s)' % (request_time, e))
                request_time += 1
                if request_time > 5:
                    break
                continue

        if html:
            html_queue.put((html, url))
        else:
            with open('error_company_url.csv', 'a+', encoding='utf-8', newline='') as f_err:
                writer = csv.writer(f_err)
                writer.writerow([url])
            print('status_code: %s , error url: %s' % (res.status_code, url))


def crawl_company_info():
    """
        读取csv文件，获取公司url，放到队列中 (company_url_queue)
    """
    while True:
        try:
            filepath = all_files_queue.get(block=True)
            name = os.path.split(filepath)[1]
            row_list = []
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    # print(row)
                    row_list.append(row)

            for row in row_list:
                url = row[1]
                company_url_queue.put(url)
        except Exception as e:
            print(e)


def main():

    """
        1、从csv文件中获取公司URL，放到队列中(company_url_queue)
        2、从队列(company_url_queue)中取出公司URL,发送http请求，得到请求结果html,将html放到队列中（html_queue）
        3、从队列中取出请求结果html，进行解析，入库。
    """

    for i in range(0, 10):
        td1 = threading.Thread(target=crawl_company_info)
        td2 = threading.Thread(target=send_request)
        td3 = threading.Thread(target=parse_html)
        td1.start()
        td2.start()
        td3.start()


if __name__ == '__main__':

    main()
