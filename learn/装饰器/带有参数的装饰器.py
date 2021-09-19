'''
带有参数装饰器：
    给原来的装饰器再套一层壳。外层函数接收装饰器的参数。
    并且接受的参数在壳内可以进行处理
'''
#给装饰器定义一个外壳，接收装饰器参数。
def ke(var):
    #如果你的装饰器需要有参数，那么给当前装饰器套个壳，用于接收装饰器参数。
    def outer(func):
        def inner():
            print('大街上相遇')
            func()
        def inner2():
            print('又遇到一个')
            func()
        #装饰器的壳参数，可以用于在函数内用于流程控制或其他用途
        if var == '两个人':
            return inner
        else:
            return inner2
    return outer


#@outer
@ke('三个人')    #ke()处理返回outer(),outer()将下方函数传入执行inner()或inner2()
def shuqing():
    print('谈人生')

shuqing()