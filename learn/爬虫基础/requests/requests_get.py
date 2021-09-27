import requests

#请求url
url = 'https://www.baidu.com'

#发起get请求
res = requests.get(url=url)

#获取响应结果
print(res)
print(res.content)   #二进制文本流
print(res.text)     #直接获取响应内容
print(res.content.decode('utf-8'))     #将二进制文本流按照utf-8字符集转化为普通字符串
print(res.headers)          #响应头信息
print(res.status_code)    #请求状态码
print(res.url)        #请求的url
print(res.request.headers)    #请求头信息
