a=10

def sum():
    b=20
    print(a)
    global d #函数内定义全局变量
    d=20
    print(locals())


sum()
print(a+d)
print(globals())   #所有全局变量
print(locals())    #所以局部变量