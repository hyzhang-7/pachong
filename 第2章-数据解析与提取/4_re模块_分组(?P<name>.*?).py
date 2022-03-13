import re

s = """
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>周杰伦</span></div>
<div class='jolin'><span id='3'>张三</span></div>
<div class='joe'><span id='4'>丽萨</span></div>
<div class='bob'><span id='5'>郭大刚</span></div>
<div class='zhy'><span id='6'>黄蓉</span></div>
"""

# re.S 是让.能匹配换行符
# (?P<name>.*?) name是分组的名字，可随意取
obj = re.compile(r"<div class='(?P<name>.*?)'><span id='(?P<id>\d+)'>(?P<xingming>.*?)</span></div>", re.S)

res = obj.findall(s)
print(res)

print("*"*30)
res1 = obj.finditer(s)
for i in res1:
    print(i.group('xingming'))
