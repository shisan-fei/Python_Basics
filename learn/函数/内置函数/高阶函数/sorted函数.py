'''
sorted()   sorted(iterable,[reverse,key])
       运行原理： 把可迭代数据元素一个个取出，放到key函数中处理，按照函数中return进行排序，返回一个新的列表。
       功能：    排序
       参数： iteranble 可迭代对象   （容器类型数据，range数据序列，迭代器）
             reverse    可选，是否反转，默认false 不反转 ture反转
             key     可选，函数，可以自定义函数，也可以是内置函数。
       返回值： 排序后的结果,一个列表
'''

list = [3,4,1,76,35,14,67]
list2 = [2,13,-6,-3,-29]

res = sorted(list)          #默认从小到大
res1 = sorted(list,reverse=True)   #从大到小
res2 = sorted(list2,key=abs)       #使用abs内置函数作为key，对数据绝对值操作

print(res)                 #--->[1, 3, 4, 14, 35, 67, 76]
print(res1)                #--->[76, 67, 35, 14, 4, 3, 1]
print(res2)                #--->[2, -3, -6, 13, -29] 将abs处理后的结果排序

#自定义一个函数作为key
def func(n):
    #print(n % 2)
    return n % 2

list3 = [57,4,6,35,24,64,85]
res3 = sorted(list3,key=func)              #--->对list3进行除2取余后进行排序
res4 = sorted(list3,key=lambda x:x%2)      #简单的函数直接使用匿名函数

print(res3)
print(res4,type(res4))
