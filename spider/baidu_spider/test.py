import requests
import json
from bs4 import BeautifulSoup
import re
import urllib


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
    token = '%3D%3DwkmKrqYydqXxlmwJGlXi2Yoh2lZRoYqp2bXeZlmhZZ'
    for i in range(2):

        url = 'https://zhaopin.baidu.com/api/qzasync?query=%s&city=%s&is_adq=1&pcmod=1&token=%s&pn=%d&rn=10' % (urllib.parse.quote(job_type), urllib.parse.quote(city), token, pn)
        print(url)
        res = requests.get(url, headers=headers)
        pn += 10
        print(res.status_code)
        data = res.json()

        # print(data)

        for item in data['data']['disp_data']:
            print(item['@name'])

        for url in data['data']['urls']:
            detail_url = 'https://zhaopin.baidu.com/szzw?id=%s' % url
            print(detail_url)

            try:
                detail_res = requests.get(detail_url)
                print(detail_res.status_code)
                html = detail_res.text
                #         print(html)
                address = re.compile(r'<p>工作地点：\D{2,6}</p>').findall(html)[0]
                print(address.replace('<p>', '').replace('</p>', ''))

                title = re.compile(r'class="job-name">(.*?)</').findall(html)[0]
                print(title)

                job_desc = re.compile(r'<span>职位描述：(.*?)<!---->').findall(html)[0]
                print(job_desc
                      )
                detail_address = re.compile(r'工作地址：</p><p class="job-addr-txt">(.*?)</p><div').findall(html)[0]
                print(detail_address)
            except:
                print('error')
                continue


if __name__ =='__main__':
    main()
