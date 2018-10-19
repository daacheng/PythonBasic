# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FtxSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 标题
    huxing = scrapy.Field()  # 户型
    size = scrapy.Field()  # 面积
    floor = scrapy.Field()  # 楼层
    fangxiang = scrapy.Field()  # 方向
    year = scrapy.Field()  # 建房时间
    shop_community = scrapy.Field()  # 小区
    address = scrapy.Field()  # 地址
    total_price = scrapy.Field()  # 总价（万）
    price = scrapy.Field()  # 单价（万/m2）
