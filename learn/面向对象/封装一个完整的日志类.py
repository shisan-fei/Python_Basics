'''
日志类：
    class mylog
    功能：
        随时可以写入日志

分析：
    日志文件在哪？----> 默认在当前路径
    日志文件名？  ----> 当前日期
    日志中的数据格式？---> [日期 错误信息]

    属性：
        作用：存储信息给成员方法
            日志文件地址 fileurl
            日志文件名称 filename
            打开的文件对象  fileobj

    方法：
        __init__()    初始化方法，完成对象初始化，打开文件
        wlog()        接受用户给的日志信息并写入到文件中
        __del__()     对象销毁时，关闭文件
'''
import time
class wlogc():
    #属性
    fileurl = './'
    filename = time.strftime("%Y-%m-%daccess.log")
    fileobj = None

    #魔术方法，类实例为对象就会自动触发。打开一个文件。将文件对象赋值给fileobj
    def __init__(self):
        self.fileobj=open(self.fileurl+self.filename,"a+",encoding="utf-8")
        print('打开了文件')

    #定义一个类成员，一个写入方法。接收要写入的数据，写入文件
    def wlog(self,s):
        date = time.strftime('%Y-%m-%d %H-%M-%S')
        msg = date + s
        self.fileobj.write(msg + '\n')
        print(f'{msg}写入文件')

    #定义一个析构方法，在程序执行完之后，对象自动销毁,文件关闭。
    def __del__(self):
        self.fileobj.close()
        print("关闭文件")


writelog = wlogc()
writelog.wlog('写入一条日志')
