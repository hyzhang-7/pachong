# 预加载正则表达式，以便重复使用
import re

obj = re.compile('\d+')

res = obj.finditer("我的电话号是10086,另一个电话是10000")
for i in res:
    print(i.group())

res1 = obj.finditer("我的月薪是100000")
for i in res1:
    print(i.group())