# 1. 函数：计算四边形面积
# def area(width,height):
#     areas = width * height
#     print(areas)
#     return areas
#
# width=2
# height=3
# area(width,height)

# 2. 查看不可变对象内存改变情况
# def change(a):
#     print(id(a))  #获取a在内存中的地址
#     a+=a
#     print(id(a),a)   #a的值重新赋予后的内存地址
#     return
# a=1
# print(id(a))
# change(a)   #调用函数，查看a在内存中的变化。

#3. 不定长参数
def info(age,**tupl):      #*tupl将实参以元组方式接受，两个星号则以字典方式传入。
    print('年龄：',age)
    print(tupl)          #除age外的所有参数存入元组打印出来
    #for hobby in tupl:
    #     print(hobby)
    return



#info(20,'A','B','C','D')
info(20,tom='AB',net='CD')