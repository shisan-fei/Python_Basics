'''
range()函数
功能：能够生成一个指定的数字序列
参数：   range(start,stop,[,step])
    start : 开始的值 ，默认值为0
    stop  ： 结束的值
    [, step]： 可选，步进值 默认值为1
返回值： 可迭代的对象，数字序列
'''

res = range(10)

print(list(res))
print(list(range(10,5,-1)))

for i in res:
    print(i,end=" ")