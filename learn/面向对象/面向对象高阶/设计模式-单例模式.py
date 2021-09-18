'''
单例(单态)设计模式：
    在当前脚本中，一个类只能创建一个对象使用，叫做单态。
实现：
    1. 需要一个方法，控制当前对象创建过程。
        __new__ 构造方法
    2. 需要一个标识，检测是否有对象
        创建一个属性，存储，默认返回none
    3. 在创建对象方法中，检测和判断是否有对象？
        若没有对象就创建对象，并把对象存储进来
        若有对象了，就不创建对象了



'''
# class Deam():
#     #定义属性存储对象，默认none.属性要私有的
#     __obj = None
#     #定义一个构造方法
#     def __new__(cls, *args, **kwargs):     #cls就是类名，
#         #创建对象过程中，判断是否有对象
#         if cls.__obj:            #判断当前类的__obj属性是否为空，不为空就返回对象
#             return cls.__obj
#         else:
#             #没有对象时创建并存储
#             obj = object.__new__(cls)  #创建对象
#             cls.__obj = obj            #存储对象
#             return obj                 #返回对象
#
# deam = Deam()    #一般情况下，一个类可以实例化多个对象
# deam2 = Deam()
# print(deam,deam2)   #现在不论创建多少个对象都是同一个


#代码优化
class Deam():
    #定义属性存储对象，默认none.属性要私有的
    __obj = None
    #定义一个构造方法
    def __new__(cls, *args, **kwargs):     #cls就是类名，
        #创建对象过程中，判断是否有对象
        if not cls.__obj:
            cls.__obj=object.__new__(cls)
        return cls.__obj

deam = Deam()    #一般情况下，一个类可以实例化多个对象
deam2 = Deam()
print(deam,deam2)   #现在不论创建多少个对象都是同一个