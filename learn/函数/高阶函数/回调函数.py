'''
回调函数：函数的参数是一个函数，并且调用了传递进来的函数。
'''

def func(n):
    print(n,type(n))

def love():
    print("i lohu you")

#func(love())   #将love函数作为参数传递给func函数。


def jisun(x,y,z):
    '''
    接受xy传递给z函数进行处理
    :param x:
    :param y:
    :param z:  一个函数
    :return:
    '''
    print(z([x,y]))

jisun(1,2,sum)    #将1,2穿入sum函数运算
print(sum([1,3]))   #sum用法