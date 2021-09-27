'''
get请求时python程序request.header默认为'User-Agent': 'python-requests/2.26.0'
    此时浏览器集会知道是爬虫程序，可以通过指定header来伪装成浏览器
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)…………}  此美容可以在浏览器中抓取
使用：
    requests.get(url=url,headers=headers)
'''
import requests
#url = 'https://www.baidu.com'
url = 'http://www.xiladaili.com/gaoni/'

#定义头信息,在浏览器的network中抓取request header。让网站知道认为自己是浏览器而不是爬虫
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
res = requests.get(url=url,headers=headers)
code = res.status_code
print(code)

#相依成功后将响应内容写入文件
if code == 200:
    with open('test.html', 'w', encoding='utf-8') as fp:
        fp.write(res.text)
