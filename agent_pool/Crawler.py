import requests
from bs4 import BeautifulSoup
import time
import traceback

"""
    爬取代理网站的免费代理并返回
"""


class Crawler(object):

    def get_crawler_proxy(self):
        proxy_set_taiyang = self.crawl_taiyang()
        proxy_set_89 = self.crawl_89ip()
        return proxy_set_taiyang | proxy_set_89

    def crawl_taiyang(self):
        print('爬取太阳代理......')
        url = 'http://ty-http-d.upupfile.com/index/index/get_free_ip'
        headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'ty-http-d.upupfile.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }
        proxy_set = set()
        for i in range(1, 15):
            try:
                date = {'page': i}
                res = requests.post(url, data=date, headers=headers)
                html = res.json()['ret_data']['html']
                soup = BeautifulSoup(html, 'html.parser')
                for item in soup.find_all(class_='tr ip_tr'):
                    divs = item.select('div')
                    ip = divs[0].text.replace(' ', '').replace('\n', '')
                    port = divs[1].text.replace(' ', '').replace('\n', '')
                    proxy_ip_port = '{}:{}'.format(ip, port)
                    proxy_set.add(proxy_ip_port)
            except:
                print('爬取太阳代理异常')
                print(traceback.format_exc())
        print('爬取到太阳代理{}个'.format(len(proxy_set)))
        return proxy_set

    def crawl_89ip(self):
        print('爬取89代理......')
        proxy_set = set()
        for i in range(1, 15):
            try:
                url = 'https://www.89ip.cn/index_{}.html'.format(i)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'www.89ip.cn',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
                }
                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, 'html.parser')
                table = soup.find(class_='layui-table')
                for tr in table.select('tr'):
                    tds = tr.select('td')
                    if len(tds) > 2:
                        ip = tds[0].text.replace(' ', '').replace('\n', '').strip()
                        port = tds[1].text.replace(' ', '').replace('\n', '').strip()
                        proxy_ip_port = '{}:{}'.format(ip, port)
                        proxy_set.add(proxy_ip_port)
            except:
                print('爬取89代理异常')
                print(traceback.format_exc())
        print('爬取到89代理{}个'.format(len(proxy_set)))
        return proxy_set

if __name__ == '__main__':
    p = Crawler().get_crawler_proxy()
    print(p)