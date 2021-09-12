'''
一个对象通过类实例化后，那么在类中定义的属性和方法可以在实例化后的对象中使用。
可以通过对象修改，添加，删除 类中的属性
    访问：对象.成员属性名
    修改：对象.成员属性名 = 新的值
    添加：对象.成员属性名 = 值 （给该对象新建一个属性）
    删除： del 对象.成员属性名  只能删除该对象的属性

'''
class Cart():
    #属性，就是变量
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

#一个类可以实例化多个对象
a = Cart()   #a,b都是通过同一个类实例化来的对象，
b = Cart()
print(a,b)

#对象成员的操作，调用类中的属性，先访问a自己有没有该属性，再访问类
print(a.color)   #调用属性
a.laren()        #调用方法

#修改类中属性
a.color = '红色'
print(a.color)
print(b.color)    #b对象的属性不变

#给类添加属性，这个属性只属于该对象
a.name='牧马人'
print(a.name)     #a对象会成功获取属性
#print(b.name)     #没有，会报错

#删除类中属性，这能删除当前对象的属性，只能删除自己添加或修改的属性
#del a.name
#del a.pail     #不能删除，pail属于类的
#print(a.color)

'''
在类外部操作对象方法
访问对象的方法：若对象没有自己独立的方法，就会访问这个对象的类的方法
              创建对象时，并不会吧类中的属性和方法复制一份给对象，而是引用
可以修改，添加，删除类方法
    对象创建后，对对象的类的修改，添加，删除就等于给对象创建了一个自己的属性和方法。
    所以删除时，只能删除对象修改或添加的成员
'''
#访问方法
a.laren()

#修改对象方法
def newlaren():
    print("可以拉5个")
a.laren = newlaren()
a.laren

#添加新方法
a.laren2=newlaren()
a.laren2

#删除方法
del a.laren2
#del a.lahuo()   #类的方法不能删除
#a.laren2

