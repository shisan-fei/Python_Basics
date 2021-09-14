'''
继承：
    一个类继承父类，就会拥有父类所有成员 除过私有成员
    被其他类继承：父类，基类，超类
    继承其他类：子类，派生类
        子类可以访问父类成员，可以自己定义，修改父类成员（重写）
        子类可以有自己的成员也可以没有。（可扩展）
        可以在子类中调用父类方法
    一个子类可以被多个子类继承
在不指定父类时，自动继承object类（系统指定）
继承的意义：
    提高代码重用性，建立类与类的关系，方便其他逻辑操作
语法：
    class 父类():
        pass

    class 子类(父类):
        pass
'''
class maoke():
    #属性
    maose = '纹理'
    huzi = '三根'

    def pao(self):
        print('猫步')

    def pashu(self):
        print("上树")

class tiger(maoke):   #老虎类继承了maoke类
    maose = '王'      #对父类属性重写

    def chiren(self):    #子类自己定义方法
        super().pashu()  #调用超类方法
        print('吃人')
    pass

class baozi(maoke):
    pass

dongbeihu = tiger()
#可以访问maoke类的成员，现在tiger的成员，没有的话就找maoke类
dongbeihu.pao()     #调用父类方法
dongbeihu.chiren()  #调用子类自己的方法
print(dongbeihu.maose)


xiaoliebao = baozi()
print(xiaoliebao.huzi)