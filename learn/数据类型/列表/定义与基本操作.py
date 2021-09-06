'''
定义：
    中括号[]，每个元素用逗号隔开
    list函数定义 List
    列表中元素为任意类型

操作：
    列表拼接：+，多个列表相加
    列表相乘：* 列表重复拼接
    in  检测字符串是否存在于列表
    索引操作：
        0 1 2 3 4……
     …… -4 -3 -2 -1
     通过下标修改元素，添加,追加,删除
    追加 ：list.append()
    删除： del list[n]
          pop(n)  默认弹出最后一个，弹出第几个
    获取列表长度:  len(list)


'''

list1 = [1,2,3,4]
list2 = ['a','b','c','d']

print(list2+list1)
print(list1*2)

print(1 in list1)

print(list1[2])   #获取元素
list1[2]=5
print(list1[2])

#追加append
list1.append('5')
print(list1)

print(len(list1))

print(list1.pop(1))