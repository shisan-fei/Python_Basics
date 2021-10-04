import requests

#请求url
url = 'https://www.baidu.com'
# url = 'https://www.baidu.com/sugrec'
#发起get请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
parars={
'prod': 'pc_his',
'from': 'pc_web',
'json': '1',
'sid': '34647_34443_34068_34552_34742_34584_34106_26350_34627_34419_34691_34681',
'hisdata': '[{"time":1632446088,"kw":"斗鱼校招都要提前实习吗"},{"time":1632471495,"kw":"sql insert插入多条"},{"time":1632533552,"kw":"gpa绩点满分多少"},{"time":1632536359,"kw":"华润银行招聘"},{"time":1632710874,"kw":"坦克300"},{"time":1632711017,"kw":"坦克300几座"},{"time":1632716573,"kw":"百度翻译api申请入口"}]',
'_t': '1633309902914',
'req': '2',
'csor': '0'
}
# res = requests.get(url=url,headers=headers,params=parars)
res = requests.get(url=url,headers=headers)
#获取响应结果
# print(res)            #---》<Response [200]>
# print(res.content)   #二进制文本流
# print(res.text)     #直接获取响应内容
# print(res.json())
# print(res.content.decode('utf-8'))     #将二进制文本流按照utf-8字符集转化为普通字符串,就相当于text
# print(res.headers)          #响应头信息
# print(res.status_code)    #请求状态码
print(res.url)        #请求的url
# print(res.request.headers)    #请求头信息


#找github上星级最高python项目
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# r = requests.get(url)
# print('status_code:',r.status_code)
#
# response_dict = r.json()
# print(response_dict.keys())
# print("total repositories:",response_dict['total_count'])