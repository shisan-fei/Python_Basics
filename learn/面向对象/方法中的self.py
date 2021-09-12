'''
self在方法中代表形参，并不是关键字
self在方法中代表的是当前对象自己
self在方法中代表对象可以操作成员，可以使用self在类的内部访问成员
self 在类的方法中，代表当前这个对象
    代表调用这个方法的对象
若定义的方法中没有self，这个方法就不能被调用
'''

class Person():   #定义一个类person
    name = "姓名"
    age = '年龄'
    sex = "性别"

    def chang(self):
        print("会唱")

    def dunce(self):
        print("会跳")

    def rap(self):
        print(f'我是{self.name}')
        #print("会rap")

    def func(self):
        #测试在类的内部是否可以像在外部一样，访问操作
        # print(self)
        # print(self.name)
        # self.age = 21     #修改属性
        # print(self.age)
        self.rap()

    def func2():   #没有形参，绑定类方法，不接受对象参数方法，只能用类调用
        print("没有self")




#在类的外部访问类的成员和属性
cai = Person()
print(cai.age)
# cai.dunce()
cai.name='wlf'
cai.func()

Person.func2()