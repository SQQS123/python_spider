# -*- coding: utf-8 -*-
import scrapy


class BspiderSpider(scrapy.Spider):
    name = 'BSpider'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        pass
