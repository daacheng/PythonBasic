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

question_id_dict = {'292901966': '有着一双大长腿是什么感觉',
                    '26297181': '大胸女生如何穿衣搭配',
                    '274143680': '男生会主动搭讪一个长得很高并且长得好看的女生吗',
                    '266695575': '当你有一双好看的腿之后会不会觉得差一张好看的脸',
                    '297715922': '有一副令人羡慕的好身材是怎样的体验',
                    '26037846': '身材好是一种怎样的体验',
                    '28997505': '有个漂亮女朋友是什么体验',
                    '29815334': '女生腿长是什么感觉',
                    '35255031': '你的身材不配你的脸是一种怎样的体验',
                    '274638737': '大胸妹子夏季如何穿搭',
                    '264568089': '你坚持健身的理由是什么现在身材怎么样敢不敢发一张照片来看看',
                    '49075464': '在知乎上爆照是一种什么样的体验',
                    '22918070': '女生如何健身练出好身材',
                    '56378769': '女生身高170cm以上是什么样的体验',
                    '22132862': '女生如何选购适合自己的泳装',
                    '46936305': '为什么包臀裙大部分人穿都不好看',
                    '266354731': '被人关注胸部是种怎样的体验',
                    '51863354': '你觉得自己身体哪个部位最漂亮',
                    '66313867': '身为真正的素颜美女是种怎样的体验',
                    '34243513': '你见过最漂亮的女生长什么样',
                    '21052148': '有哪些评价女性身材好的标准'
                    }

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

base_dir = r'D:\zhihu_picture'


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
    for i in range(10):
        td = threading.Thread(target=download_pictures)
        td.start()


if __name__ == '__main__':
    main()