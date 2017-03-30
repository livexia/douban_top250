# -*- coding: utf-8 -*-

import scrapy
from douban_top250.items import DoubanTop250Item


class Top250Spider(scrapy.Spider):
    name = "top250"
    # TODO
    start_urls = [
        'https://movie.douban.com/top250/'
    ]

    def parse(self, response):
        for info in response.xpath('//div[@class="item"]'):
            item = DoubanTop250Item()
            item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()
            item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()
            item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()
            #item['star'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span／text()').extract()
            item['star'] = info.xpath('//*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[2]/div/span[4]/text()').extract()
            item['rate'] = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['quote'] = info.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            yield item

        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)