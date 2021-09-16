'''
魔术方法和初始化方法
魔术方法：
    和普通方法一样也在类的成员中定义
    不需要手动调用的，魔术方法会在某种情况下自动触发（自动指向）
    特殊之处在于：多数的魔术方法前后都有两个下划线
    魔术方法不是自己定义的，系统定义好然后使用

__init__ 初始化方法
    通过实例化对象后，自动触发的方法
    作用： 可以在对象实例化后完成对象的初始化（属性赋值，方法调用）
    应用场景：文件的打开，数据获取。
'''

class Person():
    #成员属性
    name='wlf'
    age='12'
    sex='man'

    #__init__初始化方法
    def __init__(self,name,age):
        print("我是一个初始化方法")
        print(name,age)
        self.name = name      #属性赋值
        self.say()        #调用方法

    #成员方法
    def say(self):
        print(f'大家好，我是{self.name}')

wlf = Person('wlf',12)   #实例化对象时直接自动触发
print(Person('zz',11))