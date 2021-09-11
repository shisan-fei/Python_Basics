import time
'''
time()   获取系统当前时间戳
ctime()  获取当前时间
localtime() 获取时间元祖
strftime()  格式化时间
sleep(秒数)  在给定时间内暂停线程
'''
print(time.time())
print(time.ctime())    #--->Sat Sep 11 17:31:02 2021
print(time.localtime())


#localtime获取的时间格式化 xx年xx月xx日
res = time.localtime()
print(f'{res.tm_year}年{res.tm_mon}月{res.tm_mday}日{res.tm_hour}时')

print(time.strftime('%Y-%m-%d-%H-%M-%S-%w'))     #2021-09-11-17-58-22-6
time.sleep(5)
print(time.strftime('%Y-%m-%d-%H-%M-%S-%w'))     #2021-09-11-17-58-27-6