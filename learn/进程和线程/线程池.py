'''
固定线程总数
'''
import time,os,threading
from concurrent.futures import ThreadPoolExecutor

name_list = ['wlf','ldz','lsc','laoliu','qiaosang','yimou']
def call(name):
    print(f'打电话给{name},进程号{os.getpid()},线程号{threading.current_thread()}')
    time.sleep(2)
    print(f'{name}挂了电话,进程号{os.getpid()},线程号{threading.current_thread()}\n')

#创建线程池
pool = ThreadPoolExecutor(max_workers=3)   #只创建三个线程

#循环指派任务
for name in name_list:
    #指定对应任务数和参数
    pool.submit(call,name)

#关闭线程池
pool.shutdown(True)