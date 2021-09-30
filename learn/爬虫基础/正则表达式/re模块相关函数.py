'''
相关函数：
    re.findall(正则，字符串) ：查找匹配到的所有字符，返回一个列表。
    re.finditer(正则，字符串) :返回一个迭代器
    re.match() :
        从头开始匹配，要
        么第一个符合，要么不符合
        成功就返回match对象,否则返回none ---- <re.Match object; span=(0, 4), match='love'>
        使用re.match().group()返回匹配到的数据
        re.match().span()返回匹配到的下标
    re.search()
        与match不同的是search会从头到尾匹配，match只会匹配开始
    re.sub(正则，替换后的字符串，字符串)
        匹配到字符，完成替换。
compile()
    可以将正则表达式定义为正则对象，使用正则对象直接操作。
正则：
    \d 一个数字
'''

import re
var = 'loveyou521simida22'

# res = re.findall('\d',var)    #--->['5', '2', '1']
# print(res)
#
# res1 = re.match('love',var).group()  #返回匹配到的字符
# print(re.match('love',var).span())  #返回下标

print(re.search('\d',var))
print(re.search('\d{3}',var).group())   #'\d{3}'匹配三个数字
print(re.search('\d',var).span())

#找到数字替换成tt
newvar=re.sub('\d{3}','tt',var)
print(newvar)

#直接创建正则对象，用于复杂结构正则匹配字符串
res=re.compile('\d{3}')
print(res.findall(string=var))
print(res.search(string=var).group())