# Python爬虫--爬取网站验证码
朋友在做验证码图像识别，用自己代码生成的验证码做训练集训练出来的模型并不能很好适配实际环境下的验证码图片，
所以帮朋友去网上爬一些网站真实环境下应用的验证码，作为训练集。

### 一、分析
在网上随便找了个网站,网站地址：https://www.cndns.com/members/signin.aspx
![](https://github.com/daacheng/PythonBasic/blob/master/pic/wangzhan.png)

分析验证码所在的图片链接，每次点击验证码都会访问这个链接：https://www.cndns.com/common/GenerateCheckCode.aspx?t=sign&temp=0.5219513349247544

这个链接最后的temp参数的值是 通过 onclick="refreshVcodeForLogin() 这个方法生成的。通过搜索在js中找到这个方法，可以看出最后一个参数temp的值是一个0~1以内的随机数。

![](https://github.com/daacheng/PythonBasic/blob/master/pic/wangzhan1.png)

![](https://github.com/daacheng/PythonBasic/blob/master/pic/wangzhan2.png)

![](https://github.com/daacheng/PythonBasic/blob/master/pic/wangzhan3.png)

### 二、根据分析，写爬虫代码

    import requests
    from bs4 import BeautifulSoup
    import random
    import time

    for i in range(4500):
        # 每爬取100个，歇2秒
        if i%100 == 0:
            time.sleep(2)
        # 生成随机数
        suiji_num = random.random()
        url = 'https://www.cndns.com/common/GenerateCheckCode.aspx?t=sign&temp=' + str(suiji_num)
        # 构造请求头
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
        # 发送请求
        res = requests.get(url,headers=headers)
        # 把获取的二进制写成图片
        with open('result//'+str(suiji_num)+'.jpg', 'wb') as f:
            f.write(res.content)

### 结果
![](https://github.com/daacheng/PythonBasic/blob/master/pic/yzm.png)
