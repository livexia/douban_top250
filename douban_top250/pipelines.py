# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import importlib,sys
# importlib.reload(sys)
# sys.setdefaultencoding('utf8')


class SaveToReadablePipeline(object):
    def __init__(self):
        self.file = open("result.txt",'wb')

    def process_item(self, item, spider):
        line_one = 'top'
        line_two = '链接：'
        line_three = '豆瓣评论：'

        dict1 = dict(item)

        for i in dict1['rank']:
            rank = i
            title = ''.join(dict1['title'])
            star = ''.join(dict1['star'])
            rate = ''.join(dict1['rate'])
            link = ''.join(dict1['link'])
            quote = ''.join(dict1['quote'])

            line_one = line_one + rank + '.' + title + ' 评分' + rate + ' (' + star + ')' + '\n'
            line_two = line_two + link + '\n'
            line_three = line_three + quote + '\n\n'

            self.file.write(line_one.encode('utf-8'))
            self.file.write(line_two.encode('utf-8'))
            self.file.write(line_three.encode('utf-8'))

        return item

    def close_spider(self, spider):
        self.file.close()