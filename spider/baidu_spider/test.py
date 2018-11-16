import requests
import json
from bs4 import BeautifulSoup
import re
import urllib
import datetime
import random


headers = {
    'Accept': '*/*',
    'Cookie': 'BAIDUID=2176D64D05517AC3780B774A47F39EB6:FG=1; BIDUPSID=2176D64D05517AC3780B774A47F39EB6; PSTM=1539070163; BDUSS=1lsMWZKSFRUWjBzTDU0TjNJMWxCdnJmc0tOTUR4N2E2MDNxeGdINmZxSk5LdlZiQVFBQUFBJCQAAAAAAAAAAAEAAADi6c1PYmJveb-nt8jX0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAE2dzVtNnc1bb; MCITY=-218%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=2; H_PS_PSSID=26522_1446_21094_27400; Hm_lvt_da3258e243c3132f66f0f3c247b48473=1541989917,1542350086; Hm_lpvt_da3258e243c3132f66f0f3c247b48473=1542350420',
    'Referer': 'https://zhaopin.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}


def main():
    pn = 0
    job_type = '焊工'
    city = '北京'
    token = '%3D%3DwkmKrqYydqXxVmpRWnXi2Yoh2lZR4ZxJ2bXaJmndpZ'
    for i in range(10):

        url = 'https://zhaopin.baidu.com/api/qzasync?query=%s&city=%s&is_adq=1&pcmod=1&token=%s&pn=%d&rn=10' % (urllib.parse.quote(job_type), urllib.parse.quote(city), token, pn)
        print(url)
        res = requests.get(url, headers=headers)
        pn += 10
        print(res.status_code)
        data = res.json()

        # print(data)

        # for item in data['data']['disp_data']:
        #     print(item['@name'])

        for url in data['data']['urls']:
            detail_url = 'https://zhaopin.baidu.com/szzw?id=%s' % url
            print(detail_url)

            try:
                detail_res = requests.get(detail_url)
                print(detail_res.status_code)
                html = detail_res.text
                #         print(html)

                title = ''            # 标题
                job_desc = ''         # 工作描述
                detail_address = ''   # 详细地址
                release_time = ''     # 发布时间
                valid_time = ''       # 有效时间
                salary = ''           # 薪水

                try:
                    title = re.compile(r'class="job-name">(.*?)</').findall(html)[0]
                except Exception as e:
                    print(e)
                    title = '%s市招%s' % (city, job_type)

                try:
                    job_desc = re.compile(r'<span>职位描述：(.*?)<!---->').findall(html)[0]
                    job_desc = job_desc.replace('<span>', '').replace('<p>', '').replace('</p>', '').replace('</span>', '')
                except Exception as e:
                    print(e)
                    try:
                        job_desc = re.compile(r'><p>工作内容：(.*?)</p>').findall(html)[0]
                        job_desc = job_desc.replace('<span>', '').replace('<p>', '').replace('</p>', '').replace('</span>', '')
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
                print('标题: ', title)
                print('发布时间: ', release_time)
                print('有效时间: ', valid_time)
                print('薪水: ', salary)
                print('地址: ', detail_address)
                print('工作描述: ', job_desc)
                print('***************************************')

            except:
                print('error')
                continue


if __name__ == '__main__':
    main()
