# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import requests
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ApplePipeline(object):
    def __init__(self):
        # 创建一个文件
        self.file = open('apple.csv','w',encoding='utf-8',newline='')
        # 定义csv文件的头部
        self.headers = {
            'shop_name','address','contact','href','photo'
        }
        # 创建一个csv文件的对象
        self.writer  = csv.DictWriter(self.file,self.headers)
        # 构造一个空数据列表
        self.ITEM = []
    def process_item(self, item, spider):
        r = requests.get(item['photo'])
        if r.status_code == 200:
            open('image\%s.jpg'%item['shop_name'],'wb').write(r.content)
        
        # 将抓取的数据添加到数据列表
        self.ITEM.append(item)
        # 写入csv文件的头部
        self.writer.writeheader()
        # 写入每行数据
        self.writer.writerows(self.ITEM)
        return item

    def close_spider(self,spider):
        # 关闭文件流,如果没关闭,将不回有数据
        self.fp.close()

# ImagesPipeline 为系统中下载图片的管道


# class MzituPipeline(object):
#     def process_item(self, item, spider):
#         return item
#继承里系统中下载图片的功能
#class PhotoPipeline(ImagesPipeline):
#
    #发生图片下载请求
#    def get_media_requests(self, item, info):
#        yield scrapy.Request(url=item['photo'])

