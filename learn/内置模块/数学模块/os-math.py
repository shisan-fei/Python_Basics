'''
内置模块
    round()  四舍五入
'''
import math

'''
ceil()  向上取整
floor()  向下取整
pow(x,y)  计算数值n次方，结果是浮点数.x的y方
sqrt(x)   开平方运算
fabs()  计算绝对值
modf()  将一个数值拆分成整数和小数组成的元组
copysign() 把第二个参数的正负符号给第一个元素
fsum()  将容器类型数据求和
'''

print(math.ceil(2.25))   #3
print(round(2.25))       #2 四舍五入

print(math.floor(2.55))   #2
print(math.pow(2,8))      #2的8次方256.0

print(math.sqrt(9))      #3

print(math.fabs(-100),abs(-100))   #100.0 100

print(math.modf(3.14))    #(0.14000000000000012, 3.0)

print(math.copysign(3.14,-10))

print(math.fsum([1,2,3,4,5]))