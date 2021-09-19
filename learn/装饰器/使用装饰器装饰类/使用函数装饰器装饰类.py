'''
装饰器给函数装饰：
    目的是不改变函数的代码和调用，给原函数增加新的功能
装饰器给类进行装饰：
    目的是不给类增加新的成员，不改变代码增加新的功能

'''

#使用函数装饰器给类进行装饰
#定义一个函数，接收一个类，返回修改后的类
def outer(cls):
    def innter():
        print('新增功能')
    cls.innter = innter                   #给类新增一个方法
    cls.name = '我是在装饰器中追加的新属性'   #给类新增一个属性
    return cls

@outer
class Deamo():
    def func():
        print('i am Deam func ')


Deamo.func()
Deamo.innter()
print(Deamo.name)