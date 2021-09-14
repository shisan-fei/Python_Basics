'''
多态：
    对于同一种方法，由于调用方法的对象不同，产生不同形态的结果
    定义一个类的接口规范类，
'''
class Compute():
    #定义一个usb方法
    def usb(self,obj):
        obj.start()

#定义一个鼠标类
class Mouse():
    def start(self):
        print('启动鼠标')

#定义一个键盘类
class kB():
    def start(self):
        print('键来')

#定义一个u盘类
class Upan():
    def start(self):
        print('u盘已经插入')

diannao = Compute()
shubiao = Mouse()
jianpan = kB()
upan = Upan()

#将不同设备插入usb接口。启动
diannao.usb(shubiao)   #不同对象调用同一种方法，产生不同效果
diannao.usb(jianpan)
diannao.usb(upan)
