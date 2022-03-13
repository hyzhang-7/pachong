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

# 查找寻访数据的位置，进行数据提取
# 找到页面中存放数据的所有div
for i in range(15):
    li = web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[%d+1]' % i)
    job_name = li.find_element_by_xpath('./div/div/div/a').text
    job_salary = li.find_element_by_xpath('./div/div/div[2]/span').text
    company = li.find_element_by_xpath('./div/div[2]/div/a').text
    print(company, job_name, job_salary)







