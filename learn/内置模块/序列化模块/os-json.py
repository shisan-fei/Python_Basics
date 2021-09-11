'''
json
    轻量级数据交换格式
    在js语言中是一个对象表示方法，和python中字典定义规则和语法很像
功能：
    可以将一些符合转换的python数据对象，抓换为json
用法：
    dumps()
    loads()

    dump()
    load()
'''
import json
vardict = {"name":"wlf","age":"21","like":"sleep"}
varstr = 'asdfghj'              #只是转换为字符串
varlist = [1,2,3,45,5]

res = json.dumps(vardict)
print(res,type(res))            #{"name": "wlf", "age": "21", "like": "sleep"} <class 'str'>
print(vardict,type(vardict))    #{'name': 'wlf', 'age': '21', 'like': 'sleep'} <class 'dict'>

print(json.dumps(varlist))
print(json.dumps(varstr))

with open('data.txt','w') as fpw:    #将vardict转为json写入文件
    json.dump(vardict,fpw)

with open('data.txt','r') as fpr:
    data=json.load(fpr)
print(data)
