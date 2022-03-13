import re

# findall返回的是列表
lis = re.findall(r"\d+", "我的电话号是10086,另一个电话是10000")
print(lis)

print('*' * 30)
# finditer返回的是迭代器,从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+", "我的电话号是10086,另一个电话是10000")
print(it)
for i in it:
    print(i)
    print(i.group())

print('*' * 30)
# search返回的是match对象，也需要.group()取结果，并且找到一个结果就返回
import re
sc = re.search(r"\d+", "我的电话号是10086,另一个电话是10000")
print(sc.group())

print('*' * 30)
# match是从头开始匹配，所以会报错
import re
ma = re.match(r"\d+", "我的电话号是10086,另一个电话是10000")
print(ma.group())
