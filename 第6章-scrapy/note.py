
"""
1、创建一个工程 scrapy startproject projectName
2、cd projectName/，然后在spider子目录中创建一个爬虫文件，
    scrapy genspider spiderName www.xxx.com
3、执行工程：scrapy crawl spiderName

--数据解析
    response.xpath()

--3_持久化存储-基于终端
    --基于终端指令
        要求：只可以将parse方法的返回值(return)存储到本地的文本文件中，不能存储到数据库中，
            且文本文件仅限于json、jsonlines、jl、csv、xml、marshal、pickle

        将返回结果写入csv
        scrapy crawl based_on_terminal -o ./add_data.csv
    --基于管道
        1.数据解析
        2.在item类中定义相关的属性，将解析的数据封装存储到item类型的对象
        3.将item类型对象提交给管道进行持久化存储的操作
        4.在配置文件settings中开启管道
            # 300表示优先级，数值越小，优先级越高
            ITEM_PIPELINES = {
                                'saveResult.pipelines.SaveresultPipeline': 300,
                            }

    面试题：将爬取到的数据一份存储到本地一份存储到数据库，如何实现？
        --管道文件中一个管道类对应的是将数据存储到一种平台
        --爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
        --process_item中的return item表示将item传递给下一个即将被执行的管道类


修改settings中的设置
ROBOTSTXT_OBEY = False
USER_AGENT

# 显示指定类型的日志信息
LOG_LEVEL = 'ERROR'

"""