'''
类成员属性操作   不推荐使用类操作成员
    类名.属性 ：获取属性
    修改属性：修改后，通过这个类实例化的对象，他的属性也发生变化
    添加属性：添加后，通过这个类实例化的对象，也可以引用该属性
    删除类成员: 在之前和之后创建的对象都没有这个属性了

'''

class Cart():
    #属性，就是变量
    color = '白色'
    brand = 'jeep'
    pail = '3.0'

    #定义方法，就是函数，实现功能
    def lahuo(self):
        print('拉货')

    def laren(self):
        print("拉人")

    def douf(self):
        print('兜风')

print(Cart.brand)

#修改类属性
Cart.brand="bmw"
print(Cart.brand)
a = Cart
print(a.brand)    #对象引用的也是修改后的

#添加成员属性
Cart.name='x5'
print(Cart.name)

#删除类成员
#del Cart.name
#print(Cart.name)