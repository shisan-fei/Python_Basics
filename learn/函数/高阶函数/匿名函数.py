'''
lambda表达式
匿名函数： 就是说可以不使用def定义，并且这个函数也有没有名字
         可以使用lambda表达式，

注意：lambda表达式仅仅是一个表达式，不是一个代码块，所以lambda又称为一行代码的函数
       lambda表达式也有行参，并且不能访问除了自己的行参之外的任何数据包括全局变量

语法：lambda【参数列表】：返回值
'''

#例一：
#封装一个加法函数
def jiafa(i,n):     #普通函数
    return i+n
print(jiafa(2,2))

ras=lambda x,y:x+y   #匿名函数
print(ras(4,3))


#例二：
#带分支结构
def panduan(persion):         #普通函数
    if persion == '男':
        print('man')
    else:
        print('nv')

panduan('男')

#  lambda 参数列表: 真区间 if 表达式判断 else 假区间
res = lambda persion:'man' if persion == '男' else 'nv'         #匿名函数
print(res('nv'))