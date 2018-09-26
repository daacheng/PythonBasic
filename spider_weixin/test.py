import requests
from requests import Request


def main():
    url = 'http://weixin.sogou.com/weixin?query=Python&type=2'
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Cookie': 'SUV=006B71D77139A84A5B5AE571AD5DA453; CXID=C8E5DA6273C95D22410632D4243944C9; SUID=4AA839713965860A5B626D580005DFD1; ABTEST=6|1537866610|v1; SNUID=6183125A2C2E5D8255231EE62CBD0949; IPLOC=CN4201; JSESSIONID=aaa3dqRqYyG42bbIkHHvw',
            'Host': 'weixin.sogou.com'
        }

    # 创建Session对象
    s = requests.Session()
    # 构造Request对象
    req = Request('GET', url, headers=headers)

    proxies = {
        'http': 'http://119.28.46.123:8888'
    }
    # 将Request对象转换成 PreparedRequest对象
    prepped = s.prepare_request(req)
    # 利用Session对象的send()方法，发送PreparedRequest对象
    res = s.send(prepped, proxies=proxies)

    print(res.text)
    print(res.status_code)

if __name__ == '__main__':
    main()