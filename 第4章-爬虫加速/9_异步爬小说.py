# book_id: "4306063500"
# cid: "1569782244" 章节id
# 书的章节名
# url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'

# 每一章的内容
# url2 = 'https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4306063500","cid":"4306063500|1569782244","need_bookinfo":1}'

import requests
import asyncio
import aiohttp
import aiofiles
import time
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36'
}

# 第二步
async def aiodownload(cid, book_id, title):
    data = {
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)  # 把python对象转换成json格式
    content_url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(content_url) as resp:
            content = await resp.json()
            # 写入小说内容，aiofiles的写法
            async with aiofiles.open('9_异步爬小说/' + title + ".txt", mode='w', encoding="utf-8") as f:
                await f.write(content['data']['novel']['content'])  # 小说内容
    time.sleep(1)
    print(title, 'done')
    

# 第一步
async def getCatalog(chapter_url):
    resp = requests.get(chapter_url, headers=headers)
    html_res = resp.json()
    chapter_res = html_res['data']['novel']['items']  # 章节的标题和id章节
    tasks = []
    for chapter in chapter_res:
        title = chapter['title']
        cid = chapter['cid']
        # 准备异步任务
        tasks.append(aiodownload(cid, book_id, title))
        time.sleep(1)
    await asyncio.wait(tasks)


# 每一个章节id对应着一个url

if __name__ == '__main__':
    book_id = "4306063500"
    chapter_url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    asyncio.run(getCatalog(chapter_url))
