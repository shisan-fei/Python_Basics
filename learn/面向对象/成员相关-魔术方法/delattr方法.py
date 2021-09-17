'''
__delattr__
    触发：删除对象成员时触发
    作用：限制对象成员触发，还可以删除不存在成员时防止报错
    参数：self接收当前对象 item删除的成员名
    返回值：无
    注意事项：在当前魔术方法中进制删除成员对象，会递归触发
            object.__delattr__(self,item) 这样删除
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

  #删除成员对象时自动触发
    def __delattr__(self, item):   #有了delattr方法后，普通方法不能直接删除
        print(item)
        object.__delattr__(self,item)   #现在才可以删除


zsf = Person('zsf',180,'man')
del zsf.name   #一般可以直接删除
print(zsf.name)
