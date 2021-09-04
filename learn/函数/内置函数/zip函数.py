'''
功能：可接受多个可迭代对象，吧每个可迭代对象中第i个元素组合成一起，组合成迭代器。
参数：*iterables, 任意的，可迭代对象
返回值：一个元祖迭代器
'''

from collections.abc import Iterator,Iterable

v1 = [1,2,3,4]
v2 = ['a','b','c','d']
v3 = 'asdf'

#调用zip，组成新的元祖迭代器
res = zip(v1,v2,v3)

#提取迭代器
print(next(res))

#print(list(res))

for i in res:
    print(i,end=" ")

#判断是否为迭代器
r1 = isinstance(res,Iterable)
r2 = isinstance(res,Iterator)
print(r1,r2)

# zip() 与 * 运算符相结合可以用来拆解一个列表:
x = [1,2,3]
y = [4,5,6]
zipapp = zip(x,y)   #生成一个迭代器

#print(zip(*zip(zipapp)))
print(list(zipapp))   #[(1, 4), (2, 5), (3, 6)]

x2,y2 = zip(*zip(x,y))
print(x2,y2)          #将zip组成的迭代器又拆开返回，返回的是元祖。