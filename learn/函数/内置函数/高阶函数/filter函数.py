'''
filter(func,interable)
功能：过滤数据
     把interable中每个元素拿到func函数中进行处理
        若函数返回Ture则保留，若返回False则丢弃
参数：
    func：自定义或内置函数
    interable：可迭代数据

返回值：保留下来的数据组成的迭代器
'''

#需求一  保留所有偶数 丢弃所有技术
list1 = [1,2,3,4,5,6,7,8,9]

#普通方法
oushu=[]
for i in list1:
    if i % 2 == 0:
        oushu.append(i)
print(oushu)

#使用filter过滤
def func(n):
    '''
    定义一个函数，判断n是基数还是偶数，基数返回False，偶数返回Ture
    :param n:
    :return:
    '''
    if n % 2 == 0:
        return True
    else:
        return False

res = filter(func,list1)     #使用filter函数过滤list1中数字
print(list(res),type(res))

#使用匿名函数优化
res1 = filter(lambda x:True if x%2==0 else False,list1)
print(list(res1))

