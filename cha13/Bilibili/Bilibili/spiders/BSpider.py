# -*- coding: utf-8 -*-
import scrapy
from Bilibili.items import BilibiliItem


class BspiderSpider(scrapy.Spider):
    name = 'BSpider'
    allowed_domains = ['www.bilibili.com']
    # start_urls = ['http://www.bilibili.com/']

    offset = 1
    # url = "https://www.bilibili.com"
    url = 'https://www.bilibili.com/v/anime/serial/#/all/default/0/'
    start_urls = [url + str(offset)]

    def parse(self, response):
        #//ul[contains(@class, 'vd-list') and contains(@class, 'mod-2')]/li[1]/div/div[contains(@class,'l')]/div/a/div[contains(@class,'pic')]/div[contains(@class,'lazy-img')]/img
        # 每一页至多有20部番剧
        # for i in range(21):
        #     for each in response.xpath("//ul[contains(@class, 'vd-list') and contains(@class, 'mod-2')]/li[1]/div/div[contains(@class,'r')]/div[contains(@class,'v-desc')]"):
        #         item = BilibiliItem()
        #         item['title'] = each.xpath("./text()").extract()[0]
        #
        #         yield item
        #

        # lis = response.xpath("//ul[contains(@class, 'vd-list') and contains(@class, 'mod-2')]/li")
        # for li in lis:
        #     item = BilibiliItem()
        #     item['title'] = li.xpath("./div/div[contains(@class,'r')]/a/text()").extract()[0]
        #     print(item['title'])


        # yield scrapy.Request(self.url, callback=self.parse)
        # for each in response.xpath("//ul[contains(@class, 'vd-list') and contains(@class, 'mod-2')]"):
        #     print(each.xpath("./li[1]"))
        # //div[contains(@class, 'demo') and contains(@class, 'other')]
        for each in response.xpath("//ul[contains(@class,'vd-list') and contains(@class,'mod-2')]/li/div/div[@class='r']/a"):
            item = BilibiliItem()
            item['title'] = each.xpath('./text()').extract()
            yield item
        if self.offset < 1319:
            self.offset +=1
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
