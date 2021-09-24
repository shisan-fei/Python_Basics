'''
三种方式：
    1. 定义描述符类实现（常用）
    2. property函数在需要管理的类中直接定义函数操作
            property函数中参数依次设置为__get__,__set__,__delete__
    3. 使用property装饰器定义描述符
'''

# #方法一
class ScoreManage():
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass
class Student():
    score = ScoreManage

#方法二，使用property函数
class Student():
    #在当前需要管理的类中直接定义函数方法完成修改
    def getscore(self):
        print('获取score')
    def setscore(self,value):
        print('修改score',value)
    def delscore(self):
        print('删除score')
    #在函数中指定三个方法,
    score = property(getscore,setscore,delscore)

zsf = Student()
print(zsf.score)
zsf.score = 100
print(zsf.score)

#方法三 使用@property装饰器语法来实现
class Stutent():
    __score = None
    @property
    def score(self):
        print('get,来获取值')
        return self.__score
    @score.setter
    def score(self,value):
        print('set，来修改值')
        self.__score = value

    @score.deleter
    def score(self):
        print('delete,来删除值')
        del self.__score

zsf = Stutent()
print(zsf.score)

zsf.score = 100
print(zsf.score)

del zsf.score