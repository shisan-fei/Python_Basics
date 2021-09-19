'''
使用类装饰器装饰类：

'''
class Kuozhan():
    def __call__(self, cls):
        #把接收到的类赋值给当前对象，作为一个属性
        self.cls = cls
        #返回函数
        return self.newfunc

    def newfunc(self):
        self.cls.name = '新增属性name'  #添加一个属性
        self.cls.func2 = self.func2     #添加一个方法
        return self.cls

    def func2(self):
        print('新增一个方法 func2')


@Kuozhan
class Deamo():
    def func(self):
        print('i am Deam func ')

obj = Deamo()
obj.func()
obj.func2()