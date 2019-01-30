import requests
import re
import os
import time
import csv
from queue import Queue

# key是图片的url路径, value是图片所属的问题id（哪一个问题下的图片）
image_url_dict = {}

img_tag = re.compile(r"""<img\s.*?\s?data-original\s*=\s*['|"]?([^\s'"]+).*?>""", re.I)


# '292901966': '有着一双大长腿是什么感觉',
# '26297181': '大胸女生如何穿衣搭配',
# '274143680': '男生会主动搭讪一个长得很高并且长得好看的女生吗',
# '266695575': '当你有一双好看的腿之后会不会觉得差一张好看的脸',
# '297715922': '有一副令人羡慕的好身材是怎样的体验',
# '26037846': '身材好是一种怎样的体验',
# '28997505': '有个漂亮女朋友是什么体验',
# '29815334': '女生腿长是什么感觉',
# '35255031': '你的身材不配你的脸是一种怎样的体验',
# '274638737': '大胸妹子夏季如何穿搭',
# '264568089': '你坚持健身的理由是什么现在身材怎么样敢不敢发一张照片来看看',
# '49075464': '在知乎上爆照是一种什么样的体验',
# '22918070': '女生如何健身练出好身材',
# '56378769': '女生身高170cm以上是什么样的体验',
# '22132862': '女生如何选购适合自己的泳装',
# '46936305': '为什么包臀裙大部分人穿都不好看',
# '266354731': '被人关注胸部是种怎样的体验',
# '51863354': '你觉得自己身体哪个部位最漂亮',
# '66313867': '身为真正的素颜美女是种怎样的体验',
# '34243513': '你见过最漂亮的女生长什么样',
# '21052148': '有哪些评价女性身材好的标准',
# '52308383': '在校女学生如何才能穿搭得低调又时尚',
# '50426133': '平常人可以漂亮到什么程度',
# '268395554': '你最照骗的一张照片是什么样子',
# '277593543': '什么时候下定决心一定要瘦的',
# '277242822': '室友认为我的穿着很轻浮我该如何回应',
# '36523379': '穿和服是怎样的体验'
question_id_dict = {'62972819': '你们见过最好看的coser长什么样'}


def to_csv(image_url_dict):
    with open('image_urls.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for k, v in image_url_dict.items():
            writer.writerow([k, v])


def get_pic_urls():
    for question_id in question_id_dict.keys():

        headers = {
            'referer': 'https://www.zhihu.com/question/' + question_id,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'cookie': '_zap=df060be0-1f62-4eb0-bbb4-e25a7df5d057; _xsrf=rE8vojikPuQr6BmPHoQ3vvyYb4p4yopH; d_c0="AJDiN_6IzA6PTtlScILp1OYKQEbXWyS9E24=|1547024288"; capsion_ticket="2|1:0|10:1547024292|14:capsion_ticket|44:MzYwODQ3OTEyYzg5NGQ1MDg1ZDJlYzM3NjM4NDllYTg=|c9a7c7c195e31124acde99d18f503a97dabe44ce4dd1082d20908438d41a3336"; z_c0="2|1:0|10:1547024293|4:z_c0|92:Mi4xcDljekFBQUFBQUFBa09JM19vak1EaVlBQUFCZ0FsVk5wUVVqWFFDWnZrRXNsaVRPckNNSUF2ZGRnY0pSbjl0Rlp3|15b49d1d4fc22680d78e82410f22a516be708ae88ddc690df30fe2a6d8faebd4"; q_c1=50ec85be93ed4ae99a970b47b56568fe|1547024294000|1547024294000; __gads=ID=12d6e4ce61c46133:T=1547024296:S=ALNI_MaUpRRzsIqkrSCpk4BGSWbuKPPZCg; __utmv=51854390.100-1|2=registration_date=20140204=1^3=entry_date=20140204=1; __utma=51854390.1237612516.1547692926.1547692926.1547792023.2; __utmz=51854390.1547792023.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/people/mrxian-sheng-65/collections; tst=r; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c'
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
    get_pic_urls()

    to_csv(image_url_dict)


if __name__ == '__main__':
    main()