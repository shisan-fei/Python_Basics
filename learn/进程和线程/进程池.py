from concurrent.futures import ProcessPoolExecutor
import os
import threading
import time


name_list = ['wlf','ldz','lsc','laoliu','qiaosang','yimou']
def call(name):
    print(f'打电话给{name},进程号{os.getpid()},线程号{threading.current_thread()}')
    time.sleep(2)
    print(f'{name}挂了电话,进程号{os.getpid()},线程号{threading.current_thread()}\n')

if __name__ == '__main__':
    pool = ProcessPoolExecutor(max_workers=3)   #创建进程池
    for name in name_list:
        pool.submit(call,name)     #指定函数和参数
    pool.shutdown(True)           #关闭进程池