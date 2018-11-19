import requests
import re
import csv
from bs4 import BeautifulSoup
import time
import os
import logging.handlers
from queue import Queue
import threading

"""
    顺企网爬虫：通过公司名爬取公司联系方式
"""

###############################################################################
"""
    通用日志配置,代码copy过来直接使用mylog对象即可
"""
# 日志模块配置
# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# 创建log日志文件夹
dir_path = os.path.split(__file__)[0]
logdir = os.path.join(dir_path, 'log')
try:
    os.makedirs(logdir, exist_ok=True)
except FileExistsError:
    pass
module_name = os.path.basename(__file__).replace('.py', '')
mylog = logging.getLogger(__name__)
mylog.setLevel(logging.DEBUG)
# 按照每天一个日志，保留最近14个
filehandler = logging.handlers.TimedRotatingFileHandler(
    filename='%s/%s' % (logdir, module_name),
    when='midnight', interval=1, backupCount=14)
filehandler.suffix = '%Y%m%d.log'
filehandler.extMatch = re.compile(r'^\d{8}.log$')  # 只有填写了此变量才能删除旧日志
# 日志打印格式
filehandler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
mylog.addHandler(filehandler)
# 让日志输出到console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
mylog.addHandler(console)
###################################################################################

company_queue = Queue()
with open('company_1119.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        company_queue.put(row[0])

company_dict = {}


def get_proxy():
    """
        根据之前代理池系统，对外提供的web访问接口，从代理池获取代理
    """
    try:
        get_proxy_utl = 'http://127.0.0.1:5000/random'
        res = requests.get(get_proxy_utl)
        if res.status_code == 200:
            # print('从代理池中获取代理IP: %s' % res.text)
            proxies = {'http': 'http://' + res.text}
            return proxies
        else:
            return None
    except Exception as e:
        print('从代理池中获取代理IP出错了！！ %s' % e)
        return None


def crawl_company_phone():
    while True:
        try:
            try:
                # 请求url
                company_name = company_queue.get(block=True)
                url = 'http://so.11467.com/cse/search?s=662286683871513660&ie=utf-8&q=' + company_name

                # 获取代理IP
                proxies = get_proxy()
                print('#######################################################')
                print('代理ip：', proxies)
                if not proxies:
                    res = requests.get(url, timeout=30 )
                else:
                    res = requests.get(url, proxies=proxies, timeout=30)
                print(res.status_code, 'url:', url)

                html = res.text
                p = re.compile(r'<a rpos="" cpos="title" href="http://www.11467.com/qiye/\d*.htm')
                a_res = p.findall(html)
                if a_res:
                    company_url = a_res[0].replace('<a rpos="" cpos="title" href="', '').replace("'", '')
                    print('公司url: ', company_url)

                    if not proxies:
                        company_res = requests.get(company_url, timeout=30)
                    else:
                        company_res = requests.get(company_url, proxies=proxies, timeout=30)

                    company_html = company_res.text
                    soup = BeautifulSoup(company_html, 'html.parser')
                    tel_list = soup.select('#logotel')
                    # print(tel_list)
                    if tel_list:
                        phone = tel_list[0].string
                        mylog.info('公司：%s, 电话：%s' % (company_name, phone))
                        company_dict[company_name] = phone

            except Exception as e:
                print('error: ', e)

                res = requests.get(url)
                html = res.text
                p = re.compile(r'<a rpos="" cpos="title" href="http://www.11467.com/qiye/\d*.htm')
                a_res = p.findall(html)
                if a_res:
                    company_url = a_res[0].replace('<a rpos="" cpos="title" href="', '').replace("'", '')
                    print('公司url: ', company_url)
                company_res = requests.get(company_url)
                company_html = company_res.text
                soup = BeautifulSoup(company_html, 'html.parser')
                tel_list = soup.select('#logotel')
                # print(tel_list)
                if tel_list:
                    phone = tel_list[0].string
                    mylog.info('公司：%s, 电话：%s' % (company_name, phone))
                    company_dict[company_name] = phone
        except Exception as e:
            time.sleep(1)
            continue

def main():
    td_list = []
    for i in range(5):
        td = threading.Thread(target=crawl_company_phone)
        td_list.append(td)

    for td in td_list:
        td.start()


if __name__ == '__main__':
    main()