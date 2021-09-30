'''
当频繁请求一个网站时，对方认为被攻击会禁用客户ip
如何解决：
    1. 爬虫时频率降低
    2. 使用代理ip
代理分类：
    透明代理：服务器知道客户端是代理并知道代理ip。
    匿名代理：服务器知道是代理，单不知道ip。
    高匿代理：服务器也不知道是不是代理

http://httpbin.org/get: 请求该url可以将本机请求信息返回
'''
import requests


url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

#找一个代理ip
proxyip={
    'http':'http://106.45.105.172:3256'
    #'https':'http://47.100.14.22:9006'
}
try:
    res = requests.get(url=url,headers=headers,proxies=proxyip)
    if res.status_code == 200:
        print(res.json()['origin'])
except:
        print('请求失败了')