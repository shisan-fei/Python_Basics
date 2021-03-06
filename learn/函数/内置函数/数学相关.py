'''
abs()  返回绝对值
sum()  求和 对可迭代对象求和
max()   返回可迭代对象中最大值
min()   获取最小值
pow()   幂运算，返回x的y次幂
round()  四舍五入, 0.5和-0.5返回0，奇进偶退 1.5=2 2.5=2 3.5=4 4.5=4
'''

print(abs(-99))

print(sum([1,2,3,4,5,6,7,8,9]))

print(max([1,2,3]))
print(max((2,24,56)))

print(pow(2,8))

print(round(3.1415926,3))  #保留3位小数
