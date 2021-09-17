'''
成员相关魔术方法：
    __getattribute__
    触发：当访问对象成员时自动触发，无论当前成员是否存在
    作用： 获取对象成员时，对数据进行处理
    参数： self接收对象，一个item接收当前访问成员名称
    返回值：可有可无，返回的值就是访问的结果
    注意：在当前魔术方法中，禁止使用对象.成员方式访问会递归触发
            如果要在当前魔术方法中访问对象成员必须使用object.__getattribute__访问

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
    #获取对象成员是自动触发
    def __getattribute__(self, item):
        #通过hasattr判断是否存在属性
        try:
            print(item)            #传入的属性名
            print(object.__getattribute__(self,item))   #获取属性
            res = object.__getattribute__(self,item)
            return res[0]+'*'+res[2]   #在方法中对访问成员属性修改
        except:
            return '不是name'
        #return 'abc'

# wlf = Person()
# wlf.say()

zsf = Person('zsf',180,'man')
print(zsf.name)
