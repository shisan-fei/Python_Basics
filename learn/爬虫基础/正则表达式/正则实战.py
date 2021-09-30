'''
数据地址：https://www.lmonkey.com/t?category=aGy1J2LvZ
数据字段：问题。时间。作者
'''
import requests,re,json

url = 'https://blog.csdn.net/nav/ops'

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
res = requests.get(url=url,headers=headers)
if res.status_code == 200:
    #获取返回的数据
    html_get = res.text
    # with open('test.html','w',encoding='utf-8') as fp:
    #     fp.write(html_get)
    #数据解析
    rex = '(.*?)                                                    </a>'
    titles=re.findall(rex,html_get)
    title_list = [i.strip() for i in titles]

    rex2 = '''                        <a href="https://blog.csdn.net/weixin_(\d*)" target="_blank">
                            (.*?)                        </a>'''
    getauth=re.findall(rex2,html_get)
    auth_list = [i[1] for i in getauth]

    datas = zip(title_list,auth_list)
    # print(list(datas))

    data_list = [f'文章：{i[0]} 作者：{i[1]}' for i in datas]
    print(data_list)

    #写入文件
    # with open('last.txt','w',encoding='utf-8') as fp:
    #     fp.write(data_list)
        #json.dump(data_list,fp,indent=2,sort_keys=True)




