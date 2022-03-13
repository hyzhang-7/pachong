from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("http://lagou.com")

# 找到某个元素，点击它
el = web.find_element_by_xpath('//*[@id="changeCityBox"]/p[1]/a')
el.click()  # 点击事件

time.sleep(2)
# 找到输入框，输入python
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python', Keys.ENTER)

time.sleep(1)

# 点击一个岗位
web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

# 如何进入到新窗口进行提取
# 注：最新版本的selenium可自动切换窗口
web.switch_to.window(web.window_handles[-1])  # 切换到chrome标签页的最后一个

# 提取新页面的信息，职位描述
job_desc = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div').text
print(job_desc)

# 关掉新页面，返回原来的页面
web.close()
web.switch_to.window(web.window_handles[-1])

# 确认是否返回原来的页面
print(web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text)


# # 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，在然后才能拿到数据
# iframe = web.find_element_by_xpath('//*[@id="player_iframe"]')
# web.switch_to.frame(iframe)
# # 读取iframe页面中的内容
# text = web.find_element_by_xpath('/div/h1').text
# # 再从iframe切换回原页面
# web.switch_to.default_content()