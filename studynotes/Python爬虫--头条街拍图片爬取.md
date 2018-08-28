# Python爬虫--头条街拍图片爬取
**今日头条网站是利用ajax动态加载，返回json格式的数据**
## 代码
    import requests
    import json
    import os

    def get_jiepaipic(offset):   
        # 构造要爬取的网页url
        url = r'https://www.toutiao.com/search_content/'
        params = {
            'offset':offset,
            'format':'json',
            'keyword':'街拍',
            'autoload':'true',
            'count':20,
            'cur_tab':1,
            'from':'search_tab'
        }
        # 请求头
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
            'accept':'application/json, text/javascript',
            'content-type':'application/x-www-form-urlencoded'
        }
        # 模拟浏览器发送请求
        res = requests.get(url,headers=headers,params=params)
        print(res.url)
        for data in res.json()['data']:
            # 街拍新闻的名称
            title = data.get('title', '')
            # 创建文件夹，用于存放抓取的图片
            try:
                os.makedirs(os.path.join(root_dir,str(offset),title))
            except FileExistsError:
                pass

            if data.get('image_list', ''):
                image_list = data['image_list']
                for i,image_url_dict in enumerate(image_list):
                    # 图片名称
                    image_name = title + str(i)+'.jpg'
                    # 图片本地存放路径
                    image_filepath = os.path.join(root_dir,str(offset),title,image_name)
                    # 图片的url
                    image_url = 'http:'+image_url_dict['url']
                    # 模拟浏览器发送请求
                    image_res = requests.get(image_url)
                    # 将抓取的图片保存到本地
                    if os.path.exists(image_filepath):
                        print('图片已经存在了，',image_name)
                    else:
                        with open(image_filepath, 'wb') as f:
                            f.write(image_res.content)

    if __name__ == '__main__':
        # 存放图片的根目录
        root_dir = r'F:\jiepaipic'
        for i in range(0,90,10):
            get_jiepaipic(i)
# 结果
![](https://github.com/daacheng/PythonBasic/blob/master/pic/toutiaopic.png)
