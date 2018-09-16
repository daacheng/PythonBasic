# Python爬虫--设置代理
## 一、requests设置代理,通过proxies参数
requests通过构造字典，通过参数**proxies**即可。

    import requests
    def main():
        proxies = {
            'http': 'http://123.157.67.30:34942'
        }
        res = requests.get('http://httpbin.org/get', proxies=proxies)
        print(res.text)
    if __name__ == '__main__':
        main()

## 二、selenium设置代理
selenium在创建Chrome对象的时候，需要传入参数chrome_options.
* 先创建ChromeOptions对象 chrome_options = webdriver.ChromeOptions()
* 传入代理服务器参数 chrome_options.add_argument('--proxy-server=http://123.157.67.30:34942')
* 创建浏览器对象时，将ChromeOptions作为参数传入。

        import time
        from selenium import webdriver
        def main():
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=http://123.157.67.30:34942')
            browser = webdriver.Chrome(chrome_options=chrome_options)
            browser.get('http://httpbin.org/get')
            time.sleep(9)
            browser.close()
        if __name__ == '__main__':
            main()
