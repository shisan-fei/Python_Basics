'''
yield关键字使用在函数中 与return相似
    共同点：执行到关键字后将值返回
    不同点：
        return：将结果返回，结束本函数
        yield：将结果返回，记住当前位置，一遍下次调用继续执行
生成器函数调用过程：
    调用生成器，返回一个迭代器
    1. 执行函数，遇到yield，将值返回，记住状态位置，暂停执行，等待下一次调用
    2. 从上一次遇到的yield位置开始执行，到下一个yield，返回值，记住位置，等待下一次调用
    ……


'''
#使用yield定义一个生成器函数
def hello():
    print('hello 1')
    yield 1
    print('hello 2')
    yield 2

#print(hello())      #--->返回一个迭代器<generator object hello at 0x000001BEC0DE9510>
#使用生成器返回的迭代器
res = hello()
# r = next(res)          #此时res就是一个迭代器，内容一个个读取出来---hello 1
# print(r)               #yield的返回值
# n = next(res)          #---->hello 2
# print(n)

#使用list调用生成器返回的迭代器时，会将迭代器的返回结果作为容器元素。
print(list(hello()))

#使用for读取迭代器
for i in hello():
    print(i)


#使用生成器函数改写斐波那契数列
#普通方法
def fibo(n):
    a,b,i=0,1,0
    while i < n:
        print(b,end=" ")
        a,b = b,a+b
        i+=1
fibo(10)
#使用递归函数
def digui(n):
    if n == 1 or n == 2:
        return 1
    else:
        return digui(n-1) + digui(n-2)
for i in range(1,11):
    print(digui(i),end=" ")

#生成器实现
def shengc():
    a,b,i=0,1,0
    while True:
        yield b     #创建一个生成器函数
        a,b=b,a+b
        i+=1

#res1 = shengc(10)     #调用生成器函数返回一个迭代器对象
#print(list(res1))     #使用list方法输出所有迭代器元素，就是生成器函数yield的返回值
n = int(input("请输入多少位dbnq"))
res = shengc()

for i in range(n+1):
    print(next(res),end=" ")