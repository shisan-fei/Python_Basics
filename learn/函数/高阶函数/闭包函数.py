'''
闭包函数：在一个外函数内返回了一个内函数， 并且这个返回的内函数还使用了外函数中局部变量，这就是闭包函数
特点：
    1. 在外函数中定义了局部变量，并且在内部函数中使用了这个局部变量
    2. 在外函数中返回了内函数，返回的内函数就是闭包函数
    3. 主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏
    4. 检测一个函数是否为闭包函数，可以使用 `函数名.__closure__ `如果是闭包函数返回 cell
'''

def person():
    money = 0        # 函数中定义了一个局部变量

    #工作,定义一个内函数
    def work():
        nonlocal money          # 在内函数中使用了外函数的临时变量
        money+=100
        print(money)
    return work               # 在外函数中返回了内函数，这个内函数就是闭包函数

    # #加班
    # def over():
    #     nonlocal money
    #     money+=200
    #
    # #购物
    # def shopping():
    #     nonlocal money
    #     money-=100

rsa = person()
rsa()     #res() == work()
rsa()
rsa()
# 此时 就不能够在全局中对money这个局部变量进行任何操作了，
print(rsa.__closure__)    #检查是不是闭包函数