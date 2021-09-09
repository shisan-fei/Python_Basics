'''
冰冻集合：
    定义：
        冰冻集合 使用frozenset()定义
        定义后不能修改
        冰冻集合只能做集合相关运算
        frozenset() 本身就是一个强制转换类函数，可将其他容器类型函数转换成冰冻集合
    可以和普通集合一样进行运算


'''
var = frozenset({1,2,3})
print(var)

for i in frozenset({'q','w','f',3,1}):
    print(i)

print(frozenset({i<<1 for i in range(6)}))