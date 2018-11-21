import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup

"""
    爬取代理网站的免费代理并返回
"""


class Crawler(object):

    def get_crawler_proxy(self):
        # proxy_list = self.crawl_xici()
        proxy_list = self.crawl_66()
        return proxy_list

    def crawl_xici(self):
        """
            爬取西刺代理
        """
        print('爬取西刺代理......')
        proxy_list = []
        for i in range(1, 20):

            url = 'http://www.xicidaili.com/nn/' + str(i)
            # url = 'http://www.baidu.com'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.xicidaili.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
            }

            res = requests.get(url, headers=headers)
            doc = pq(res.text)
            for odd in doc('.odd').items():
                info_list = odd.find('td').text().split(' ')
                print(info_list)
                if len(info_list) == 11:
                    proxy = info_list[1].strip() + ':' + info_list[2].strip()
                    print(proxy)
                    proxy_list.append(proxy)
        return proxy_list


    def crawl_66(self):
        """
            爬取66代理
        """
        print('爬取66代理......')
        proxies = set()
        for i in range(2, 50):

            url = 'http://www.66ip.cn/' + str(i) + '.html'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'www.66ip.cn',
                'Referer': 'http://www.66ip.cn/',
                'Cookie': 'yd_cookie=6a7e01d3-10be-4ae2b8e78de96a2800d2acafbb3198899b66; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1542431334,1542515035,1542515047,1542810896; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1542810896; _ydclearance=bbf3278f36318e3da7cd2f93-4ad5-4070-bc2d-12187600dcfe-1542818102',
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
        return list(proxies)