'''
类继承关系检测：
    类与类关系：
    类名.mro()   获取类的继承列表
    实现继承语法后，程序自动生成一个继承列表MRO(方法关系列表)。
    mro列表生成原则：子类永远在父类前边，对用同一等级的类按照继承顺序摆放，先子类后父类原则。最后object
issubclass(A,B) :检查A是不是B子类
'''
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

print(issubclass(B,A))   #检测B是不是A子类
print(issubclass(D,A))
print(issubclass(B,D))