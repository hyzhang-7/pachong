import scrapy


class BasedOnTerminalSpider(scrapy.Spider):
    name = 'based_on_terminal'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://nanjing.zbj.com/search/f/?kw=saas']

    def parse(self, response):
        divs = response.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
        # print('saas'.join(divs[2].xpath('./div/div/a[2]/div[2]/div[2]/p/text()').extract()))
        all_data = []
        for i in divs:  # 每一个服务商
            # 返回的是列表，所以先取出列表内的第一个元素，然后去掉金额前面的人民币符号
            price = i.xpath('./div/div/a[2]/div[2]/div/span[1]/text()').extract()
            title = 'saas'.join(i.xpath('./div/div/a[2]/div[2]/div[2]/p/text()').extract())
            dic = {
                'price': price[0][1:],
                'title': title
            }
            all_data.append(dic)

        return all_data

# 将返回结果写入csv
# scrapy crawl based_on_terminal -o ./add_data.csv