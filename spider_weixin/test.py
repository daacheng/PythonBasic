import requests
from requests import Request


class MyRequest(Request):
    """
        继承Request对象，重新构造一个请求对象
    """

    def __init__(self,
                 method='GET', url=None, headers=None, files=None, data=None,
                 params=None, auth=None, cookies=None, hooks=None, json=None,
                 call_back=None, need_proxy=False, failtime=0, timeout=10):
        Request.__init__(self, method, url, headers)
        self.call_back = call_back
        self.need_proxy = need_proxy
        self.failtime = failtime
        self.timeout = timeout


def hello(name):
    print('hello,', name)


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

    # 构造Request对象
    req = MyRequest(url=url, headers=headers, call_back=hello)
    req.call_back('aa')

if __name__ == '__main__':
    main()