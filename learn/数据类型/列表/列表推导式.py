'''
基本列表推导式
    变量 = [变量处理 for i in 容器数据类型]
带条件判断列表推导式
    变量 = [变量或处理 for i in 容器数据类型 条件表达式]

'''

#需求1 创建一个平方列表
#普通方法
list1 = []
for i in range(10):
    res = i**2
    list1.append(res)

print(list1)

#map函数
pingf = map(lambda x:x**2,range(10))
print(list(pingf))

#使用列表推导式
list2 = [i**2 for i in range(10)]
print(list2)

#需求2 '1234' ----> [2,4,6,8]
strs='1234'
num = list(map(lambda n:int(n)*2,strs))
print(num)

num2 = [int(n)*2 for n in strs]
print(num2)

print([int(i) << 1 for i in strs])

#带条件的列表推导式
#求0-9所有偶数

print([i for i in range(10) if i % 2 == 0 ])

#带有多个条件判断的推导式
#[1,2,3] [3,8,7]   两列表中数组两两组合，组合的元素不重复
ll1 = [1,2,3]
ll2 = [3,8,7]
nn = [(i,n) for i in ll1 for n in ll2 if i != n ]
print(nn)


#九九乘法表
table = [[f'{i}*{n}={i*n}' for n in range(i,i+1) ] for i in range(1,10)]