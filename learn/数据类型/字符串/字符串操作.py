'''
加法，拼接
乘法,将字符串重复
切片，str[开始:结束:步进]
'''

var = '君不见 黄河之水天上来，奔流到海不复回'
var2 = '君不见 高堂明镜悲白发，朝如青丝暮成雪'

#拼接
print(var + var2)

#乘法
var3 = '大山' * 5
print(var3)

#切片
#字符串的索引操作，只能访问不能修改
print(var[5])
print(var[-5])
print(var[4:-5:2])
