# -*- coding: utf-8 -*-
import scrapy

from anyspider.items import AnyspiderItem


class WwwbaiducomSpider(scrapy.Spider):
    name = 'wwwbaiducom'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost:5000/',
                  # 'http://en.wikipedia.org/wiki/Main_Page',
                  'http://www.baidu.com']

    def parse(self, response):
        # pass
        item = AnyspiderItem()
        title = response.xpath('//div')
        print 'title is: ', title,
        item['title'] = title
        return item