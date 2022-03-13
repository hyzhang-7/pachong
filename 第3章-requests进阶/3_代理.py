"""
原理：通过第三方的一个机器去发送请求
代理网站
https://www.kuaidaili.com/free/
匿名度为透明的比较好
"""

import requests

proxies = {
    'https': 'https://121.232.125.250'
}

resp = requests.get('https://www.baidu.com', proxies=proxies)
resp.encoding = 'utf-8'
print(resp.text)
