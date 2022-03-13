"""
让程序连接到浏览器，让浏览器来完成各种复杂的操作，我们只接受最终的结果
selenium：自动化测试工具
可以打开浏览器，然后像人一样去操作浏览器
程序员可以从selenium中直接提取网页上的各种信息

环境搭建：
    pip install selenium
    下载浏览器驱动 http://chromedriver.storage.googleapis.com/index.html
        把解压缩的驱动 chromedriver 放在python解释器所在的文件夹  /opt/anaconda3/bin
        如果解压之后的文件名后带有数字 需要把数字删除，如 chromedriver 3
"""

# 让selenium驱动谷歌浏览器
from selenium.webdriver import Chrome

# 1.创建浏览器对象
web = Chrome()

# 2.打开一个网址
web.get("http:www.baidu.com")

print(web.title)