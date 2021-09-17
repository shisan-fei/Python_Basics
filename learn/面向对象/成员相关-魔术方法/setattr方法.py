'''
__setattr__
    触发：给对象成员进行赋值（添加修改）时自动触发.
    作用：限制管理对象成员的添加修改操作
    参数：self  接收当前对象，
         key  设置成员名
              设置的成员值
    返回值：无
    注意事项：在当前魔术方法中禁止给当前对象成员直接进行赋值操作，会触发递归操作
            使用object.__setattr__
'''
class Person():
    name = '姓名'
    age = '年龄'
    sex = '性别'

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.sex =s

    def say(self):
        print('聊天')

    def sing(self):
        print('唱歌')

    #访问不存在成员时自动触发
    def __getattr__(self, item):
        print(item+'不存在')
        return False

    #给对象成员赋值自动触发，该方法中没有给对象成员赋值，那么对象成员赋值失败
    def __setattr__(self, key, value):
        print(self,key,value)
        object.__setattr__(self,key,value)   #现在就能赋值成功了

zsf = Person('zsf',180,'man')
print(zsf.abc)
zsf.abc = 'abc'
print(zsf.abc)