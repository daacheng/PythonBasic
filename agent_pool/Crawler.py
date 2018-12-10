import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time

"""
    爬取代理网站的免费代理并返回
"""


class Crawler(object):

    def get_crawler_proxy(self):
        proxy_list_xici = self.crawl_xici()
        proxy_list_66 = self.crawl_66()
        proxy_list_kuaidaili = self.crawl_kuaidaili()
        return proxy_list_xici + proxy_list_66 + proxy_list_kuaidaili

    def crawl_xici(self):
        """
            爬取西刺代理
        """
        print('爬取西刺代理......')
        proxy_list = []
        for i in range(1, 20):
            try:
                url = 'http://www.xicidaili.com/nn/' + str(i)
                # url = 'http://www.baidu.com'
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.xicidaili.com',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                    'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWJjZjUxMWRkODBlNjA2OTk5YTk2Zjg2MzM5MjQ4YTEwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXcwcFpTcXI2NXVFMHo2MXJGbkplSnc1V3Jhc1I0b21EUTk0SGpPdjhxTHc9BjsARg%3D%3D--81e7db215ded5d21af3e1b11de436f65173eb89d; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1542337081,1544068047; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1544068047'
                }

                res = requests.get(url, headers=headers)
                if res.status_code == 200:
                    doc = pq(res.text)
                    for odd in doc('.odd').items():
                        info_list = odd.find('td').text().split(' ')
                        # print(info_list)
                        if len(info_list) == 11:
                            proxy = info_list[1].strip() + ':' + info_list[2].strip()
                            proxy = proxy.replace(' ', '')
                            proxy_list.append(proxy)
            except Exception as e:
                continue
        print('爬取到西刺代理 %s 个' % len(proxy_list))
        return proxy_list


    def crawl_66(self):
        """
            爬取66代理
        """
        print('爬取66代理......')
        proxies = set()
        for i in range(2, 50):
            try:
                url = 'http://www.66ip.cn/' + str(i) + '.html'
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.66ip.cn',
                    'Referer': 'http://www.66ip.cn/',
                    'Cookie': 'yd_cookie=b04f4f2e-bece-46a1ac6ee50ce2ffd7b607de356fce654d8e; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1543800567,1543892144,1544411555,1544411564; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1544411564; _ydclearance=cdc56c50fac95ebdcc5cb44a-f476-4ed6-9412-40debf56f8a6-1544418766',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                # print(res.status_code)
                # print(res.text)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('.container table tr')

                for i in range(1, len(items)):
                    tds = items[i].select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        # print(proxy)
                        # print(proxy.replace(' ', ''))
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到66代理 %s 个' % len(proxies))
        return list(proxies)


    def crawl_kuaidaili(self):
        print('爬取快代理......')
        proxies = set()
        for i in range(1, 50):
            try:
                url = 'https://www.kuaidaili.com/free/inha/' + str(i)
                time.sleep(1)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.kuaidaili.com',
                    'Referer': 'http://www.66ip.cn/',
                    'Cookie': 'channelid=0; sid=1543828498576461; _ga=GA1.2.2019923346.1543828501; _gid=GA1.2.613511733.1544411613; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1543828501,1543892257,1544068211,1544411614; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1544411614',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                # print(res.status_code)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('#list tbody tr')
                for item in items:
                    tds = item.select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到块代理 %s 个' % len(proxies))
        return list(proxies)

