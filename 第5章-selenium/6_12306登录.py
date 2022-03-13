from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from chaojiying import Chaojiying_Client
import time

# 初始化超级鹰
chaojiying = Chaojiying_Client('用户名', '密码', '9298')
web = Chrome()

# 有的网站会识别selenuim
# 1.如果浏览器版本号小于88，在浏览器启动时(此时没有加载任何网页内容)，向页面嵌入js代码，去掉webdriver
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#     navigator.webdriver = undefined
#      Object.defineProperty(navigator, 'webdriver', {
#         get: () => undefined
#      })
#     """
# })

# 2.chrome版本号大于等于88
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')



web = Chrome(options=option)
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)

# # 先处理验证码 验证码类型是找出指定的图片，如找出汽车
# verify_img_element = web.find_element_by_xpath('//*[@id"J-loginImg]')
# # 用超级鹰去识别验证码
# dic = chaojiying.PostPic(verify_img_element.screenshot_as_png, 9004)
# result = dic['pic_str']  # x1,y1|x2,y2|x3,y3
# rs_list = result.split('|')  # 划分出每个坐标
# for rs in rs_list:
#     p_temp = rs.split(',')
#     x = int(p_temp[0])  # x1
#     y = int(p_temp[1])  # y1
#     # 让鼠标移动到某个坐标，然后点击
#     ActionChains(web).move_to_element_with_offset(verify_img_element, x, y).click().perform()

time.sleep(1)

# 输入用户名和密码
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('用户名')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('密码')

# 点击登录
web.find_element_by_xpath('//*[@id="J-login"]').click()

time.sleep(5)

# 滑块验证
button = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(button, 300, 0).perform()  # 拖拽滑块沿横坐标移动300，纵坐标不动
