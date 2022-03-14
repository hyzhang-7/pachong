import scrapy


class SpidersecondSpider(scrapy.Spider):
    name = 'spiderSecond'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response)
