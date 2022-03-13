from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

# 准备好参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")


web = Chrome(options=opt)  # 把参数配置设置到浏览器中

web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')

# 定位到下拉列表
select_element = web.find_element_by_xpath('//*[@id="OptionDate"]')
# 对元素进行包装，包装成下拉菜单
sel = Select(select_element)
# 让浏览器进行调整选项
for i in range(len(sel.options)):  # i就是每一个下拉框选项索引位置
    sel.select_by_index(i)  # 按照索引进行切换
    time.sleep(2)
    table = web.find_elements_by_xpath('//*[@id="TableList"]/table/tbody/tr')  # 每一行
    for j in table:
        film_rank = j.find_element_by_xpath('./td[1]').text
        film_name = j.find_element_by_xpath('./td[2]/a/p').text
        film_type = j.find_element_by_xpath('./td[3]').text
        film_box = j.find_element_by_xpath('./td[4]').text
        film_unit = j.find_element_by_xpath('./td[5]').text
        film_times = j.find_element_by_xpath('./td[6]').text
        film_region = j.find_element_by_xpath('./td[7]').text
        film_open_date = j.find_element_by_xpath('./td[8]').text
        print(film_rank, film_name, film_type, film_box, film_unit, film_times, film_region, film_open_date)
    print("=="*20)


# 拿到页面代码elements(经过数据加载以及js执行之后的html内容)
# web.page_source

