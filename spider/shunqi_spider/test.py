from bs4 import BeautifulSoup
import traceback
import os
import csv
import requests


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


def main():

    filepath = r'D:\daacheng\Python\PythonBasic\spider\shunqi_spider\company_after_clear\GPS系统公司黄页.csv'
    name = os.path.split(filepath)[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)

            # 获取代理IP
            proxies = get_proxy()
            url = row[1]
            res = requests.get(url, proxies=proxies)
            print(res.status_code)
            if res.status_code == 200:

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
                    '类型': ''
                }

                soup = BeautifulSoup(res.text, 'html.parser')
                tr_list = soup.select('.boxcontent .codl tr')
                for tr in tr_list:
                    td_list = tr.select('td')
                    # print(td_list[0].text)
                    # print(td_list[1].text)
                    # print('######################')
                    if '法人名称' in td_list[0].text:
                        company_info['公司名称'] = td_list[1].text
                    elif '经营产品' in td_list[0].text:
                        company_info['主营产品'] = td_list[1].text
                    elif '经营范围' in td_list[0].text:
                        company_info['经营范围'] = td_list[1].text
                    elif '营业执照' in td_list[0].text:
                        company_info['营业执照'] = td_list[1].text
                    elif '发证机关' in td_list[0].text:
                        company_info['发证机关'] = td_list[1].text
                    elif '核准日期' in td_list[0].text:
                        company_info['核准日期'] = td_list[1].text
                    elif '经营期限' in td_list[0].text:
                        company_info['经营期限'] = td_list[1].text
                    elif '经营状态' in td_list[0].text:
                        company_info['经营状态'] = td_list[1].text
                    elif '成立时间' in td_list[0].text:
                        company_info['成立时间'] = td_list[1].text
                    elif '注册资本' in td_list[0].text:
                        company_info['注册资本'] = td_list[1].text
                    elif '职员人数' in td_list[0].text:
                        company_info['职员人数'] = td_list[1].text
                    elif '所属分类' in td_list[0].text:
                        company_info['所属分类'] = td_list[1].text
                    elif '所属城市' in td_list[0].text:
                        company_info['所属城市'] = td_list[1].text
                    elif '类型' in td_list[0].text:
                        company_info['类型'] = td_list[1].text
                    else:
                        pass
                print(company_info)
            else:
                print('status_code: %s , error url: %s' % (res.status_code, url))


if __name__ == '__main__':

    main()
