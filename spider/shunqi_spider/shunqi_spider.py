import requests
from bs4 import BeautifulSoup
import csv
from queue import Queue
import threading
import os
import traceback

"""
    顺企网 公司基本信息爬取
    一、获取 顺企网(http://b2b.11467.com/)公司行业分类(大类)(75)
    二、获取 公司行业分类(大类)下每个细分类型的url(1868)
    三、获取 每一个细分类型下的公司url。

"""

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208=1542459691,1542459766,1542811198,1543747746; Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208=1543749436',
    'Host': 'b2b.11467.com',
    'Referer': 'http://www.11467.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

detail_category_url_queue = Queue()
company_url_queue = Queue()
base_dir = r'E:\code\PythonBasic\spider\shunqi_spider\company'

with open('detail_category.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    i = 0
    for row in reader:
        i += 1
        if i < 455:
            continue
        # print(row)
        detail_category_url_queue.put(row)
print(detail_category_url_queue.qsize())

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


def get_main_category_url():
    """
        一、获取 顺企网(http://b2b.11467.com/)公司行业分类(大类)
    """
    url = 'http://b2b.11467.com/'
    res = requests.get(url, headers=headers)
    print(res.status_code)
    # print(res.text)

    soup = BeautifulSoup(res.text, 'html.parser')
    class_list = soup.select('#il .boxcontent li a')

    with open('main_category.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)

        for item in class_list:
            print(item)
            class_name = item.text
            class_url = 'http:' + item.attrs.get('href').replace('http:', '')
            writer.writerow([class_name, class_url])


def get_detail_category_url():
    """
         二、获取 公司行业分类(大类)下每个细分类型的url
    """
    with open('main_category.csv', 'r', encoding='utf-8') as fr:
        reader = csv.reader(fr)
        for row in reader:
            url = row[1]
            res = requests.get(url, headers=headers)
            print(res.status_code)

            soup = BeautifulSoup(res.text, 'html.parser')
            class_list = soup.select('.boxcontent .listtxt dd a')
            with open('detail_category.csv', 'a+', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for item in class_list:
                    print(item)
                    class_name = item.attrs.get('title')
                    class_url = 'http://b2b.11467.com/search/' + item.attrs.get('href')
                    if class_url and class_name:
                        # print(class_name)
                        # print(class_url)
                        writer.writerow([class_name, class_url])


def get_company_url():
    """
        三、每一个 细分类型url下都有最多40页公司信息，爬取这40页的所有公司url
    """
    while not detail_category_url_queue.empty():
        detail_category_info = detail_category_url_queue.get(block=True)

        base_url = detail_category_info[1]  # 行业细分类型url
        category_name = detail_category_info[0]  # 行业细分类型名称
        file_path = os.path.join(base_dir, category_name + '.csv')

        # 获取代理IP
        proxies = get_proxy()

        for i in range(1, 41):

            try:
                url = base_url.replace('.htm', '') + '-' + str(i) + '.htm'

                if not proxies:
                    res = requests.get(url, headers=headers, timeout=30)
                else:
                    res = requests.get(url, headers=headers, proxies=proxies, timeout=30)

                if res.status_code == 200:
                    print('返回值: %s, url: %s, 代理IP: %s' % (res.status_code, url, proxies))
                    soup = BeautifulSoup(res.text, 'html.parser')
                    company_url_list = soup.select('.companylist .f_l a')

                    with open(file_path, 'a+', encoding='utf-8', newline='') as fc:
                        writer = csv.writer(fc)

                        for company in company_url_list:
                            company_url = company.attrs.get('href')
                            company_url = 'http://' + company_url.replace('http://', '')
                            company_name = company.attrs.get('title')
                            writer.writerow([company_name, company_url])
                else:
                    print('返回值: %s, url: %s, 代理IP: %s' % (res.status_code, url, proxies))
            except Exception as e:
                # print(traceback.format_exc())
                print('error_url: ', url)
                with open('error_url.csv', 'a+', encoding='utf-8', newline='') as f_err:
                    writer = csv.writer(f_err)
                    writer.writerow([url])
                continue


def main():
    td_list = []
    for i in range(50):
        td = threading.Thread(target=get_company_url)
        td_list.append(td)

    for td in td_list:
        td.start()
    # print(detail_category_url_queue.empty())

    # get_company_url()


if __name__ == '__main__':
    main()