'''
交集 并集 差集 对称差集
交集  set1&set2
并集  |   将集合中元素集中，去重
差集  -   set1-set2:1有2没有的   set2-set1:2有1没有的
对称差集 ^ 两集合去除重复的之后合并的
超集和子集：
    a是b的子集
    b就是a的差集
    检测：set1.issuperset(set2)  检测是否为超集，检测1是不是2的超集
         set1.issubeset(set2)    检测1是不是2的子集
         检测两集合是否相交:
           var1.isdisjoint(var2)  检测两集合是否不向交，不相交就返回true

函数：
    交集：
    set1.intersection(set2)  求交集
    set2.intersection_update(set2)  求交集后返回给set2
    并集：
    var1.union(var2)     求并集
    var1.update(var2)    求并集后赋值给var1
    差集
    var1.difference(var2)       差集
    var1.difference_update(var2) 求差集后赋值给var1
    对称差集
    var1.symmetric_difference(var2)  差集
    var1.symmetric_difference_update(var2)  求差集后将结果返回给var2


'''
var1 = {'gfc','ldh','zgr','f4'}
var2 = {'ln','xsy','zs','f4'}


print(var1&var2)
print(var1|var2)
print(var1-var2,var2-var1)
print(var1^var2)

print(var1.intersection(var2))  #返回1和2的交集
#var2.intersection_update(var1)      #计算交集后赋值给第一个集合，没有返回值
#print(var2)

print(var1.union(var2))
# var1.update(var2)
# print(var1)

print(var1.difference(var2))
# var1.difference_update(var2)
# print(var1)

print(var1.symmetric_difference(var2))
var1.symmetric_difference_update(var2)
print(var1)

print(var1.issuperset(var2))  #检测1是不是2的超集
print(var1.issubset(var2))    #检测1是不是2的子集

print(var1.isdisjoint(var2))