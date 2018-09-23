import requests
from pyquery import PyQuery as pq
"""
    爬取代理网站的免费代理并返回
"""


class Crawler(object):

    def get_crawler_proxy(self):
        proxy_list = self.crawl_xici()
        return proxy_list

    def crawl_xici(self):
        """
            爬取西刺代理
        """
        proxy_list = []
        for i in range(1, 20):

            url = 'http://www.xicidaili.com/nn/' + str(i)

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
                if len(info_list) == 11:
                    proxy = info_list[5].lower().strip() + '://' + info_list[1].strip() + ':' + info_list[2].strip()
                    proxy_list.append(proxy)
        return proxy_list
