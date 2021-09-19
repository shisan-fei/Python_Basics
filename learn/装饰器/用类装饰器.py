'''
类装饰器：
    使用类名获取装饰器，相当于将类实例化为对象
    使用__call__方法将对象作为函数调用，返回一个装饰器方法。
    再定义一个用来装饰的方法单独进行装饰

'''
class Outer():
    #__call__方法：当把该类对象当做函数调用时自动触发
    def __call__(self, func):
        self.func = func       #将传进来的函数作为对象成员
        return self.inner

    #定义需要返回的新的方法，进行装饰处理
    def inner(self,name1):
        print('大街相遇')
        self.func(name1)
        print('回家')


'''Outer类实例化一个对象obj   obj---》obj(love)把对象当做函数调用，将love函数作为参数传入
__call__(love) 返回类中inner方法
'''
@Outer()
def love(name1):
    print(f'{name1}和李白对诗')

love('wlf')    #相当于调用类中inner方法