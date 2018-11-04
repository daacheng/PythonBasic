import scrapy
from ImageSpider.items import ImagespiderItem


class ImageSpider(scrapy.Spider):

    name = 'imagedown'

    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        image_item = ImagespiderItem()
        urls = response.xpath('//div[@class="post-content"]/p/img/@src').extract()
        image_item['image_urls'] = urls
        yield image_item

