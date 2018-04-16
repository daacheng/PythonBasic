#爬取贴吧刘诗诗图片
import requests
import os
from bs4 import BeautifulSoup

#定义一个获取图片对象的方法，用于控制获取图片的尺寸大小。
def get_image(content):
    from PIL import Image
    from io import BytesIO
    #BytesIO用于操作内存中的二进制数据
    img=Image.open(BytesIO(content))
    return img

for i in range(3):
    url='http://tieba.baidu.com/p/5071714177?pn='
    url+=str(i)
    #print(url)
    res=requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    images=soup.select('.BDE_Image')
    #print(images)
    for image in images:
        image_name=image.get('src').strip().split('/')[-1]
        image_url=image.get('src').strip()
        #print(image_url)
        r=requests.get(image_url)
        #print(r.status_code)
        if(r.status_code==200):
            if not os.path.exists('lssimages'):
                os.mkdir('lssimages')
            else:
                #控制图片尺寸，宽*高大于400*600
                if(get_image(r.content).size[0]>400 and get_image(r.content).size[1]>600):
                    #wb以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
                    open('lssimages/'+image_name,'wb').write(r.content)
                    print('保存成功')
                else:
                    print('尺寸不行，不要')
                    
