# python爬虫之网易云音乐
* 爬取指定歌单下的歌曲列表
* 爬取指定歌曲的热门评论
* 爬取所有歌单下歌曲的热门评论

```python
import requests
from bs4 import BeautifulSoup
import json
from Cryptodome.Cipher import AES
import base64
import codecs
import re


class Spider163:
    def __init__(self):
        self.playlist_url = 'https://music.163.com/discover/playlist'
        self.comments_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
        self.play_ids = []  # 记录歌单的ID
        self.music_ids = []  # 记录歌单下歌曲的ID

        self.headers = {
            'authority': 'music.163.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'referer': 'https://music.163.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
        }

    def spider_playlist(self):
        # 爬取歌单
        params = {
            'order': 'hot',
            'cat': '全部',
            'limit': '35',
            'offset': '0',
        }
        res = requests.get(self.playlist_url, headers=self.headers, params=params)

        soup = BeautifulSoup(res.text, 'html.parser')
        play_list = soup.select('#m-pl-container li .msk')
        for item in play_list:
            href = item.get('href', '')
            if href and re.findall(r'\?id=(\d+)', href):
                play_id = re.findall(r'\?id=(\d+)', href)[0]
                self.play_ids.append(play_id)

        with open('play_list.json', 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(self.play_ids, ensure_ascii=False))

    def spider_playlist_musics(self, play_id=None):
        # 爬取指定歌单下的歌曲信息，默认爬取全部歌单下的歌曲信息
        if not play_id:
            play_ids = self.play_ids
        else:
            play_ids = [play_id]

        for play_id in play_ids:
            try:
                url = 'https://music.163.com/api/playlist/detail?id={}'.format(play_id)
                res = requests.get(url, headers=self.headers)
                res_json = res.json()
                result = res_json.get('result', {})
                if result:
                    name = result.get('name', '')
                    print('歌单: {}\n'.format(name))
                    for music in result.get('tracks', []):
                        music_name = music.get('name', '')
                        music_id = music.get('id', '')
                        self.music_ids.append(music_id)
                        print('歌曲ID:{:<20}歌曲名称:{}'.format(music_id, music_name))
            except Exception as e:
                print('获取歌单下歌曲信息异常:{}'.format(e))

    def spider_music_hot_comments(self, music_id=None):
        # 爬取指定歌单下的歌曲信息，默认爬取全部歌单下的歌曲信息
        if not music_id:
            music_ids = self.music_ids
        else:
            music_ids = [music_id]

        for music_id in music_ids:
            ic6 = {
                "rid": "R_SO_4_{}".format(music_id),
                "threadId": "R_SO_4_{}".format(music_id),
                "pageNo": "1",
                "pageSize": "20",
                "offset": "40",
                "orderType": "1",
                "csrf_token": ""
            }
            ic6 = json.dumps(ic6, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
            data = spider.encrypt_WangYiYun(ic6)
            res = requests.post(self.comments_url, data=data, headers=self.headers)
            res_json = res.json()
            if res_json.get('data', {}):
                if res_json['data'].get('hotComments', []):
                    for comment in res_json['data'].get('hotComments', []):
                        content = comment.get('content', '').replace('\n', '  ')
                        nickname = comment['user'].get('nickname', '')
                        likedCount = comment.get('likedCount', '')
                        print('昵称:【{}】 评论:【{}】 点赞次数:【{}】'.format(nickname, content, likedCount))

    def get_random_str(self, n):
        """
        产生指定n位数的随机字符串 [a-zA-Z0-9]
        :param n: 随机字符串的位数
        :return:
        """
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        random_str = ""
        # return "".join([random_str+random.choice(text) for i in range(n)]).encode("utf-8")
        return b"abcdefghijklmnop"

    def add_to_16(self, text):
        """
        AES 算法要求明文的字节是16的倍数
            补足为16的倍数
        :param text: 要加密的文本
        :return:
        """
        text += b"\x01" * (16 - len(text) % 16)  # 注意是 不是 \x00
        return text

    def encrypt_AES(self, plaintext, key, iv):
        """
        AES加密
        :param plaintext: 要加密的内容都是16位的字节数据
        :param key: 密钥
        :param iv: 偏移
        :return: 二进制的密文
        """
        # 创建一个 AES 对象
        aes = AES.new(key, AES.MODE_CBC, iv=iv)
        # 加密 明文
        ciphertext = aes.encrypt(self.add_to_16(plaintext))
        return base64.b64encode(ciphertext)

    def encrypt_RSA(self, plaintext, pub_key, modulus):
        """
        RSA 加密
        :param plaintext:
        :param pub_key: 公钥 010001
        :param modulus: 00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
        :return: 二进制的密文
        """
        """
        modulus =
        """
        plaintext = plaintext[::-1]
        rs = int(codecs.encode(plaintext, 'hex_codec'), 16) ** int(pub_key, 16) % int(modulus, 16)
        return format(rs, 'x').zfill(256)

    def encrypt_WangYiYun(self, plaintext):
        """
        网易云音乐加密算法
        :param plaintext: 加密的文本
        :param pub_key: RSA公钥
        :param modulus: AES
        :param key: AES密钥
        :return:
        """
        """
        /*
        * 使用d,g AES加密产生加密enctext
        * 使用e,f RSA加密产生 encSecKey
        */
        function d(d, e, f, g) {
            var h = {} // 对象
            , i = a(16); // 16位的随机字符串
            return h.encText = b(d, g), // g为秘钥对d进行加密
                h.encText = b(h.encText, i), // 又进行了一次加密，使用 i 16位的随机字符串
                h.encSecKey = c(i, e, f), // 使用rsa加密
                h // 最后返回 h 对象
        }
        """
        pub_key = b"010001"
        modulus = b"00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        key = b"0CoJUm6Qyw8W8jud"
        IV = b"0102030405060708"
        # 1. 产生16位的随机字符串
        random_16 = self.get_random_str(16)
        # 2. 获取encText
        encText = self.encrypt_AES(plaintext, key, IV)
        encText = self.encrypt_AES(encText, random_16, IV)
        # 3. 获取encSecKey
        encSecKey = self.encrypt_RSA(random_16, pub_key, modulus)
        return {"params": encText.decode("utf-8"), "encSecKey": encSecKey}


if __name__ == '__main__':
    spider = Spider163()
    # 1.爬取歌单链接
    # spider.spider_playlist()
    # 2.爬取歌单下面的歌曲列表
    # spider.spider_playlist_musics()
    # 3.爬取歌曲下热门评论
    # spider.spider_music_hot_comments()
    # 指定歌曲ID爬取热门评论
    spider.spider_music_hot_comments(music_id='33599439')
```
