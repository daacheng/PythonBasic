import requests
import os
from bs4 import BeautifulSoup
url='https://tieba.baidu.com/p/4662090035?pn=4'
res=requests.get(url)
res.encoding='utf-8'
soup=BeautifulSoup(res.text,'html.parser')
images=soup.select('.BDE_Image')
def img_size(content):
    # 熟悉下面这个图片处理库，对于验证码处理和AI有很大帮助哦。
    from PIL import Image
    from io import BytesIO
    img = Image.open(BytesIO(content))
    # width,height = img.size  # 获取图片大小，更改图片大小，拼接照片墙自己先试试
    return img.size
for i in images:
    image_name=i.get('src').strip().split('/')[-1]
    r=requests.get(i.get('src').strip())
    if(r.status_code==200):
        print(os.path)
        if not os.path.exists('baidu_img'):  # 没有文件夹，则创建文件夹
            os.mkdir('baidu_img')
        if img_size(r.content)[0] > 400 and img_size(r.content)[1] > 600:  # 图片宽*高大于400*600像素才保存
            print('尺寸不错，留下了')
            open('baidu_img/' + image_name, 'wb').write(r.content)
            
