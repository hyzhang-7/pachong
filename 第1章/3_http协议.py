"""
请求： request headers
1.请求行：请求方式(get、post)、请求url地址、协议
2.请求头：放一些服务器要使用的附加信息
3.请求体：一般放一些请求参数

响应： response headers
1.状态行：协议、状态码
2.响应头：放一些客户端要使用的一些附加信息
3.响应体：服务器返回的真正客户端要用的内容(HTML、json)等

请求头中常见的一些重要内容：
1.User-Agent：请求载体的身份标识(用啥发送的请求)
2.Referer：防盗链(这次请求是从哪个页面来的？反爬会用到)
3.Cookie：本地字符串数据信息(用户登录信息、反爬的token)
"""