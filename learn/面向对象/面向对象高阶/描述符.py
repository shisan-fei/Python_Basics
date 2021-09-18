'''
描述符：
    当一个类中，包含了三个魔术方法之一时，这个类就是描述符类。
    三个魔术方法
        __get__
        __set__
        __delte__
    作用：
        对一个类中某个成员进行详细管理操作，获取修改删除
        描述符就是代理了一个类中成员操作，属于一个类。只能定义为类的属性
使用格式：
    把当前的描述符类赋值给需要代理的类成员属性
数据描述符：
    同时又三个魔术方法，就是数据描述符
'''
#定义一个描述符类
class PersonName():
    __name = 'wlf'

    def __get__(self, instance, owner):
        print(self,instance,owner)
        return self.__name            #有返回允许成员获取

    def __set__(self, instance, value):
        print(self,instance,value)
        self.__name = value           #允许修改

    def __delete__(self, instance):
        compile(self,instance)
        #del self.__name
        print('允许删除')

#定义一个普通类
class Person():
    '''
    将类的成员属性交给描述符类实现
    一个类中成员的值，是另一个描述符的对象
    当对这个类中成员进行操作时就是对另一个类的操作
    '''
    name = PersonName()   #代替name去获取值

#实例化一个类
mi = Person()
print(mi.name)  #通过对象获取成员

mi.name = 'hhaha'
print(mi.name)

del mi.name
#print(mi.name)

