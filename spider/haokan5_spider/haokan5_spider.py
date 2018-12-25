import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

"""
    好看听书网爬虫
"""


# 创建浏览器对象，这里用的是谷歌浏览器无界面模式，不用每一次请求都弹出浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options = chrome_options)
wait = WebDriverWait(browser, 15)


def main():
    url = 'http://www.haokan5.com/show/11179.html'

    baseurl = 'http://www.haokan5.com'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'www.haokan5.com',
        'Referer': 'http://www.haokan5.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Cookie': r'safedog-flow-item=4ED93BF0E968879DC187669D851F3617; cck_lasttime=1545702575855; cck_count=0; UM_distinctid=167e30d92580-0d1d70fdc4db33-594d2a16-1fa400-167e30d925a2cb; CNZZDATA1272856968=1926676568-1545698737-null%7C1545698737; ASPSESSIONIDAQSTDCRB=JNDBMCGAHLOGBMBODMFIDPFN; MAX_HISTORY={video:[{"name":"\u81F3\u5C0A\u5C0F\u519C\u6C11","link":"http://www.haokan5.com/show/11179.html","pic":"/pic/uploadimg/2013-8/11179.jpg"}]}; max_cms2_v=%u81F3%u5C0A%u5C0F%u519C%u6C11%20001^http%3A//www.haokan5.com/play/%3F11179-0-0.html_$_|; ASPSESSIONIDCSSQDCRB=JCJFFBBACOACMHFPHADBPAGF; bdshare_firstime=1545702587697; ASPSESSIONIDASSQDBQB=EDJMFELAMBDLKOLJNHFPIPND; ASPSESSIONIDAQQSCAQA=BPGFEBBAKHLCODDFKIAFKKOH'

    }
    res = requests.get(url, headers=headers)
    print(res.status_code)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        a_tag_list = soup.select('.compress li a')
        for a in a_tag_list:
            # 下载页面的html
            if 'down' in a.attrs.get('href'):
                dowmload_html_url = baseurl + a.attrs.get('href')
                print(dowmload_html_url)
                browser.get(dowmload_html_url)
                html = browser.page_source
                dowmload_html_soup = BeautifulSoup(html, 'html.parser')
                iframe_list = dowmload_html_soup.select('iframe')
                for iframe in iframe_list:
                    iframe_src = iframe.attrs.get('src')
                    if iframe_src and 'down.php' in iframe_src:
                        download_url = iframe_src.split('?url=')[1]
                        mp3_name = download_url.split('/')[-1]
                        mp3_path = os.path.join(r'F:\mp3', mp3_name)
                        mp3_res = requests.get(download_url)

                        if mp3_res.status_code == 200:
                            print(mp3_path)
                            print(mp3_res.content)
                            with open(mp3_path, 'wb') as f:
                                f.write(mp3_res.content)
                # 等待提交按钮加载出来，获取按钮
                # down_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fl .dlink')))
                # print(down_button)




                # result = requests.get(dowmload_html_url)
                # if result.status_code == 200:
                #     # print(res.text)
                #     download_soup = BeautifulSoup(result.text, 'html.parser')
                #     download_a_tag = download_soup.select('body')
                #     print(download_a_tag)
                #     print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')




if __name__ == '__main__':
    # print('言情通俗'.encode('gb2312'))
    main()