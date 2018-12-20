# Python爬虫--爬取微博指定用户主页下的所有图片
## 写在前面
最近比较无聊，冒出来一个想法，去各大图片网站爬取大妹子的图片，然后自己写个简单的网站，按网站分类显示图片，第一个想到的是爬取知乎问题下面的答案，肯定有很多
漂亮的小姐姐，然后是微博，有些图片博主会发很多街拍图片，最后是百度上搜索图片网站。知乎我试了试，网上找了些教程，我放弃了，目前暂时爬不动。于是转战微博，
准备爬取微博用户主页下的发布微博内容中的所有图片，当然文字内容想要一样可以爬取，这里我只爬取图片。<br>
最开始我还是去百度找别人的教程，说不定有写好的代码直接拿来用也行，后来发现基本微博都是模拟登陆，然后爬取用户信息的，感觉很麻烦，后来我自己登录微博试了试，
只用cookies就可以爬取了，功能不是很强的，只能爬取指定用户发布的微博内容，但是代码很简单，实现的功能也满足了自己的需求。
## 分析请求url
首先要先登录自己的微博，然后随便找到一个图片博主，比如这样，
![](https://github.com/daacheng/PythonBasic/blob/master/pic/weibo1.png)

然后打开谷歌开发者调试页面，这里每一页的内容大概是分两三次动态加载的，页面不断地往下滑动，直到在调试页面出现这样一个链接：
![](https://github.com/daacheng/PythonBasic/blob/master/pic/weibo2.png)

接下来我们点击下一页，到第二页，然后下滑获取到这个链接的请求url，观察参数有什么变化
![](https://github.com/daacheng/PythonBasic/blob/master/pic/weibo3.png)

**最后发现请求url中只有三个参数是变化的，表示请求的页面，pagebar，page， pre_page，这样我们就可以通过构造请求url，爬取主页下每一页页的微博内容了**

## 分析页面html
分析页面，可以发现每一篇微博的图片原图链接是字符串的形式在标签中，如图:
![](https://github.com/daacheng/PythonBasic/blob/master/pic/weibo4.jpg)
**最后，我们只需要解析这段字符串，获取图片url，就能够获取到我们要的图片了**

## 代码

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
        'Cookie': ''
    }


    def main():

        if not os.path.exists('pic'):
            os.mkdir('pic')

        for i in range(0, 10):
            for j in range(0, 2):
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

## 结果
![](https://github.com/daacheng/PythonBasic/blob/master/pic/weibo5.jpg)
