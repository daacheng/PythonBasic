import hashlib
import urllib
from urllib import parse
import urllib.request
import base64
import json
import time
from PIL import Image
import os
import time

url_preffix='https://api.ai.qq.com/fcgi-bin/'


def setParams(array, key, value):
    array[key] = value


def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, parse.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str.encode('utf-8'))
    return hash_md5.hexdigest().upper()


class AiPlat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
        self.url_data = ''

    def invoke(self, params):
        self.url_data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(self.url, self.url_data)

        try:
            rsp = urllib.request.urlopen(req)
            str_rsp = rsp.read().decode('utf-8')
            dict_rsp = json.loads(str_rsp)
            return dict_rsp
        except Exception as e:
            print(e)
            return {'ret': -1}

    def face_detectface(self, image, mode):
        self.url = url_preffix + 'face/face_detectface'
        setParams(self.data, 'app_id', self.app_id)
        setParams(self.data, 'app_key', self.app_key)
        setParams(self.data, 'mode', mode)
        setParams(self.data, 'time_stamp', int(time.time()))
        setParams(self.data, 'nonce_str', int(time.time()))
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data.decode("utf-8"))
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)
        return self.invoke(self.data)


if __name__ == '__main__':
    AppID = '1106858595'
    AppKey = 'bNUNgOpY6AeeJjFu'

    FACE_PATH = 'face/'
    # 审美标准
    BEAUTY_THRESHOLD = 50

    # 最小年龄
    GIRL_MIN_AGE = 14

    filepath_list = []
    pic_dir = r'E:\code\PythonBasic\spider\zhihu_spider\pic'
    for root, dirs, files in os.walk(pic_dir):
        for file in files:
            filepath_list.append(os.path.join(root, file))
    for filepath in filepath_list:
        # filepath = 'pic/eccadb3aly1fxklvyd05uj20qo0zkwl7.jpg'
        print('##########################')
        print(filepath)
        with open(filepath, 'rb') as bin_data:
            image_data = bin_data.read()


        ai_obj = AiPlat(AppID, AppKey)
        time.sleep(1.5)
        rsp = ai_obj.face_detectface(image_data, 0)
        print(rsp)

        major_total = 0
        minor_total = 0

        if rsp['ret'] == 0:
            beauty = 0
            for face in rsp['data']['face_list']:
                print(face)
                face_area = (face['x'], face['y'], face['x'] + face['width'], face['y'] + face['height'])
                print(face_area)
                img = Image.open(filepath)
                cropped_img = img.crop(face_area).convert('RGB')
                cropped_img.save(FACE_PATH + face['face_id'] + '.png')
                # 性别判断
                if face['beauty'] > beauty and face['gender'] < 50:
                    beauty = face['beauty']

                if face['age'] > GIRL_MIN_AGE:
                    major_total += 1
                else:
                    minor_total += 1

            # 是个美人儿~关注点赞走一波
            if beauty > BEAUTY_THRESHOLD and major_total > minor_total:
                print('发现漂亮妹子！！！')


        else:
            print(rsp)


