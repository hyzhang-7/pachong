import requests

# query = input("输入一个名字")
url = "https://www.sogou.com/web?query=维斯塔潘"

# 加一个请求头
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
}
resp = requests.get(url, headers=headers)
print(resp.text)

# 关闭resp
resp.close()
