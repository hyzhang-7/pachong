import requests
from lxml import etree
import time

url = "https://nanjing.zbj.com/search/f/?kw=saas"
resp = requests.get(url)

html = etree.HTML(resp.text)

# 获取所有服务商的div
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for i in divs:  # 每一个服务商
    # 返回的是列表，所以先取出列表内的第一个元素，然后去掉金额前面的人民币符号
    price = i.xpath('./div/div/a[2]/div[2]/div/span[1]/text()')[0][1:]
    title = 'saas'.join(i.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))

    #       APP开发/小程序开发/前端开发/软件开发/
    #       <hl>saas</hl>
    #       平台
    # 因为是搜索结果，所以saas被高亮显示，title的返回结果是 ['APP开发/小程序开发/前端开发/软件开发/', '平台']
    # 所以使用 'saas'.join(['APP开发/小程序开发/前端开发/软件开发/', '平台']) 进行拼接
    shop_name = i.xpath('./div/div/a/div/p/text()')[1].strip()  # 有换行符需要剔除

    city = i.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]
    print(price, title, shop_name, city)
    time.sleep(1)


resp.close()
print('over')

