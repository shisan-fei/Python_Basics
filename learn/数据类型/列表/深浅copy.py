'''
浅拷贝：普通copy
    只能拷贝当前列表，不能拷贝列表中多维列表元素
    多维列表：
        拷贝后两个列表id相同
        对新列表修改，源列表和新列表均发生改变
深拷贝：
    不光拷贝当前列表，同时拷贝列表中多维列表
    import copy
    copy.deepcopy(lists)
'''


list1 = [1,2,3,4]

#简单的copy 复制列表
# list2=list1.copy()
# del list2[1]               #对列表的操作也是相互独立的
# print(list1,id(list1))     #id不同,  [1, 2, 3, 4] 2332402978752
# print(list2,id(list2))     #[1, 3, 4] 2332403014080

#copy多维列表时
lists = [[1,2,3],['a','b','c']]
# newlist = lists.copy()
# print(lists,id(lists[1]))       #id相同，另个列表占用同一内存
# print(newlist,id(newlist[1]))
# del newlist[0][2]
# print(lists,id(lists))
# print(newlist,id(newlist))

#深copy
import copy
newlist2 = copy.deepcopy(lists)

print(lists,id(lists[1]))    #此时发现id不同了
print(newlist2,id(newlist2[1]))
del newlist2[0][0]
print(lists,id(lists[1]))    #各自不受影响了[[1, 2, 3], ['a', 'b', 'c']] 2794201446016
print(newlist2,id(newlist2[1]))   #[[2, 3], ['a', 'b', 'c']] 2794201447680