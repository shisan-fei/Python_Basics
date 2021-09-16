'''
issubclass(D,B)        检测D类是不是B类子类
isinstance(对象,类)     检测一个对象是否是该类实例化对象
hasattr(类或成员,成员))  检测类或成员是否有指定成员，私有成员无法检测（访问不到的检测不到）
getattr(d,'_like')     获取对象成员的值
setattr(d,'age',21)    设置对象成员的值
delattr(D,'_like')     删除对象或类的成员  和del._like效果一样
dir(d))                获取当前对象所有可以访问成员列表
'''

class A():
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    name = 'wlf'
    age = 12
    _like = 'play'
    __hight=170
    pass

print(issubclass(D,B))

d = D()
print(isinstance(d,D))
print(hasattr(D,'name'))   #查看name成员是否在D类中

print(getattr(d,'_like'))   # print(d.age)效果一样
setattr(d,'age',21)        #   d.age = 20效果一样
print(getattr(d,'age'))

delattr(D,'_like')       #删除对象或类的成员
#print(d._like)

print(dir(d))   #获取当前对象所有可以访问成员列表

