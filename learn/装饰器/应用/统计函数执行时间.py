'''
统计函数执行时间：

'''
import time
#定义一个统计函数执行时间装饰器
def count_time(f):
    def inner():    #在内函数中实现要添加的功能
        start = time.perf_counter()
        f()
        stop = time.perf_counter()
        count = stop - start
        print(f'\n耗时{count}')
    return inner

@count_time     #使用定义的装饰器
def func():
    for i in range(3):
        print(i,end=" ")
        time.sleep(1)
func()