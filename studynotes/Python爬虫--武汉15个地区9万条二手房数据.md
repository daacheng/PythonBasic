# Python爬虫--武汉15个地区9万条二手房数据
周末无聊，想着看看武汉的房价现在是多少了，于是想到了爬虫去爬点数据，自己亲手去统计数据应该比在网上听别人说的要靠谱点吧。
在导航上找到了一个叫房天下的网站，正好拿来试手，谁知道这个网站一点反爬措施都没有，尴尬，既然这样就放手去爬数据了。

这次爬取了武汉15个区，大约90000条二手房数据，每条数据包括房屋信息("标题"，"户型","面积","楼层","走向","建房时间","总价","单价","小区","地址")，数据存储MongoDB数据库。
以后可以每个月爬两次，动态关注房价走势。

## 代码
### 爬虫代码

    from pyquery import PyQuery as pq
    import requests
    from pymongo import MongoClient
    import time


    """
        连接MongoDB数据库
    """

    client = MongoClient('localhost', 27017)
    fangtianxia = client.fangtianxia
    # 东湖高新区"房屋信息表"
    collection_dhgx_roomprice = fangtianxia.dhgx_roomprice
    # 洪山区"房屋信息表"
    collection_hongshan_roomprice = fangtianxia.hongshan_roomprice
    # 江岸区"房屋信息表"
    collection_jiangan_roomprice = fangtianxia.jiangan_roomprice
    # 东西湖区"房屋信息表"
    collection_dxh_roomprice = fangtianxia.dxh_roomprice
    # 汉阳区"房屋信息表"
    collection_hanyang_roomprice = fangtianxia.hanyang_roomprice
    # 武昌区"房屋信息表"
    collection_wuchang_roomprice = fangtianxia.wuchang_roomprice
    # 江汉区"房屋信息表"
    collection_jianghan_roomprice = fangtianxia.jianghan_roomprice
    # 硚口区"房屋信息表"
    collection_qiaokou_roomprice = fangtianxia.qiaokou_roomprice
    # 黄陂区"房屋信息表"
    collection_huangpi_roomprice = fangtianxia.huangpi_roomprice
    # 江夏区"房屋信息表"
    collection_jiangxia_roomprice = fangtianxia.jiangxia_roomprice
    # 青山区"房屋信息表"
    collection_qingshan_roomprice = fangtianxia.qingshan_roomprice
    # 蔡甸区"房屋信息表"
    collection_caidian_roomprice = fangtianxia.caidian_roomprice
    # 新洲区"房屋信息表"
    collection_xinzhou_roomprice = fangtianxia.xinzhou_roomprice
    # 汉南区"房屋信息表"
    collection_hannan_roomprice = fangtianxia.hannan_roomprice
    # 沌口区"房屋信息表"
    collection_zhuankou_roomprice = fangtianxia.zhuankou_roomprice


    def save_to_mongodb(collection, room_info):
        """
        保存数据到  东湖高新区"房屋信息表"
        :param collection: 数据库中对应每个地区的“房屋信息表”
        :param room_info: 房屋信息
        """
        try:
            if collection.insert_one(room_info):
                print('记录成功！')
        except Exception:
            print('记录失败！')


    def get_wh_roominfo(collection, baseurl):
        """
            根据指定的地区路径，爬取武汉二手房信息
        """
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'wuhan.esf.fang.com',
            'Referer': 'http://wuhan.esf.fang.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        cookies = {
            'Cookie': 'sf_source=; s=; showAdwh=1; city=wuhan; indexAdvLunbo=lb_ad1%2C0%7Clb_ad2%2C0%7Clb_ad3%2C0%7Clb_ad4%2C0%7Clb_ad5%2C0; global_cookie=386rgzyf1rl9d383k2jgwlnjm16jm33thrp; logGuid=597322e9-3321-4674-86cb-630c0ca44b0d; Integrateactivity=notincludemc; budgetLayer=1%7Cwuhan%7C2018-09-15%2015%3A26%3A53; lastscanpage=0; SoufunSessionID_Esf=3_1536996430_1331; polling_imei=a638be15dc201049; unique_cookie=U_386rgzyf1rl9d383k2jgwlnjm16jm33thrp*9'
        }

        for i in range(1, 100):
            try:
                # 构造完整请求路径
                url = baseurl+str(i)
                # 发起请求
                res = requests.get(url, headers=headers, cookies=cookies)
                # 解析结果，获取房屋信息("标题"，"户型","面积","楼层","走向","建房时间","总价","单价","小区","地址")
                doc = pq(res.text)
                shop_list = doc('.shop_list  .clearfix').items()
                for shop in shop_list:
                    # 标题
                    shop_title = shop.find('.clearfix').text().replace('\n', '')
                    shop_info = shop.find('.tel_shop').text().split('|')
                    if len(shop_info)>4:
                        huxing = shop_info[0]  # 户型
                        size = shop_info[1]  # 面积
                        floor = shop_info[2]  # 楼层
                        fangxiang = shop_info[3]  # 走向
                        shop_time = shop_info[4]  # 建房时间
                    price_info = shop.find('.price_right').text().split(' ')
                    if len(price_info) > 1:
                        # 总价
                        shop_total_price = shop.find('.price_right').text().split(' ')[0]
                        # 单价
                        shop_unit_price = shop.find('.price_right').text().split(' ')[1]
                    # 小区
                    shop_community = shop.find('.add_shop a').text().replace('\n', '').replace(' ', '')
                    # 地址
                    shop_address = shop.find('.add_shop span').text().replace('\n', '').replace(' ', '')

                    if shop_title:
                        room_info = {
                            'title': shop_title,
                            'huxing': huxing,
                            'size': size,
                            'floor': floor,
                            'fangxiang': fangxiang,
                            'time': shop_time,
                            'total_price': shop_total_price,
                            'unit_price': shop_unit_price,
                            'community': shop_community,
                            'address': shop_address
                        }
                        save_to_mongodb(collection, room_info)
                print('********************************************************************')
                time.sleep(3)
            except Exception:
                print('出错了!!!! url:%s' % url)
                time.sleep(5)


    def main():
        # 东湖高新区
        dhgx_baseurl = 'http://wuhan.esf.fang.com/house-a013126/i3'
        # 洪山区
        hongshan_url = 'http://wuhan.esf.fang.com/house-a0495/i3'
        # 江岸区
        jiangan_url = 'http://wuhan.esf.fang.com/house-a0491/i3'
        # 东西湖区
        dxh_url = 'http://wuhan.esf.fang.com/house-a0497/i3'
        # 汉阳区
        hanyang_url = 'http://wuhan.esf.fang.com/house-a0493/i3'
        # 武昌区
        wuchang_url = 'http://wuhan.esf.fang.com/house-a0494/i3'
        # 江汉区
        jianghan_url = 'http://wuhan.esf.fang.com/house-a0490/i3'
        # 硚口区
        qiaokou_url = 'http://wuhan.esf.fang.com/house-a0492/i3'
        # 黄陂区
        huangpi_url = 'http://wuhan.esf.fang.com/house-a0651/i3'
        # 江夏区
        jiangxia_url = 'http://wuhan.esf.fang.com/house-a0652/i3'
        # 青山区
        qingshan_url = 'http://wuhan.esf.fang.com/house-a0496/i3'
        # 蔡甸区
        caidian_url = 'http://wuhan.esf.fang.com/house-a01158/i3'
        # 新洲区
        xinzhou_url = 'http://wuhan.esf.fang.com/house-a0689/i3'
        # 汉南区
        hannan_url = 'http://wuhan.esf.fang.com/house-a0759/i3'
        # 沌口区
        zhuankou_url = 'http://wuhan.esf.fang.com/house-a0934/i3'
        get_wh_roominfo(collection_zhuankou_roomprice, zhuankou_url)


    if __name__ == "__main__":
        main()

数据存入数据库

![](https://github.com/daacheng/PythonBasic/blob/master/pic/roominfo1.png)

![](https://github.com/daacheng/PythonBasic/blob/master/pic/roominfo2.png)

![](https://github.com/daacheng/PythonBasic/blob/master/pic/roominfo3.png)
### 统计代码
从MongoDB数据库读入爬取的数据，统计每个地区房屋总面积与总价格，计算每个地区的平均房价

    from pyquery import PyQuery as pq
    import requests
    from pymongo import MongoClient
    import time


    def main():
        """
        从MongoDB数据库读入爬取的数据，统计每个地区房屋总面积与总价格，计算每个地区的平均房价
        """
        client = MongoClient('localhost', 27017)
        fangtianxia = client.fangtianxia
        # 东湖高新区"房屋信息表"
        collection_dhgx_roomprice = fangtianxia.dhgx_roomprice
        # 洪山区"房屋信息表"
        collection_hongshan_roomprice = fangtianxia.hongshan_roomprice
        # 江岸区"房屋信息表"
        collection_jiangan_roomprice = fangtianxia.jiangan_roomprice
        # 东西湖区"房屋信息表"
        collection_dxh_roomprice = fangtianxia.dxh_roomprice
        # 汉阳区"房屋信息表"
        collection_hanyang_roomprice = fangtianxia.hanyang_roomprice
        # 武昌区"房屋信息表"
        collection_wuchang_roomprice = fangtianxia.wuchang_roomprice
        # 江汉区"房屋信息表"
        collection_jianghan_roomprice = fangtianxia.jianghan_roomprice
        # 硚口区"房屋信息表"
        collection_qiaokou_roomprice = fangtianxia.qiaokou_roomprice
        # 黄陂区"房屋信息表"
        collection_huangpi_roomprice = fangtianxia.huangpi_roomprice
        # 江夏区"房屋信息表"
        collection_jiangxia_roomprice = fangtianxia.jiangxia_roomprice
        # 青山区"房屋信息表"
        collection_qingshan_roomprice = fangtianxia.qingshan_roomprice
        # 蔡甸区"房屋信息表"
        collection_caidian_roomprice = fangtianxia.caidian_roomprice
        # 新洲区"房屋信息表"
        collection_xinzhou_roomprice = fangtianxia.xinzhou_roomprice
        # 汉南区"房屋信息表"
        collection_hannan_roomprice = fangtianxia.hannan_roomprice
        # 沌口区"房屋信息表"
        collection_zhuankou_roomprice = fangtianxia.zhuankou_roomprice

        area_dict = {
            # '东湖高新区': collection_dhgx_roomprice,
            # '洪山区': collection_hongshan_roomprice,
            # '江岸区': collection_jiangan_roomprice,
            # '东西湖区': collection_dxh_roomprice,
            # '汉阳区': collection_hanyang_roomprice,
            # '武昌区': collection_wuchang_roomprice,
            # '江汉区': collection_jianghan_roomprice,
            # '硚口区': collection_qiaokou_roomprice,
            # '黄陂区': collection_huangpi_roomprice,
            # '江夏区': collection_jiangxia_roomprice,
            # '青山区': collection_qingshan_roomprice,
            # '蔡甸区': collection_caidian_roomprice,
            # '新洲区': collection_xinzhou_roomprice,
            # '汉南区': collection_hannan_roomprice,
            '沌口区': collection_zhuankou_roomprice
        }

        # 统计结果
        statistic_res = {}

        for area in area_dict.items():
            # 总价格
            total_price = 0
            # 总面积
            total_size = 0
            length = 0
            for room in area[1].find():
                # print(room)
                total_size += int(float(room['size'][:-3]))
                total_price += int(float(room['total_price'].split('万')[0]))
                length += 1
            print(length)
            print(total_price*10000)
            print(total_size)
            average_price = round(total_price*10000/total_size, 2)
            print('%s：%d 元/平方米' % (area[0], average_price))
            statistic_res[area[0]] = average_price
            print(statistic_res)


    if __name__ == "__main__":
        main()

### 可视化

    import matplotlib.pyplot as plt
    import matplotlib

    # 垂直条形图
    def main():
        # 统计数据
        data = {'东湖高新区': 21016.46,
                '洪山区': 19673.17,
                '江岸区': 24970.01,
                '东西湖区': 16142.81,
                '汉阳区': 19079.9,
                '武昌区': 27032.32,
                '江汉区': 21933.65,
                '硚口区': 19577.95,
                '黄陂区': 14796.93,
                '江夏区': 16194.93,
                '青山区': 20422.83,
                '蔡甸区': 13206.6,
                '新洲区': 7637.38,
                '汉南区': 9445.6,
                '沌口区': 15587.82}

        # 指定默认字体，可以支持中文
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['font.family'] = 'sans-serif'

        # 绘图
        # 第一个参数表示：每个柱x轴左边界，第二个参数表示：每个柱y轴下边界
        plt.bar(range(15), data.values(), width=0.5, align='center', color='steelblue', alpha=0.8)
        plt.title('武汉各地区二手房价格比较')
        # 轴标签
        plt.ylabel('价格')
        # 刻度标签
        plt.xticks(range(15), data.keys())
        # 设置Y轴范围
        plt.ylim([5000, 30000])
        # 为每个条形图添加数值标签
        for x, y in enumerate(data.values()):
            # 前两个参数表示标签的坐标位置，第三个参数表示标签的值
            plt.text(x, y+500, '%s' %round(y, 1), ha='center')
        plt.show()


    if __name__ == '__main__':
        main()

![](https://github.com/daacheng/PythonBasic/blob/master/pic/roominfo4.png)
