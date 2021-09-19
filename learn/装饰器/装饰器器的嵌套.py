'''
装饰器嵌套：
    先使用就近的装饰器，处理后将结果函数交给上一个装饰器处理。

'''
#定义装饰器，闭包函数+回调函数。
def outer(func):
    def inner():
        print('找人')
        func()
        print('go move')
    return inner

#再定义一个
def kuozhan(func):
    def shixian():
        print('new tool1')
        func()
        print('new tool2')
    return shixian

@outer  #使用装饰器装饰，添加新功能
@kuozhan
def love():
    print('play together')
love()

'''
同时使用两个装饰器时调用顺序：
    先使用就近的装饰器处理完后，将结果交给上一个装饰器处理最后输出：
    1. love函数交给kouzhan装饰器处理返回，函数shixian
                                    new tool1
                                    play together
                                    new tool2
    2. 将这个结果函数shixian交给outer装饰器处理，又再次添加功能。
'''