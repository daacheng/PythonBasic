import requests
from bs4 import BeautifulSoup
import os
from queue import Queue
import time
import threading

pic_html_queue = Queue()
today = time.strftime("%Y-%m-%d", time.localtime())
base_dir = r'D:\pictures'
if not os.path.exists(base_dir):
    try:
        os.mkdir(base_dir)
    except:
        pass


def get_main_page_urls():
    """
        获取主页中 每一组图片的url
    """
    result = []
    for i in range(1, 6):
        url = 'http://www.win4000.com/meinvtag4_%s.html' % str(i)
        res = requests.get(url)
        print(res.status_code)
        # print(res.text)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            li_list = soup.select('.Left_bar .tab_tj .tab_box .clearfix li')
            for li in li_list:
                page_url = li.select('a')[0].attrs.get('href')
                title = li.select('p')[0].text
                print(title, page_url)
                result.append((title, page_url))

        else:
            print('请求失败[get_main_page_urls](url:%s)' % url)
    return result


def get_single_page_url(result):
    """
        获取每一组图片html页面的url中，每一张图对应的html的url链接
    """
    for item in result:
        group_name = item[0]  # 每一组图片的名称
        pages_url = item[1]   # 每一组图片的html对应的url链接
        res = requests.get(pages_url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            a_list = soup.select('#scroll li a')
            for a in a_list:
                page_url = a.attrs.get('href')  # 获取这组图片中，每一张图片对应的html的url链接
                pic_html_queue.put((group_name, page_url))
        else:
            print('请求失败[get_single_page_url](url:%s)' % pages_url)


def download_pic():
    """
        下载图片到本地
    """
    while True:
        try:
            item = pic_html_queue.get(block=True, timeout=180)
        except:
            break
        group_name = item[0]
        page_url = item[1]
        res = requests.get(page_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        pic_url = soup.select('.pic-large')[0].attrs.get('url')  # 图片链接
        pic_name = pic_url.split(r'/')[-1]  # 图片名称
        pic_dir = os.path.join(base_dir, today, group_name)
        pic_path = os.path.join(pic_dir, pic_name)  # 图片存放路径

        print(pic_url, pic_path)

        if not os.path.exists(pic_dir):
            try:
                os.makedirs(pic_dir)
            except:
                pass
        try:
            res_pic = requests.get(pic_url)
            if res_pic.status_code == 200:
                with open(pic_path, 'wb') as f:
                    f.write(res_pic.content)
        except:
            print('error, pic_url: %s' % page_url)
            continue

    print('图片爬取结束。')


def main():
    result = get_main_page_urls()
    get_single_page_url(result)
    for i in range(5):
        td = threading.Thread(target=download_pic)
        td.start()


if __name__ == '__main__':
    main()