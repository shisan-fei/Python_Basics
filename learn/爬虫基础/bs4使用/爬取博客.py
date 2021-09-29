'''
数据源地址：https://www.lmonkey.com/t?category=aGy1J2LvZ
爬取内容：博客时间作者，内容
工具： python request bs4 json

'''
import requests,json
from bs4 import BeautifulSoup

#定义一个类来获取博客页面的博客标题和url
class getboke():
    #定义请求url和请求头
    url = 'https://www.lmonkey.com/t?category=aGy1J2LvZ'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    boke = None   #请求结果写入变量
    varlist = []  #存放处理后的数据

    def __init__(self):
        #发送请求
        res = requests.get(url=self.url,headers=self.headers)
        if res.status_code == 200:
            print('请求成功')
            self.boke = res.text    #将请求结果写入文件之后操作
            if self.parsedata():    #如果解析成功
                self.write()        #将结果写入文件
        else:
            print('请求失败')

    #解析数据，将结果写入列表
    def parsedata(self):
        #解析数据
        soup = BeautifulSoup(self.boke,'lxml')
        try:
            #获取文章
            divs = soup.find_all('div',class_='crayons-story')
            for i in divs:
                r = i.find('span',style="vertical-align: inherit;")    #获取了文章名
                if r:
                    vardict={
                        'title':r.text.strip(),
                        'url':i.a['href']         #获取了url
                        #'作者':
                    }
                    self.varlist.append(vardict)    #将结果写入列表
            return True
        except:
            return False

    #将结果列表写入文件
    def write(self):
            if self.varlist != []:
                try:
                    with open('boke_file.txt','a+',encoding='utf-8') as fp:
                        json.dump(self.varlist,fp)                #将列表转换成json写入
                    return True
                except:
                    return False
            else:
                print('无法取得当前数据')

res = getboke()