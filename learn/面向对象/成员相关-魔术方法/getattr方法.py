'''
__getattr__
    触发：当访问对象中不存在成员时，自动触发
    作用：防止访问不存在成员时报错，为不存在成员进行赋值操作
    参数：一个self接收当前对象，一个item接收当前访问成员名称
    返回值：可有可无
    注意事项：存在__getattribute__时优先执行getattribute
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

zsf = Person('zsf',180,'man')
print(zsf.name)
print(zsf.mm)    #访问不存在方法时触发getattr方法
