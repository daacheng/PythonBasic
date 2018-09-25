import requests
from requests import Request


def main():
    url = 'http://weixin.sogou.com/weixin?query=Python&type=2'
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

    # 创建Session对象
    s = requests.Session()
    # 构造Request对象
    req = Request('GET', url, headers=headers)

    proxies = {
        'http': 'http://221.10.250.48:56766'
    }
    # 将Request对象转换成 PreparedRequest对象
    prepped = s.prepare_request(req)
    # 利用Session对象的send()方法，发送PreparedRequest对象
    res = s.send(prepped, proxies=proxies)

    print(res.text)
    print(res.status_code)

if __name__ == '__main__':
    main()