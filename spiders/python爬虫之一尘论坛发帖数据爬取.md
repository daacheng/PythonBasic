# python爬虫之一尘论坛发帖数据爬取
**方便实时了解四版币及纪念币的行情价格。**

```python
import requests
import re
import time
import traceback
import os
from bs4 import BeautifulSoup

current_dir = os.getcwd()


class Spider:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'www.lc0011.net',
            'Referer': 'http://www.lc0011.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        }
        self.rmb4_html_dir = os.path.join(current_dir, 'html', 'rmb4')
        self.jinianbi_html_dir = os.path.join(current_dir, 'html', 'jinianbi')
        os.makedirs(self.rmb4_html_dir, exist_ok=True)
        os.makedirs(self.jinianbi_html_dir, exist_ok=True)

    def clear_html(self, html_dir):
        for root, dirs, files in os.walk(html_dir):
            for file in files:
                filepath = os.path.join(root, file)
                os.remove(filepath)

    def get_html_dir(self, boardid):
        html_dir = ''
        if boardid == '119':
            # 四版币板块
            html_dir = self.rmb4_html_dir
        elif boardid == '10':
            # 纪念币板块
            html_dir = self.jinianbi_html_dir
        else:
            print('未知的板块ID')
        return html_dir

    def spider_detail(self, url, html_dir):
        try:
            id_ = re.findall('&ID=(\d+)', url)[0] if re.findall('&ID=(\d+)', url) else ''
            if not id_:
                return

            res = requests.get(url, headers=self.headers, timeout=20)
            res.encoding = 'GB2312'
            html = res.text
            html = html.encode().decode('utf-8')
            html_path = os.path.join(html_dir, '{}.html'.format(id_))
            with open(html_path, 'w', encoding='utf-8') as fw:
                fw.write(html)
        except Exception as e:
            print('爬取详情信息异常:{}'.format(e))

    def spider(self, boardid):
        html_dir = self.get_html_dir(boardid)
        if not html_dir:
            return

        self.clear_html(html_dir)

        for i in range(1, 3):
            try:
                url = 'http://www.lc0011.net/index.asp?boardid={}&action=&topicmode=0&page={}'.format(boardid, i)
                res = requests.get(url, headers=self.headers, timeout=20)
                res.encoding = 'GB2312'
                html = res.text
                soup = BeautifulSoup(html, 'html.parser')
                div_list = soup.find_all(attrs={'class': 'list'})
                for item in div_list:
                    a_tag = item.select('.listtitle a')
                    if a_tag:
                        title = a_tag[0].text.replace(' ', '').replace('\n', '').replace('�', '')
                        href = a_tag[0].get('href')
                        href = 'http://www.lc0011.net/' + href
                        print('标题:{}({})'.format(title, href))
                        self.spider_detail(href, html_dir)
            except Exception as e:
                print('爬取第{}页异常:{}'.format(i, e))

    def parse(self, boardid, keyword):
        html_dir = self.get_html_dir(boardid)
        if not html_dir:
            return

        all_files_list = []
        for root, dirs, files in os.walk(html_dir):
            for file in files:
                all_files_list.append(os.path.join(root, file))

        for filepath in all_files_list:
            filename = os.path.basename(filepath)
            id_ = filename.replace('.html', '')
            href = 'http://www.lc0011.net/dispbbs.asp?boardID={}&ID={}&page=1'.format(boardid, id_)
            with open(filepath, 'r', encoding='utf-8') as fr:
                html = fr.read()
                soup = BeautifulSoup(html, 'html.parser')

                title = ''
                for item in soup.select('.th'):
                    if item.find_all(attrs={'style': 'height:24px;float:left;text-indent:10px;'}):
                        title_div = item.find_all(attrs={'style': 'height:24px;float:left;text-indent:10px;'})[0]
                        title = title_div.text.replace('\n', ',').replace('\t', ',').replace(' ', ',')

                if not title or '公告' in title or '栏目' in title or '管理办法' in title:
                    continue

                div_list = soup.select('.postlary1 .post')
                content_list = []
                if div_list:
                    floor_1 = div_list[0].find_all(attrs={'onload': "this.style.overflowX='auto';"})
                    if floor_1:
                        for p in floor_1[0].find_all('p'):
                            if p.text:
                                content_list.append(p.text)
                        if not content_list:
                            content_list.append(floor_1[0].text)

                if not content_list:
                    div_list = soup.select('.postlary2 .post')
                    if div_list:
                        floor_1 = div_list[0].find_all(attrs={'onload': "this.style.overflowX='auto';"})
                        if floor_1:
                            for p in floor_1[0].find_all('p'):
                                if p.text:
                                    content_list.append(p.text)
                            if not content_list:
                                content_list.append(floor_1[0].text)

                content = "\n".join(content_list)

                if keyword and keyword in title:
                    print('标题:{}({})\n'.format(title, href))
                    print('{}\n'.format(content))
                    print('***' * 60)


if __name__ == '__main__':
    spider = Spider()
    # spider.spider(boardid='119')  # 四版币板块
    # spider.spider(boardid='10')  # 纪念币板块

    spider.parse(boardid='119', keyword='802')
    # spider.parse(boardid='10', keyword='802')
    # spider.spider_rmb4()  # 爬取四版币板块
    # spider.parse_rmb4()

```
