# 豆瓣-电影-排行榜-喜剧
# get请求
import requests

# url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

# url太长，重新封装参数
url = "https://movie.douban.com/j/chart/top_list"
param = {
    # Payload中的参数
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20"
}

# resp = requests.get(url, params=param)
# print(resp.text)
# 发现没有返回值
# 查看一下headers print(resp.request.headers) {
# 'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
# 所以需要改一下headers

headers = {
    "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 "
        "Safari/537.36 "
}
resp = requests.get(url, params=param, headers=headers)
print(resp.text)
print("*" * 30)
print(resp.json())

# 关闭resp
resp.close()
