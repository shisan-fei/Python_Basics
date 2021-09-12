'''
要实例一个对象，就需要先抽象一个类
要创建一个汽车对象，就得抽象一个汽车类（相当于一个设计图纸），由这个类去创建汽车对象
定义一个汽车类
    使用class定义类
    类名命名：使用驼峰命名法。MyCart  XiaoMi
    内容：
        特征：一个描述，例如：颜色，大小……
        功能：一个能力，例如：拉人，拉货……
        特征在编程就就是变量，在类中就是属性
        功能在编程中就是一个函数，在类中就是方法
    类中属性一般在最前
'''
class Cart():
    color = '白色'
    brand = 'jeep'
    pail = '3.0'

    #定义方法，就是函数，实现功能
    def lahuo(self):
        print('拉货')

    def laren(self):
        print("拉人")

    def douf(self):
        print('兜风')
#使用类，通过类实例化对象
jeep = Cart()
print(jeep,type(jeep))    #---><__main__.Cart object at 0x0000017A8B76EFD0> <class '__main__.Cart'>
#通过对象调用方法
jeep.douf()
jeep.laren()
