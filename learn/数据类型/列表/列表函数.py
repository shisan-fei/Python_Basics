'''
len()  检测长度
count()  检查列表中指定元荤素出现的次数
append()  向列表尾部追加元素
insert()  在列表指定位置插入元素
pop(索引)     弹出列表指定位置元素,返回弹出的元素。结束后列表中指定元素将不存在
remove('元素')  删除指定元素，没有返回值
index('要找的内容',start,end)  找到元素在列表第一次出现的索引,可指定范围
extend()     接受一个容器类型数据，追加到列表中
clear()      清空列表内容
reveres()     将列表倒序输出
sort()      对列表进行排序 ，用法和sorted相同
copy()      复制当前列表

'''
list1 = ['liudehua','zhangxueyou','liming','guofucheng','zhangguorong','xiaoshenyang','liuneng','zhaosi','songxiaobao']
f4 = ['xiaoshenyang','liuneng','zhaosi','songxiaobao']
num = [1,4,8,2,3,0]

print(len(list1))
print(list1.count("xiaoshenyang"))

f4.append('wlf')
print(f4)

f4.insert(0,"name")
print(f4)

#print(f4.pop(3))     #弹出索引为3元素 默认最后一个
list1.remove('liudehua')
print(list1)

print(f4.index('liuneng',0,5))

f4.extend(['4da','tianw'])

num.sort(reverse=True)     #默认从小到大，reverse=True从小到大
print(num)


num2 = [1,3,4,7,[2,1,3,5]]
num3=num2.copy()
del num3[4][2]    #对多维元素进行操作就出现了全部改变情况
print(num2)       #--->[1, 3, 4, 7, [2, 1, 5]]
print(num3)       #--->[1, 3, 4, 7, [2, 1, 5]]


