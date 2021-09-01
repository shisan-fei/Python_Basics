'''
在内函数中如果想使用外层函数的变量，那么需要使用 nonlocal 关键字 引用
'''

def outer():    #定义一个外层函数
    num=10           #外函数局部变量
    def inner():        #内函数
        nonlocal num
        num+=1
        print(num)
    inner()

outer()