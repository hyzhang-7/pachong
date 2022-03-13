from lxml import etree

tree = etree.parse('11_xpath入门2使用的文件.html', etree.HTMLParser())
# 返回li节点中a节点的值
result = tree.xpath('/html/body/ul/li/a/text()')
print(result)

# 仅返回第一个li节点中a节点的值
result1 = tree.xpath('/html/body/ul/li[1]/a/text()')
print(result1)

# 返回li节点中a节点中href='dapao'的值
result2 = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')
print(result2)

# 返回li节点中a节点中href值
result3 = tree.xpath('/html/body/ul/li/a/@href')
print(result3)

ol_li_list = tree.xpath('/html/body/ol/li')
print(ol_li_list)

# 从每一个li中提取到属性
for i in ol_li_list:
    # 提取a标签的值
    res = i.xpath('./a/text()')  # 从li中继续查找，相对查找 ./
    print(res)
    # 提取a标签的href值
    res2 = i.xpath('./a/@href')
    print(res2)
