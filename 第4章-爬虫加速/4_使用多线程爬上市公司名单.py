import requests
from lxml import etree
import csv
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

f = open('4_public_company.csv', mode='w', encoding='utf-8')
csvwriter = csv.writer(f)


def download_company(url):
    resp = requests.get(url)
    tree = etree.HTML(resp.text)
    table = tree.xpath('//*[@id="myTable04"]/tbody')[0]
    result = table.xpath('./tr')
    # print(len(result)) 每页有20个公司
    for res in result:
        txt = res.xpath('./td/text()')
        csvwriter.writerow(txt)
    print(url, 'done')
    time.sleep(1)


if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 51):
            t.submit(download_company, f'https://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum={i}')

    print('all over')
