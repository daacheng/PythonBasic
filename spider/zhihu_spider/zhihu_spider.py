import requests
import re
import os
import time
import csv
from queue import Queue

# key是图片的url路径, value是图片所属的问题id（哪一个问题下的图片）
image_url_dict = {}

img_tag = re.compile(r"""<img\s.*?\s?data-original\s*=\s*['|"]?([^\s'"]+).*?>""", re.I)

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

# 图片存储路径
base_dir = r'F:\zhihu_picture'


def to_csv(image_url_dict):
    with open('image_urls.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for k, v in image_url_dict.items():
            writer.writerow([k, v])


def download_pictures(image_url_dict):
    # 读取csv文件中的内容到内存中
    url_dict = {}
    with open('image_urls.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            url_dict[row[0]] = row[1]


    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    }

    for image_url, question_id in url_dict.items():
        try:
            headers['referer'] = 'https://www.zhihu.com/question/' + question_id

            res = requests.get(image_url, headers=headers)

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
            if res.status_code == 200:
                with open(pic_path, 'wb') as f:
                    f.write(res.content)
                    print('下载成功: ', pic_name)
                    time.sleep(0.3)
        except Exception as e:
            print('下载图片出错, (%s)' % e)
            continue


def get_pic_urls():
    for question_id in question_id_dict.keys():

        headers = {
            'referer': 'https://www.zhihu.com/question/' + question_id,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'cookie': '_zap=7046aefd-0092-44d1-b880-04de5f981682; _xsrf=G3PwSWza9HcMJ59BxVlze0wjfN1pdghU; d_c0="AKDhuw7Hqg6PThIMSmp4O6KItYCXzMi1pKo=|1544758857"; q_c1=4625ea8f2521418fb16b7045d3344de2|1544758863000|1544758863000; l_cap_id="NDBiN2NmN2UwYmQ4NDNmYmFmZDkyODQ1MTBiZjkxMzk=|1545111159|80d038eba45b0fcd1e0cbdf34427f52bd7765917"; r_cap_id="OGRkNzg0NDE3M2Q0NGUwMWE1ZTk0OTkyMzE2NDMxYjQ=|1545111159|1063ab0137447e5fdc882adc38b1e5a816939cbc"; cap_id="ZTZjNmVkMzBjMTVkNGRmYmIyMDIxYmFiYjRlZjZiN2I=|1545111159|222b5a0f21a39905dac643764b61ac3be422784a"; _cid="2|1:0|10:1545120509|4:_cid|28:MTA1ODM5MjgwODc3NTI2NjMwNA==|b00990cddf1479254a819f23e7942f42952535e4638ffc2428941f089d6b9615"; tst=r; __gads=ID=a9b1d670d026cb80:T=1545291223:S=ALNI_MZ20uGeV5nVgwy2Hv4l3lNYZMyH-g; __utma=51854390.1825326029.1545371950.1545371950.1545371950.1; __utmc=51854390; __utmz=51854390.1545371950.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20140204=1^3=entry_date=20140204=1; capsion_ticket="2|1:0|10:1545374067|14:capsion_ticket|44:OWEzZjVlMjgzYmM4NGZlZDgwYWYzYWEwNDk4Zjc3Njc=|4d1dd267e4fb6931876a78565a8addcc63d9d826501e6c263420a5e03b7134f7"; z_c0="2|1:0|10:1545374068|4:z_c0|92:Mi4xcDljekFBQUFBQUFBb09HN0RzZXFEaVlBQUFCZ0FsVk5kTmNKWFFDNUkwc254NkZrUWpRbG0xVUlQaS0yVURpbi13|daa0e9ef9f099b761fe392ffa1047f2c7ead1a5bdf80e0e9336d3149f99755bc"; tgw_l7_route=27a99ac9a31c20b25b182fd9e44378b8'

        }

        for i in range(0, 500, 5):
            try:
                url = 'https://www.zhihu.com/api/v4/questions/'+question_id+'/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset='+str(i)+'&platform=desktop&sort_by=default'

                res = requests.get(url, headers=headers)
                #     print(res.status_code)
                if res.status_code == 200:
                    data = res.json()
                    if not data['data']:
                        print('没有数据！(%s)' % url)
                        break
                    for answer in data['data']:
                        content = answer.get('content', '')
                        if content:
                            #         print(content)
                            image_url_list = img_tag.findall(content)

                            for image_url in image_url_list:
                                print('图片url: %s, 问题id: %s' % (image_url, question_id))
                                image_url_dict[image_url] = question_id
                else:
                    print('返回值: %s, url: %s' % (res.status_code, url))
                # 防止访问频繁
                time.sleep(1.1)
            except Exception as e:
                print('请求出错, (%s)' % e)
                time.sleep(1.1)
                continue


def main():
    # get_pic_urls()

    # to_csv(image_url_dict)

    download_pictures(image_url_dict)


if __name__ == '__main__':
    main()