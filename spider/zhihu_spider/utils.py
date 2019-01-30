import csv
from queue import Queue
import requests
import os
import time
import threading

url_queue = Queue()
with open('image_urls.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        url_queue.put((row))

question_id_dict = {'62972819': '你们见过最好看的coser长什么样'}

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

base_dir = r'F:\zhihu_picture'


def get_proxy():
    """
        根据之前代理池系统，对外提供的web访问接口，从代理池获取代理
    """
    try:
        get_proxy_utl = 'http://127.0.0.1:5000/random'
        res = requests.get(get_proxy_utl)
        if res.status_code == 200:
            print('从代理池中获取代理IP: %s' % res.text)
            proxies = {'http': 'http://' + res.text}
            return proxies
        else:
            return None
    except Exception as e:
        print('从代理池中获取代理IP出错了！！ %s' % e)
        return None


def download_pictures():

    while True:
        try:
            item = url_queue.get(block=True, timeout=180)
            image_url, question_id = item
        except:
            break

        data = None
        request_time = 0

        while True:
            try:
                headers['referer'] = 'https://www.zhihu.com/question/' + question_id
                proxies = get_proxy()
                # print('代理IP: %s' % proxies)
                res = requests.get(image_url, proxies=proxies, headers=headers, timeout=3)
                print('返回值: %s, url: %s' % (res.status_code, image_url))
                if res.status_code == 200:
                    data = res.content
                    break
                else:
                    request_time += 1
                    if request_time > 5:
                        break
            except Exception as e:
                print('请求次数: %s (%s)' % (request_time, e))
                request_time += 1
                if request_time > 5:
                    res = requests.get(image_url, headers=headers)
                    if res.status_code == 200:
                        data = res.content
                    break
                continue

        try:

            # 获取图片所属的问题名称
            question_name = question_id_dict.get(question_id)
            # 创建图片存储的文件夹
            pic_dir = os.path.join(base_dir, question_name)
            if not os.path.exists(pic_dir):
                try:
                    os.makedirs(pic_dir)
                except:
                    pass
            # 图片名称
            pic_name = image_url.split('/')[-1]
            # 图片路径
            pic_path = os.path.join(pic_dir, pic_name)
            if data:
                with open(pic_path, 'wb') as f:
                    f.write(data)
                    print('下载成功: ', pic_name)
                    # time.sleep(0.3)
        except Exception as e:
            print('存入图片数据出错, (%s)' % e)
            continue


def main():
    for i in range(15):
        td = threading.Thread(target=download_pictures)
        td.start()


if __name__ == '__main__':
    main()