from urllib.request import urlopen

url = 'http://www.baidu.com'
result = urlopen(url)
# decode()解码 显示中文
# print(result.read().decode('utf-8'))

with open('mybaidu.html',mode='w') as f:
    f.write(result.read().decode('utf-8'))


###################