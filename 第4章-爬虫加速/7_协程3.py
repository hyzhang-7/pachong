import asyncio
import time


async def func1():
    print('你好，我是张桓屹')
    # time.sleep(3)  # 当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)  # 异步操作的代码
    print('你好，我是张桓屹')


async def func2():
    print('你好，我是33')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('你好，我是33')


async def func3():
    print('你好，我是44')
    # time.sleep(3)
    await asyncio.sleep(3)
    print('你好，我是44')


if __name__ == '__main__':
    f1 = func1()
    f2 = func2()
    f3 = func3()
    tasks = [f1, f2, f3]
    # 一次性启动多个任务
    t1 = time.time()
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2 - t1)  # 发现执行时间缩短了很多


############################################################
############################################################
# 推荐的写法

async def main():
    tasks = [func1(), func2(), func3()]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)  # 发现执行时间缩短了很多


# 在爬虫领域的应用
async def download(url):
    print('开始下载')
    await asyncio.sleep(2)  # 网络请求
    print('下载完成')


async def main():
    urls = ['baidu', '163', 'bilibili']
    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
