"""
1.拿到主页面的源代码，然后提取到子页面的链接地址，href
2.通过href拿到子页面的内容，从子页面中找到图片的下载地址 img -> src
3.下载图片
"""
import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'
resp = requests.get(url)
resp.encoding = 'utf-8'

page = BeautifulSoup(resp.text, 'html.parser')

# 现找到包含链接的那段代码，然后定位到每个链接的标签 a ，返回的是列表
alist = page.find('div', attrs={'class': 'TypeList'}).find_all('a')
for i in alist:
    # 超链接存储在 href 中，直接用get就可以获取，但返回的是部分连接，需要和url进行拼接
    href = 'https://www.umeitu.com' + i.get('href')  # 每个图片的子链接

    # 访问每个图片的子链接
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'utf-8'
    child_page = BeautifulSoup(child_page_resp.text, 'html.parser')
    img = child_page.find('div', attrs={'class': 'ImageBody'}).find('img')
    src = img.get('src')  # 返回每个图片的下载地址
    # 下载图片，也就是把图片内容保存在文件中
    img_resp = requests.get(src)  # img_resp.content 就是图片的内容
    # 设置每个图片的名称，https://kr.zutuanla.com/file/2020/1031/small6b72c57a1423c866d2b9dc10d0473f27.jpg
    # 通过 / 切分每个图片的网页，然后取最后一个作为图片的名称
    img_name = src.split('/')[-1]
    with open('9_save_image/' + img_name, mode='wb') as f:
        # 右键存储图片的文件夹 mark directory as excluded 避免索引卡掉pycharm
        f.write(img_resp.content)  # 把图片内容写入文件
    print(img_name+' 已下载完成')
    time.sleep(2)

print('所有图片已下载完成')

