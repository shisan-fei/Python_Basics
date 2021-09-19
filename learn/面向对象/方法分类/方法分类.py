'''
方法的分类：
    对象方法
        特征：在类中定义的方法，含有self参数
            含有self的方法，只能使用对象调用
            会把调用的对象传入
    类方法
        在类中定义的方法，使用装饰器@classmethod进行装饰
        方法中有cls这个形参，不需要实例化对象直接调用
        会把调用这个方法的类传递进来
    绑定方法
        在类中定义方法
        只能使用类进行调用
        不会传递任何对象或对象进来
    静态方法
        在类中定义方法，使用装饰器@staticmethod进行装饰
        可以使用类和对象调用
        不会传递对象或类进来
'''

class Deam():
    #对象方法：
    def func1(self):
        print(self)
        print('this is func1')

obj = Deam()
obj.func1()
#Deam.func1('a')    #不能用类来调用方法，需要传递任意参数

#类方法
class Deam2():
    @classmethod
    def func2(cls):
        print(cls)
        print('this is func2')

Deam2.func2()   #可以使用类进行调用
obj2 = Deam2()
obj2.func2()    #用方法调用还是传入的是类

#绑定类方法
class Deam3():

    def func3():
        print('this is func3')

Deam3.func3()   #直接使用类调用
obj3 = Deam3()
#obj3.func3()    #不能用对象获取

#静态方法
class Deam4():
    @staticmethod
    def func4():
        print('this is func4')

Deam4.func4()
obj4 = Deam4()
obj4.func4()