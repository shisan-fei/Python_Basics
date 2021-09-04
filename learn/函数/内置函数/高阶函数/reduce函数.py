'''
reduce(func,*iterable)
功能：
    每次从iterable中拿出两个元素，放到func中进行处理，得到结果
    然后将结果和第三个元素放到func中计算，然后得到新的结果。
    然后依次将结果和后一个元素做相同的操作，知道元素完
参数：
    func：内置函数或自定义函数
    iterable： 可迭代数据

返回值：最后函数处理结果
注意：reduce需要导入from functools import reduce
'''
from functools import reduce

#需求1  [5,2,1,1] ==> 5211
#普通方法
list1 = [5,2,1,1]
a = ''
for i in list1:
    a+=str(i)

print(int(a))

#使用reduce函数
def func(x,y):
    return x * 10 + y

print(reduce(func,list1))


#需求2 '456' --- > 456
def func2(s):
    '''
    给一个字符串数字，返回整型数字
    :param s:
    :return:
    '''
    dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return dict[s]

iter1 = map(func2,'456')    #使用map函数，让func2函数处理‘456’。转成一个数字列表[4, 5, 6]
#print(list(iter1))

iter2 = reduce(lambda i,n:i*10+n,iter1)   #使用reduce函数，将iter1元素两两传入匿名函数，返回数据
print(iter2)
