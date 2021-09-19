'''
带有参数的函数装饰：
    带有一个参数：
    原函数有一个参数，对迭代器内函数也传入一个参数。实质就是内函数执行了原函数。

    带有多个参数函数：
    同样将多个参数传入内函数中
'''
#对带有一个参数的函数进行装饰
def outer(func):
    #若装饰带有参数的函数，需要在内函数中定义，并传递给调用的函数。因为装饰器实质就是调用内函数完成。
    def inner(var):
        print('找到人了')
        func(var)
        print('一起吃饭')
    return inner

#定义一个有参数的函数
@outer
def love(name):
    print(f'和{name}畅谈')

love('libai')   #此时指向原函数实质就是执行inner函数，传入参数name---->执行inner(var)函数

print('上边一个参数，下边多个参数'.center(90,'#'))

#对带有多个参数的函数进行装饰
def outer2(func):
    def innter(n1,n2,*args,**kwargs):    #同样在内函数中指定想用数量的参数，接收原函数
        print('二人相遇')
        func(n1,n2,*args,**kwargs)
        print('后会有期')
    return innter

#定义一个带有多参数的函数
@outer2
def liaotian(name1,name2,*args,**kwargs):
    print(f'{name1}和{name2}畅谈天地')
    print('一起吃饭',args)
    print('观看焰火',kwargs)

liaotian('duanyu','wanggirl','糕点','水果',mov='万人篝火',zashua='喷火，走钢丝')

