"""
https://www.pearvideo.com/video_1752361
https://video.pearvideo.com/mp4/short/20220221/cont-1752361-15829295-hd.mp4
https://video.pearvideo.com/mp4/short/20220221/1646057542749-15829295-hd.mp4

第一个地址是我们正常浏览看到的
第二个地址是视频的真实地址
第三个地址是检查工具里找到的视频地址
发现使用爬虫找到的地址(第三个地址)被特殊处理了，cont-1752361 被修改为 1646057542749

"""

import requests

raw_url = 'https://www.pearvideo.com/video_1752361'
contid = raw_url.split("_")[1]
# url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1752361&mrd=0.27237100364275535'
url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1752361'

headers = {
    # 防盗链：溯源，本次请求的上一级地址是谁，如果没有这个，就被被认为是非正常访问
    'Referer': 'https://www.pearvideo.com/video_1752361'
}
resp = requests.get(url, headers=headers)
result = resp.json()
video = result['videoInfo']['videos']['srcUrl']
systemtime = result['systemTime']

# 视频链接
real_video = video.replace(systemtime, f'cont-{contid}')

# 请求视频链接，把内容写入文件中
resp1 = requests.get(real_video)

with open('2_video.mp4', mode='wb') as f:
    f.write(resp1.content)

resp.close()
resp1.close()

print('done')