# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class SaveresultPipeline(object):
    fp = None

    # 重写父类的一个方法，该方法旨在开始爬虫时被调用一次
    def open_spider(self, spider):
        print('开始爬虫...')
        self.fp = open('./saas.text', 'w', encoding='utf-8')

    # 用于处理item类型的对象
    # 可以接受爬虫文件提交过来的item对象
    # 该方法每接收一个item就会被调用一次
    def process_item(self, item, spider):
        price = item['price']
        title = item['title']

        self.fp.write(price + ',' + title + '\n')

        return item

    def close_spider(self, spider):
        print('爬虫结束...')
        self.fp.close()


class mysqlPipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='qF2n2fh5:diM', db='data',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute("insert into new_table values('%s','%s')" % (item["price"], item["title"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    # 还需要在settings中添加mysqlPipeline
