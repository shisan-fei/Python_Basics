'''
三大特征：
    封装，集成，多态
封装：
    使用特殊语法，对成员属性和方法进行包装，达到保护和隐藏的目的。被封装的成员主要供内部使用
    封装是为了限制一些访问和操作，不能全部都限制
    被封装的成员只是限制了访问权限，并不是不让访问。通常情况下，被封装的成员供内部使用

    级别：
               共有的 public  :默认就是共有的    受保护的 protected    私有的 private
    在类的内部      可以                               可以                  可以
    类的外部        可以                               不可以（python可以）    不可以
    _new:受保护的类成员属性，在类的外部（python）可以操作。
    __new:私有的类的成员属性， 只有内部可以访问，外部不可以访问
'''
class Person():
    #成员属性
    name=None
    age=None
    sex=None
    _like='play'
    __shengao=170

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex = s

    def siyou(self):
        print(self.__shengao)  #在类的内部调用私有成员
    #成员方法
    def liaot(self):
        print('hahahah')

    def changge(self):
        print('songsang')

    def kiss(self):
        print('kiss')

ym = Person('ym','30','nu')

print(ym.name)
print(ym)
print(ym._like)   #在类的外部调用受保护的类的成员
#print(ym.__shengao)    #不能在类的外部调用类的私有成员
ym.siyou()

print(ym.__dict__)    #获取当前对象所有属性
print(ym.__dir__())   #获取对象所有信息
print(ym._Person__shengao)   #特殊方法访问私由成员属性