# Python爬虫--顺企网企业信息爬取
## 写在前面
最近接触一个项目，需要大量的企业相关的数据，类似企业基本信息，工商信息，招聘信息，投资信息等。
顺企网是供企业发布产品供求信息的B2B电子商务平台，收录了342 个城市，92373445 家公司信息。

顺企网下有差不多80个公司行业分类（大类），80个大类下包含了差不多1800多个行业细分类别，每个细分类别下有最多40页的公司列表，每一页下有约40个公司链接。
顺企网没有什么特别的反爬措施，只有访问过频繁会封IP，比较简单，这里用之前搭建好的代理池系统就行（[代理池系统](https://github.com/daacheng/PythonBasic/blob/master/studynotes/Python%E7%88%AC%E8%99%AB--%E4%BB%A3%E7%90%86%E6%B1%A0%E7%BB%B4%E6%8A%A4.md)），差不多1000个代理IP，我要做的是尽可能爬取网站所有的企业基本信息。

![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi1.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi2.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi3.png)
![](https://github.com/daacheng/PythonBasic/blob/master/pic/shunqi4.png)

## 思路
#### crawl_company_urls.py
1. 从主页（http://b2b.11467.com/） 获取80个行业大类的链接url，保存到main_category.csv.
2. 爬取80个公司行业分类(大类)下每个细分类型的url(共1868个),保存到detail_category.csv.
3. 每一个细分类型url下都有最多40页公司信息，爬取这40页的所有公司url,保存到company文件夹下，1800多个csv文件，每个文件名代表一个细分类型。(队列+多线程)

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

#### company_info_spider.py
1. 读取company文件夹下所有的csv文件路径到all_files_queue队列中。
2. 处理all_files_queue队列，从csv文件中获取公司URL，放到队列中(company_url_queue)
3. 从队列(company_url_queue)中取出公司URL,发送http请求，得到请求结果html,将html放到队列中（html_queue）
4. 从队列中取出请求结果html，进行解析，入库。

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


**三个队列，每个队列对应10个线程处理，最后速度还可以。用三个队列主要是把“url的获取”、“url的请求”、“url的解析”，全部分开处理，尽量减少因http请求引起的阻塞时间，每次请求最多等待3秒，请求失败会重新获取代理IP发送请求，同一个url最多请求5次，提高容错率，以及http请求效率**

## 代码地址
https://github.com/daacheng/PythonBasic/tree/master/spider/shunqi_spider
