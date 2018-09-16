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