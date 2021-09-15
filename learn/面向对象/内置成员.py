'''
内置成员：
    类定义好后系统自带的方法
    Demo.__dict__  获取当前类或对象所属成员
    Hello.__doc__   用来获取类的文档
    Hello.__name__   用来获取类名
    Hello.__module__  获取类所在文件名称，若是当前文件就显示为__main__
    Hello.__bases__   获取父类列表，继承的所有父类
    Hello.__base__    获取父类列表，继承的第一个列表
    Hello.__mro__    获取继承顺序
    hello.__dir__()   获取对象自带的方法
'''

class Demo():
    pass

print(Demo.__dict__)  #获取当前类所属成员
res = Demo()
print(res.__dict__)   #获取当前对象所属成员

class Hello(Demo):
    '''
    用来say一句hello
    '''
    def say(self):
        '''
        say方法的说明
        :return:
        '''
        print('hello word')

print(Hello.__dict__)
hello = Hello()
hello.say = 'say hello'
print(hello.__dict__)

print(Hello.__doc__)     #用来获取类的文档

print(Hello.__name__)    #用来获取类名

print(Hello.__module__)  #获取类所在文件名称，若是当前文件就显示为__main__

print(Hello.__bases__)   #获取父类列表，继承的所有父类
print(Hello.__base__)    #获取父类列表，继承的第一个列表
print(Hello.__mro__)     #获取继承顺序
print(hello.__dir__())   #获取对象自带的方法