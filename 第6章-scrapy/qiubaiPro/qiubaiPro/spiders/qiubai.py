import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=1']

    def parse(self, response):
        # 解析：段子内容
        content = response.xpath('//*[@id="myTable04"]/tbody/tr[15]/td[15]/text()')
        # content返回的是列表，但列表元素是Selector类型的对象
        # 调用extract()，将Selector对象中data对应的字符串取了出来
        print(content)
        print(content.extract())
        print(content[0])
        print(content[0].extract())
