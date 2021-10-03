
import time
from multiprocessing import Process   #进程
import os
import threading
from threading import Thread    #线程

name_list = ['wlf','ldz','lsc','laoliu','qiaosang','yimou']
def call(name):
    print(f'打电话给{name},进程号{os.getpid()},线程号{threading.current_thread()}')
    time.sleep(2)
    print(f'{name}挂了电话,进程号{os.getpid()},线程号{threading.current_thread()}\n')

#普通方法，循环单进程，单线程完成
# for i in name_list:
#     call(i)

# if __name__ == '__main__':
#使用多进程
    # plist = []
    # for name in name_list:
    #     #循环创建进程
    #     proce = Process(target=call,args=(name,))
    #     #生成进程
    #     proce.start()
    #     #把进程写入列表
    #     plist.append(proce)
    # #阻塞终止线程
    # for i in plist:
    #     i.join()

#使用多线程
thlist = []
for name in name_list:
    th = Thread(target=call,args=(name,))
    th.start()
    thlist.append(th)
for i in thlist:
    i.join()
