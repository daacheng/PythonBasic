# coding=gbk
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
from urllib import parse
from parsel import Selector


# info_list = []
# with open('info1.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print(row)
#         info_list.append(row)
#         # print(info_list)


headers = {
    'Accept': '*/*',
    'Cookie': 'BAIDUID=2176D64D05517AC3780B774A47F39EB6:FG=1; BIDUPSID=2176D64D05517AC3780B774A47F39EB6; PSTM=1539070163; BDUSS=1lsMWZKSFRUWjBzTDU0TjNJMWxCdnJmc0tOTUR4N2E2MDNxeGdINmZxSk5LdlZiQVFBQUFBJCQAAAAAAAAAAAEAAADi6c1PYmJveb-nt8jX0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2dzVtNnc1bb; MCITY=-218%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; H_PS_PSSID=26522_1446_21094_27400; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1541989917,1542350086; Hm_lpvt_da3258e243c3132f66f0f3c247b48473=1542350420',
    'Referer': 'https://zhaopin.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


client = MongoClient('localhost', 27017)
baidu = client.baidu
collection = baidu.company_phone

def main():
    # city_list = []
    # with open('common_citys.csv', 'r', encoding='utf-8') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         city_list.append(row[0])
    #
    # with open('info1.csv', 'r', encoding='utf-8') as f:
    #     with open('info.csv', 'w', encoding='utf-8', newline='') as fw:
    #         writer = csv.writer(fw, delimiter='\t')
    #         reader = csv.reader(f)
    #         for row in reader:
    #             if row[2] in city_list:
    #                 print(row)
    #                 writer.writerow(row)
    # items = collection.find()
    with open('company_phone.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            if row[1] == 'None' or row[1] == '':
                continue
            print(row)
            info = {
                'name': row[0],
                'phone': row[1]
            }

            collection.insert_one(info)

    # res = {}
    # with open('log.txt', 'r', encoding='utf-8', newline='') as f:
    #     data = f.readlines()
    #     for line in data:
    #         if '电话' in line:
    #             company = line.split(', ')[0].split('公司：')[1]
    #             phone = line.split(', ')[1].split('电话：')[1].replace('\r\n', '')
    #             res[company] = phone
    #     print(res)



    # with open('company_phone1.csv', 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f, delimiter='\t')
    #     for k, v in res.items():
    #         writer.writerow([k, v])


if __name__ == '__main__':
    main()

