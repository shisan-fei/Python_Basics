'''
数据源地址：https://www.lmonkey.com/t?category=aGy1J2LvZ
爬取内容：博客时间作者，内容
工具： python request bs4

'''
import requests,json
from bs4 import BeautifulSoup

#定义请求url和请求头
url = 'https://www.lmonkey.com/t?category=aGy1J2LvZ'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

#发送请求
res = requests.get(url=url,headers=headers)
#判断是否请求成功
if res.status_code == 200:
    #解析数据
    soup = BeautifulSoup(res.text,'lxml')
    #获取文章
    divs = soup.find_all('div',class_='crayons-story')
    #print(divs)
    for i in divs:
        r = i.find('span',style="vertical-align: inherit;")
        if r:
            vardict={
                'title':r.text.strip(),
                'url':i.a['href']
                #'作者':
            }
            #将数据写入文件
            with open('boke.txt','a+',encoding='utf-8') as fp:
                json.dump(vardict,fp)
