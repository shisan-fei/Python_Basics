'''
map()   map(func, *iterables)
      功能： 将传入的可迭代数据中每个元素放入函数中进行处理，返回一个新的迭代器
      参数：
          func：可自定义，可内置的
          iterable： 可迭代数据
      返回值： 迭代器
'''
#需求一：
#把一个字符串数字的列表转为 整型的数字列表
oldlist = ['1','3','2','5']   # 转换成[1,3,2,5]
newlist = []

#普通方法
for i in oldlist:
    newlist.append(int(i))
print(newlist)          #--->[1, 3, 2, 5]

#map函数实现
res = map(int,oldlist)    #将可迭代数据每个元素放到指定函数中处理
print(res)                #处理完后返回一个新的迭代器
print(list(res))          #使用list方法打印迭代器


#需求2    [1,2,3,4] ==> [1,4,9,16]


list2 = [1,2,3,4]
def pingfang(n):
    return n ** 2

res2 = map(pingfang,list2)
print(res2, list(res2))

#优化
res3 = map(lambda x:x ** 2,list2)
print(list(res3))


#需求3 ['a','b','c','d'] ==> [65,66,67,68]

list3 = ['a','b','c','d']
def func1(list3):
    list = []
    n=65
    for i in list3:
        list.append(n)
        n+=1
    return list

