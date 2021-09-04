'''
迭代器：是访问集合元素的一种方式，是一个可以记住访问编历位置的对象（Iterator 迭代器对象）
       第一个元素开始访问，直到集合中的所有元素被访问完毕
       只能从前往后一个一个的遍历，不能后退

      iter()：吧可迭代对象，转化为一个迭代器对象
             参数：可迭代对象---str list dict tuple set range
             返回值：迭代对象
             注意：迭代器一定是可迭代对象，但可迭代对象不一定是迭代器
      取值方式：
            next(): 调取一次，取一个，知道取完
            list()：直接取出迭代器中所有数据
            for: 循环编历迭代器
            特点： 不管哪个都是取出一个少一个，知道取完。
      检测迭代器和可迭代对象的方法：
                from collections.abc import Iterator,Iterable
            isinstance() ；检测一个数据是否为一个指定对象
'''

#检测是否为可迭代对象或者是迭代器
from collections.abc import Iterator,Iterable
strvar='asdfghjkl'
diedai = iter(strvar)

r1 = isinstance(strvar,Iterable) #是否为可迭代对象 返回Ture就是
r2 = isinstance(diedai,Iterator) #是否为迭代器，返回True就是


print(r1,r2)

#定义一个列表，一个可迭代对象
f4=['zhaosi','liuneng','songxiaobao','xiaoshenyang']

#使用for编历
# for i in f4:
#     print(i,end=" ")

#吧迭代对象转换为迭代器
res = iter(f4)
print(res,type(res))

#使用next函数调用迭代器对象
print(next(res))        #每次取一个
print(next(res))
# print(next(res))
# print(next(res))
#print(next(res))   #超出迭代器范围 StopIteration

#使用list（）获取
print(list(res))

#使用for循环
for n in res:
    print(n)

r3 = isinstance(res,Iterable)
r4 = isinstance(res,Iterator)
print(r3,r4)