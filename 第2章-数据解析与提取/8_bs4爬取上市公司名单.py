import requests
from bs4 import BeautifulSoup
import csv

# 爬取A股上市公司名单
# 1.拿到源代码
# 2.使用bs4进行解析，拿到数据

f = open('8_public_company.csv', mode='w')
csv_writer = csv.writer(f)

url = 'https://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=1'
resp = requests.get(url)

# 解析数据
# 1.把源代码交给bs4进行处理，生成bs对象，'html.parser' 告诉bs4我输入的是源代码
page = BeautifulSoup(resp.text, 'html.parser')

"""
从bs对象中查找数据
find(标签,属性值)，并且find只查找一个
findall(标签,属性值)
"""

# class是python的类名，所以加一个下划线，两种写法都可以
# table = page.find('table', class_="fancyTable")
table = page.find('table', attrs={'class': "fancyTable"})  # 返回的是table那段源代码
trs = table.find_all('tr')[1:]  # 从1开始取，0表示表头行

# 写入列名
csv_writer.writerow(['code', 'name_abbr', 'name', 'province', 'city', 'income', 'profit',
                     'employees', 'launch_date', 'cate', 'product', 'main_business'])
for tr in trs:  # 每一行
    tds = tr.find_all('td')  # 每一行的所有td
    code = tds[1].text  # .text表示拿到被标签标记的内容
    name_abbr = tds[2].text
    name = tds[3].text
    province = tds[4].text
    city = tds[5].text
    income = tds[6].text
    profit = tds[7].text
    employees = tds[8].text
    launch_date = tds[9].text
    cate = tds[12].text
    product = tds[13].text
    main_business = tds[14].text
    csv_writer.writerow([code, name_abbr, name, province, city, income, profit,
                         employees, launch_date, cate, product, main_business])
resp.close()
f.close()
print('over')
