# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings


class FtxSpiderPipeline(object):

    def __init__(self):
        # 连接MongoDB
        self.client = pymongo.MongoClient(host=settings['HOST'], port=settings['PORT'])
        # 获取数据库
        self.db = self.client[settings['DB_NAME']]
        # 获取集合
        self.collection = self.db[settings['COLL_NAME']]

    def process_item(self, item, spider):
        print(dict(item))
        self.collection.insert(dict(item))
