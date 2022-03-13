import re
import requests
import csv
import time

"""
1.定位到2020必看片
2.从2020必看热片中提取到子页面的链接地址
3.请求子页面的链接地址，拿到下载地址
"""

url = 'https://www.dy2018.com/'
resp = requests.get(url)  # 去掉安全验证
resp.encoding = 'gbk'  # 默认的编码是utf-8，而有些网站不是，就会出现乱码，因此需要指定编码格式

# 返回首页的源代码
url_res = resp.text
print("已获取网页源代码")

# 使用正则表达式提取出属于2020必看热片的那部分代码
obj = re.compile(r"2022必看热片.*?<ul>(?P<url>.*?)</ul>", re.S)

# 因为那部分代码只有一块，所以用search就可以
res = obj.search(url_res)
res_link = res.group('url')
print(res_link)

#  <a href='/i/104994.html' title="2021年国产剧情犯罪片《误杀2》4K国语中字">2021年国产剧情犯罪片《误杀2》4K国语中字</a>
# 观察提取后的代码，<a </a>表示超链接，而/i/104994.html就是网址，通过与https://www.dy2018.com/拼接后即为真正的子链接地址

obj1 = re.compile(r"<li><a href='(?P<link_>.*?)' title=", re.S)
res1 = obj1.finditer(res_link)

# 把拼接后的子链接存储的list中
url_lis = []
for i in res1:
    sub_link = url + (i.group('link_')).strip('/')  # 子链接里多了一个 / 需要剔除
    url_lis.append(sub_link)

print("已获取子链接")
time.sleep(3)
# 得到了子链接之后进行访问，然后得到下载地址

# 定位电影名称、下载地址
obj2 = re.compile(r'◎片　　名(?P<film>.*?)'
                  r'<br />◎年.*?<!--xunleiDownList Start-->.*?<td style=.*?<a href="(?P<magnet>.*?)">magnet', re.S)

f = open('6_film_heaven.csv', mode='w')
csv_writer = csv.writer(f)

for i in url_lis:
    resp2 = requests.get(i)  # 访问子链接
    resp2.encoding = 'gbk'
    res2 = obj2.finditer(resp2.text)  # 提取下载地址
    for j in res2:
        dic = j.groupdict()
        dic['film'] = dic['film'].strip()  # 去除电影名前的空行
        csv_writer.writerow(dic.values())

f.close()
resp.close()
resp2.close()
print("该项目结束")