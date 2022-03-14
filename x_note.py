import requests
from lxml import etree


url = "https://ishuo.cn/member/4"
resp = requests.get(url)

html = etree.HTML(resp.text)


content = html.xpath('//*[@id="list"]/ul/li[1]/div[1]/text()')
print(content)