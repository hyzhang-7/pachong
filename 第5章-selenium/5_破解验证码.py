# 破解超级鹰的验证码
import time
from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client

web = Chrome()
web .get("http://www.chaojiying.com/user/login/")

# 处理验证码
# 首先把验证码对应的元素转化为图片
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('用户名', '密码', '9999')
# 解析验证码
dic = chaojiying.PostPic(img, 1902)
# 发挥验证码结果
verify_code = dic['pic_str']

# 在页面中填写用户名、密码、验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('用户名')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('密码')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

time.sleep(2)

# 点击登录按钮
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
