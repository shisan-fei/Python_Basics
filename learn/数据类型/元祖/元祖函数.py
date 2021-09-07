'''
len()    元祖长度
count()  统计元元素出现次数
index()  获取元素出现的索引
+  合并元祖
'''
tup = 'hh','kk','mm','kk'
tup1 = 1,2,3,4,5
print(len(tup))
print(tup.count('kk'))
print(tup.index('kk',0,2))
print(tup+tup1)                #输出一个合并的元祖
print(1 in tup1)              #1是否在tup1这个元祖中