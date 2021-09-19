'''
__del__析构方法
    触发机制：当前类实例化的对象销毁时，自动触发。
    作用：可以在析构方法中完成特任务，如：关闭魔术方法打开的文件。
对象销毁
    程序执行完毕，对象销毁(内存中资源都被释放)
    使用del删除对象
    对象没有被引用，自动销毁

定义一个类，完成信息记录
    调用这个对象，传递日志信息
    这个对象会创建一个文件，开始写入，并在最后关闭文件
'''
import time

class writelog():
    #成员属性
    fileurl = './'   #文件路径
    filelog = str(time.strftime('%Y-%m-%d')+'-access.log')    #文件名
    fileobj = None

    #初始化，打开文件
    def __init__(self):
        print('文件已经打开')
        self.fileobj=open(self.fileurl+self.filelog,'a+',encoding="utf-8")

    #写日志
    def log(self,s):
        self.fileobj.write(f'把{s}写入文件')
        print('文件写入成功')

    #析构方法，对象销毁时，关闭文件
    def __del__(self):
        print("文件已关闭")
        self.fileobj.close()


log = writelog()
log.log("日志")   #魔术方法和析构方法都会调用，文件会打开和销毁
# del log
# writelog()     #直接执行初始化方法和析构方法，对象没有被引用
# print("test")


