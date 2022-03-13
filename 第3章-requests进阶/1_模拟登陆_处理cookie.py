"""
17k小说网
登陆 -> 得到cookie
带着cookie去请求到书架url ->书架上的内容

必须把上面的两个操作连起来
我们可以使用session进行请求 -> session可以认为是一连串的请求，在这个过程中的cookie不会丢失
"""
import requests

session = requests.session()

data = {
    'loginName': '15852303326',
    'password': 'ZHy1996326'
}

# 1.登陆
url = 'https://passport.17k.com/ck/user/login'
resp = session.post(url, data=data)
# print(resp.text)
# print(resp.cookies)

# 2.拿到书架上的数据
# 并且书架上的数据并不在源代码里显示，因此需要从network中找
shelf_url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
resp1 = session.get(shelf_url)
print(resp1.json())
