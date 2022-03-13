"""
requests.get()是同步的代码 要切换为 异步操作
"""
import aiohttp
import asyncio

urls = [
    'http://kr.shanghai-jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg',
    'http://kr.shanghai-jiuxin.com/file/bizhi/20211216/k0vkzf5fpgl.jpg',
    'http://kr.shanghai-jiuxin.com/file/2021/0222/e7dcbb6d848e2b745c44cfdf8dc522c5.jpg'
]


async def download(url):
    img_name = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            # 请求之后，写入文件，可以学习一下 aiofiles
            with open(img_name, mode='wb') as f:
                f.write(await resp.content.read())  # 读取内容是异步的，需要await挂起

            # aiofiles的写法
            # async with aiofiles.open(img_name, mode='wb') as f:
            #     contents = await resp.content.read()
            #     await f.write(contents)
    print(img_name, 'done')

    # aiohttp.ClientSession() 等价于 requests
    # 异步的写法 resp.text()   resp.json()


async def main():
    tasks = []
    for url in urls:
        d = download(url)
        tasks.append(d)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())


