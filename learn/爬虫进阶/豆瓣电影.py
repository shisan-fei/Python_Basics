'''

主程序：
    负责调度，调度爬虫程序
'''
import time
import requests
from lxml import etree
import json

def getpage(url):
    '''
    请求数据页面
    :param url: main函数合成的当前页面url
    :return: 返回请求到的html
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.text
        else:
            return None
    except:
        return None


def parsepage(html):
    '''
    html数据解析，拿到电影名称，排名，评分，介绍，海报
    :param html: 解析到的当前页html数据
    :return: 处理后的电影数据
    '''
    html = etree.HTML(html)
    items = html.xpath('//div[@class="item"]')
    for i in items:
        data = {
            '排名':i.xpath('.//div/em[@class=""]/text()'),
            '照片':i.xpath('.//img[@width="100"]/@src'),
            '名称':i.xpath('.//span[@class="title"]/text()'),
            '介绍':i.xpath('.//p[@class=""]/text()'),
            '评分':i.xpath('.//span[@class="rating_num"]/text()')
        }
        yield data

def writefile(item):
    '''
    将得到的数据写入文件
    :param item: 得到的数据
    :return:
    '''
    with open('douban.json','a+',encoding='utf-8') as fp:
        fp.write(json.dumps(item,ensure_ascii=False))

def main(offset):
    url = f'https://movie.douban.com/top250?start={offset}&filter='
    html = getpage(url)
    if html:
        #解析页面数据 parsepage(html)
        for i in parsepage(html):
            print(i)
            #写入数据
            # writefile(i)

if __name__ == '__main__':
    for i in range(2):
        print(f'正在解析第{i}页')
        main(i*25)
        time.sleep(5)
