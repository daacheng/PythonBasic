import requests
import re
import os
import time

image_urls = []

img_tag = re.compile(r"""<img\s.*?\s?data-original\s*=\s*['|"]?([^\s'"]+).*?>""", re.I)

headers = {
    'cookie': 'tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; _zap=22e3f22c-b309-4b75-b85d-a1ec6470806c; _xsrf=3bc02393-e69f-41b6-a44e-c9985c6e6913; d_c0="ABDiOunBsg6PTqlIQxsvSr-E2OIhlCZeMqs=|1545294378"; q_c1=1cb77304bef748249bb9740be08a36bb|1545294381000|1545294381000; l_n_c=1; l_cap_id="MmU2MTYyZjlhYzcyNDI4MDg2MDFmYWIyZDZkM2JlOTU=|1545294509|f5c8a6a68b1bbdddca2a9c03369a62d12c987865"; r_cap_id="ODUxMGY0YWU1Zjg0NDk4MzkyMDcxNDNjYzBhNzg3MDc=|1545294509|1b375d47ddaecc25b40c405d8efc29bd7564adaa"; cap_id="NDcyNTdjMjE5NmYyNGM3ZjgzYTBmYzRmMDMwNDFjNTU=|1545294509|c1adbee1f1aa8032d68cbc6e9bde2fe118ad0399"; n_c=1',
    'referer': 'https://www.zhihu.com/question/20799742',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

for i in range(0, 100, 5):

    url = 'https://www.zhihu.com/api/v4/questions/292901966/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=' + str(
        i) + '&platform=desktop&sort_by=default'

    res = requests.get(url, headers=headers)
    #     print(res.status_code)
    data = res.json()

    for answer in data['data']:
        content = answer.get('content', '')
        if content:
            #         print(content)
            image_url_list = img_tag.findall(content)
            print(image_url_list)
            image_urls.extend(image_url_list)

for image_url in set(image_urls):
    res = requests.get(image_url, headers=headers)
    pic_name = image_url.split('/')[-1]
    pic_path = os.path.join('F:\pic', pic_name)
    if res.status_code == 200:
        with open(pic_path, 'wb') as f:
            f.write(res.content)
            print('下载成功: ', pic_name)
            time.sleep(1.1)