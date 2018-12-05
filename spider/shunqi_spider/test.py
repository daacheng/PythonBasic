from bs4 import BeautifulSoup
import traceback
import os
import csv

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Cookie': 'Hm_lvt_819e30d55b0d1cf6f2c4563aa3c36208=1542459691,1542459766,1542811198,1543747746; Hm_lpvt_819e30d55b0d1cf6f2c4563aa3c36208=1543749436',
    'Host': 'b2b.11467.com',
    'Referer': 'http://www.11467.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}


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
    '公司名称': '',
    '公司名称': '',
}


def main():

    filepath = r'E:\code\PythonBasic\spider\shunqi_spider\company_after_clear\测量工具公司黄页.csv'
    name = os.path.split(filepath)[1]
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == '__main__':

    main()