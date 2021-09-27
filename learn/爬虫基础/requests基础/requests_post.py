import requests

# url='https://fanyi.baidu.com/langdetect'  #抓取的百度翻译post地址
endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/vip/translate'
url = endpoint + path
#定义请求头
header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded'
}

#要发送的数据
data = {'kw':'你好'}
#发送请求
res = requests.post(url=url,headers=header,data=data)

code = res.status_code
if code == 200:
    print('请求成功')
    data = res.json()
    # if data['errno'] == 0:
    #     print('响应成功')
    #     k=data['data'][0]['k']
    #     v = data['data'][0]['v'].split(':')[-2]
    #     print(k,'====',v)
print(res.json())