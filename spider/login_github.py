"""
    模拟登陆github
"""
import requests
from lxml import etree

class Login(object):
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        # github仓库
        self.repositories_url = 'https://github.com/daacheng?tab=repositories'
        self.session = requests.session()

    def get_authenticity_token(self):
        res = self.session.get(self.login_url, headers=self.headers)
        html = etree.HTML(res.text)
        authenticity_token = html.xpath('//input[@name="authenticity_token"]/@value')[0]
        return authenticity_token

    def login(self, username, password, token):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': token,
            'login': username,
            'password': password
        }
        res = self.session.post(self.post_url, data=post_data, headers=self.headers)
        return res
    def run(self):
        token = self.get_authenticity_token()
        res = self.login('daacheng', 'lday0726.', token)
        if res.status_code == 200:
            print('登陆成功。')
            repositories_res = self.session.get(self.repositories_url, headers=self.headers)
            html = etree.HTML(repositories_res.text)
            repositories_list = html.xpath('//a[@itemprop="name codeRepository"]/text()')
            print(repositories_list)

def main():
    login = Login()
    login.run()


if __name__ == '__main__':
    main()