# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import importlib,sys
# importlib.reload(sys)
# sys.setdefaultencoding('utf8')


class DoubanTop250Pipeline(object):
    def __init__(self):
        self.file = open('top250.txt', mode='wb')

    def process_item(self, item, spider):
        line_one = 'top'
        line_two = '链接：'
        line_three = '豆瓣评论：'

        for i in range(1, len(item['star']) - 1):
            rank = item['rank']
            title = item['title']
            star = item['star']
            rate = item['rate']
            link = item['link']
            quote = item['quote']
            line_one = line_one + rank + '.' + title + '评分' + rate + '(' + star + ')' + '\n'
            line_two = line_two + link + '\n'
            line_three = line_three + quote + '\n\n'

        self.file.write(line_one)
        self.file.write(line_two)
        self.file.write(line_three)

        # self.file.write(line_one.encode('utf-8'))
        # self.file.write(line_two.encode('utf-8'))
        # self.file.write(line_three.encode('utf-8'))

    def close_spider(self, spider):
        self.file.close()