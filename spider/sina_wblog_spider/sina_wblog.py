import os
import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://weibo.com/2419425757/profile?topnav=1&wvr=6&is_all=1',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'SINAGLOBAL=6283620407388.335.1545013420830; un=daacheng@sina.cn; wvr=6; SCF=AoNOcR0Jv549ru7Gy2DIhmjPfcjPqz2SFhIpvw522t2f1mYDwK2emzC4YsUtcQW-aiQjMaHvGtPQBmJQ8RlcZKc.; SUHB=0LcDXmLGXeN6UR; ALF=1547705166; SUB=_2A25xHP4eDeRhGeRK6lsV8ivLzjuIHXVS_oJWrDV8PUJbkNAKLRntkW1NU3WJi4WnonMe-vVZ1ocZnVrrfVyJKfGB; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF6h2LprjiSsc7UbCl.cKaW5JpX5oz75NHD95QESh24ShzfS0-NWs4Dqcjci--fiK.0iK.Ei--fiK.0iK.Ei--fiK.0iK.Ei--fi-2Xi-2Ni--fi-2Xi-2Ni--Ri-8siKLW; UOR=,,www.baidu.com; Ugrow-G0=169004153682ef91866609488943c77f; TC-V5-G0=28bf4f11899208be3dc10225cf7ad3c6; TC-Page-G0=8dc78264df14e433a87ecb460ff08bfe; wb_view_log_2419425757=1920*10801; _s_tentry=www.baidu.com; Apache=8579536681377.65.1545271083129; ULV=1545271083148:3:3:3:8579536681377.65.1545271083129:1545198461605'
}


def main():

    if not os.path.exists('pic'):
        os.mkdir('pic')

    for i in range(0, 10):
        for j in range(0, 2):
            # 构造请求url
            url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&is_hot=1&pagebar=%s&pl_name=Pl_Official_MyProfileFeed__21&id=1005052651221301&script_uri=/u/2651221301&feed_type=0&page=%s&pre_page=%s&domain_op=100505&__rnd=1545271176219' % (str(j), str(i), str(i))

            print(url)
            res = requests.get(url, headers=headers)
            res_data = res.json()
            html = res_data['data']
            soup = BeautifulSoup(html, 'html.parser')
            # print(soup.prettify())  # 格式化html内容
            ul_list = soup.select('.WB_detail .media_box ul')
            for ul in ul_list:
                # print(ul)
                action_data = ul.attrs.get('action-data', '')
                for item in action_data.split('&'):
                    if 'clear_picSrc' in item:
                        pic_urls = item.split('=')[1].replace('%2F', '/').split(',')
                        for pic_url in pic_urls:
                            pic_name = pic_url.split('/')[-1]
                            res_of_pic = requests.get('http:' + pic_url)
                            if res_of_pic.status_code == 200:
                                with open('pic/' + pic_name, 'wb') as f:
                                    f.write(res_of_pic.content)
                                    print('抓取成功', pic_name)


if __name__ == '__main__':
    main()