import requests
import re
import csv
from bs4 import BeautifulSoup
import time

"""
    顺企网爬虫：通过公司名爬取公司联系方式
"""
company_list = []
with open('company.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        company_list.append(row[0])

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


def main():
    for company in company_list:
        try:
            # 请求url
            company_name = company
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
                    print('公司：%s, 电话：%s' % (company, phone))
                    company_dict[company] = phone




                # time.sleep(10)
                # # print(company_html)
                #
                # phone_list = None
                # res_list = re.compile(r'<dt>固定电话：</dt><dd>\d*-\d*</dd>').findall(company_html)
                # if res_list:
                #     phone_list = res_list
                #
                # else:
                #     res_list = re.compile(r'<dt>固定电话：</dt><dd>\d*</dd>').findall(company_html)
                #     if res_list:
                #         phone_list = res_list
                #
                # if phone_list:
                #     phone = phone_list[0].replace('<dt>固定电话：</dt><dd>', '').replace('</dd>', '')
                #     print(phone)
                #     company_dict[company] = phone
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
                print('公司：%s, 电话：%s' % (company, phone))
                company_dict[company] = phone

            continue

    print(company_dict)


if __name__ == '__main__':
    main()