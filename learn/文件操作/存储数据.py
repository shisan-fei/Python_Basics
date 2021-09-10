import json
'''输入一个名字，将他存入文件name_txt'''
#
# username=input('please input you name:')
# with open('name_txt','w') as namefile:
#     json.dump(username,namefile)
#     print('you name:',username)
#
# '''从文件name_txt中读取名字'''
# with open('name_txt') as nameout:
#     youname=json.load(nameout)
#     print('hello:',youname)

'''使用异常处理当文件不存在时，让用户输入'''
try:
    with open('name_txt') as youname:
        username=json.load(youname)
except FileNotFoundError:
    name=input('please input you name:')
    with open('name_txt', 'w') as newname:
        json.dump(name,newname)
else:
    print('hello:'+ username)