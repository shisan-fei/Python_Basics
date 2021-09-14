'''
单继承：
    一个类只能继承一个父类
    一个父类能被多个子类继承,可以存在链式继承
class 父类():
    pass
class 子类(父类)：
    pass

多继承：
    一个类继承多个父类
class 父类():
    pass
class 母亲():
    pass

class 子类(父类,母亲)：
    super().父类方法()   #调用时从mro列表找上一个类，会将当前self传入上以及类方法
    pass

菱形继承，钻石继承
        A           zuxian
    B       C    F          M
        D             son
D继承了B和C，B和C又同时继承了A。
类与类关系：
    类名.mro()   获取类的继承列表
    实现继承语法后，程序自动生成一个继承列表MRO(方法关系列表)。
    mro列表生成原则：子类永远在父类前边，对用同一等级的类按照继承顺序摆放，先子类后父类原则。最后object
'''
class zuxian():
    num = 1
    def eat(self):
        print(self.num)
        print('烧烤')

class F(zuxian):
    num = 2
    def eat(self):
        super().eat()
        print(super().num)
        print('大口吃')


class M(zuxian):
    num = 3
    def eat(self):
        super().eat()
        print(super().num)
        print('小口吃')

class son(F,M):
    num = 4
    def eat(self):
        super().eat()          #多继承中父类方法调用
        print(super().num)
        print('吃玩吃')

mi = son()

mi.eat()
print(son.mro())