'''
定义一个接口规范类，其他类继承这个类，并实现父类方法：
由于每个对象实现父类方法的方式或过程不同，最后结果不一样
'''
class USB():
    '''
    这个类就是一个接口规范类，子类继承并实现start方法
    start方法不做任何功能实现
    '''
    #定义一个规范接口，但不实现任何代码
    def start(self):
        pass

#定义鼠标类
class Mouse(USB):
    def start(self):
        print('鼠标启动')

#定义一个键盘类
class kB(USB):
    def start(self):
        print('键来')

#定义一个u盘类
class Upan(USB):
    def start(self):
        print('u盘已经插入')

#实例化对象
mouse = Mouse()
jianpan = kB()
upan = Upan()

#各个对象调用父类同一个方法
mouse.start()
jianpan.start()
upan.start()

