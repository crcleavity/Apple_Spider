# -*- coding: utf-8 -*-
from apple.items import AppleItem
import scrapy


class AppleSpiderSpider(scrapy.Spider):
    name = 'apple_spider'
    allowed_domains = ['www.apple.com.cn']
    start_urls = ['https://www.apple.com.cn/retail/storelist/']

    def parse(self, response):
        shop_list = response.xpath('//*[@id="cnstores"]/div/div/div/div/ul')
        for shop in shop_list:
            apple = AppleItem()
            apple['shop_name'] = shop.xpath('li[1]/a/text()').get()
            apple['address'] = shop.xpath('li[2]/text()').get()
            apple['contact'] = shop.re('400-\d{3}-\d{4}')
            apple['href'] = shop.xpath('li[1]/a/@href').get()
            apple['photo'] = apple['href'] + "images/hero_large.jpg"
            
            yield apple