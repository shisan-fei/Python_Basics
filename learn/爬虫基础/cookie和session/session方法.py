'''
如果需要爬虫程序主动记录cookies并携带cookies，那么在使用requests之前调用session方法
并使用session方法返回的对象发起登录和请求
'''
import requests
url = 'http://www.xiladaili.com/usercenter/'  #请求的URl
login = 'http://www.xiladaili.com/login/'     #抓取的登录url
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

req = requests.session()

#发起登录请求,该数据来源于抓取from data
data = {
    'username': '大聪明',
    'password': '2000asd92',
    'csrfmiddlewaretoken': 'wVEqQxgHPPxxcp4daLarmFnioeF74qBHWPj9dUiplLOVZrMGqUhkK4T0aj1MU6yQ'
}

res = req.post(url=login,headers=header,data=data)  #登录请求
code=res.status_code


if code == 200:
    #发起新请求，获取目标
    res = req.get(url=url,headers=header)
    print(res)