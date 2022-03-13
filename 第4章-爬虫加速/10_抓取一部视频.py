"""
<video src="视频.mp4"></video>
用户上传视频 -> 转码(把视频做处理，2k，1080，标清) -> 切片处理(把单个视频进行切分)
还需要一个文件记录视频切片后的播放顺序、存放的路径，即M3U文件，经过utf-8转码后就变成了M3U8文件

爬取视频的步骤：
1.找到m3u8文件
2.通过m3u8文件下载ts文件
3.通过各种手段把ts文件合并为一个mp4文件
"""

"""
久久影院 https://www.5199dy.com/jjplay/213342/1/1.html
思路：
下载第一层m3u8文件， -> 下载第二层m3u8文件
下载视频
下载秘钥，进行解密操作
合并所有ts文件为一个mp4文件
"""

import requests
import re
import aiofiles
import asyncio
import aiohttp
from Crypto.Cipher import AES
import os


# 从首页获取第一层m3u8文件的下载地址
def get_src(url):
    resp = requests.get(url)
    obj = re.compile(r'var url = "(?P<name>.*?)";', re.S)
    src = obj.findall(resp.text)[0]  # 第一层m3u8文件的下载链接
    return src  # https://qq.sd-play.com/20220305/xOMVvUay/index.m3u8


# 下载m3u8文件
def download_m3u8(url, name):
    resp = requests.get(url)
    with open(name, mode='wb') as f:
        f.write(resp.content)


# 异步下载ts文件1
async def download_ts(url, name, session):
    async with session.get(url) as resp:
        async with aiofiles.open('10_video/' + name, mode='wb') as f:
            await f.write(await resp.content.read())  # 把下载到的内容写入到文件中
    print(f'{name}下载完毕')


# 异步下载ts文件2
async def aio_download():
    tasks = []
    async with aiohttp.ClientSession() as session:  # 如果把session写在download_ts中，那么每次循环都需要请求，
        async with aiofiles.open('10_银行家_second_m3u8.txt', mode='r', encoding='utf-8') as f:
            async for line in f:
                if line.startswith('#'):
                    continue
                line = line.strip()  # 去掉空格和换行符  https://qq.shanshanku.com/20220305/xOMVvUay/hls/5TSLg0I8.ts
                task = asyncio.create_task(download_ts(line, line.split('/')[-1], session))  # 创建下载任务
                tasks.append(task)

            await asyncio.wait(tasks)  # 等待任务结束


# 获取秘钥
def get_key(url):
    resp = requests.get(url)
    return resp.text  # b466bd45ad8efe9a


# 解密
async def dec_ts(name, key):
    aes = AES.new(key=b'b466bd45ad8efe9a', IV=b"0000000000000000", mode=AES.MODE_CBC)
    # 读取每个ts文件，因为第二层m3u8文件中的文件名和下载好的ts文件名一样，所以读取m3u8文件效率更高
    async with aiofiles.open(f'10_video/{name}', mode='rb') as f1, \
            aiofiles.open(f"10_video/temp_{name}", mode='wb') as f2:
        bs = await f1.read()  # 读取下载的ts视频文件
        await f2.write(aes.decrypt(bs))  # 把解密好的文件写入文件
    print(f"{name}解密完毕")


# 解密
async def aio_decode(key):
    tasks = []
    async with aiofiles.open('10_银行家_second_m3u8.txt', mode='r', encoding='utf-8') as f:
        async for line in f:
            if line.startswith('#'):
                continue
            line = line.strip()
            # 开始创建异步任务
            task = asyncio.create_task(dec_ts(line.split('/')[-1], key))
            tasks.append(task)
        await asyncio.wait(tasks)


# 合并
def merge_ts():
    # mac: cat
    # win : copy /b
    lis = []
    with open('10_银行家_second_m3u8.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            line = line.strip()
            line = line.split('/')[-1]
            lis.append(f"10_video/temp_{line}")

    s = ' '.join(lis)  # 把lis列表里的每个元素用 空格 分开，变成一个字符串
    os.system(f"cat {s} >movie.mp4")


def main(url):
    # 1.拿到主页的源代码，找到第一层m3u8文件的下载链接
    first_m3u8_url = get_src(url)
    # 2.下载第一层m3u8文件
    download_m3u8(first_m3u8_url, '10_银行家_first_m3u8.txt')
    print('第一层m3u8文件下载完毕')
    # 3.从第一层m3u8文件中拿到第二层m3u8文件的下载链接
    with open('10_银行家_first_m3u8.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue  # 忽视以 # 开头的
            else:
                line = line.strip()  # 去掉空行符和换行符  /20220305/xOMVvUay/hls/index.m3u8
                # 需要和第一层的下载地址进行拼接
                url_split = first_m3u8_url.split('/20220305')[0]
                second_m3u8_url = url_split + line
                # 4.下载第二层第二层m3u8文件
                download_m3u8(second_m3u8_url, '10_银行家_second_m3u8.txt')
                print('第二层m3u8文件下载完毕')

    # 第二层m3u8文件中包含了每个切片视频的下载链接，如https://qq.shanshanku.com/20220305/xOMVvUay/hls/GOxXMgrU.ts
    # 但有时候文件中只有 GOxXMgrU.ts，就需要和检查工具中的ts文件的Request URL进行拼接

    # 发现有3000多个下载链接，考虑使用异步操作
    # 5.下载视频
    asyncio.run(aio_download())
    # 6.拿到秘钥，秘钥的链接地址和ts文件一样，https://qq.shanshanku.com/20220305/xOMVvUay/hls/
    key_url = "https://qq.shanshanku.com/20220305/xOMVvUay/hls/key.key"
    keys = get_key(key_url)

    # 7.解密
    # 读取每个ts文件进行，因此也需要异步
    asyncio.run(aio_decode(keys))

    # 8.合并
    merge_ts()


if __name__ == '__main__':
    url = "https://www.5199dy.com/jjplay/213342/1/1.html"
    main(url)
