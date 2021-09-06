'''
列表切片：
    语法：list[开始索引:结束索引:步进]
         list[开始索引:]  从开始索引到最后
         list[:结束索引]  从第零个到结束索引
         list[:]或list[::] 所有
         list[::-1]   倒着输出列表
    使用切片对列表更新删除：
        list[开始索引:结束索引] = 'abc' 将匹配到的元素替换为指定元素
                                'a'  将匹配到的所有替换为一个元素a

'''

list1 = ['liudehua','zhangxueyou','liming','guofucheng','zhangguorong','xiaoshenyang','liuneng','zhaosi','songxiaobao']
f4 = ['xiaoshenyang','liuneng','zhaosi','songxiaobao']

print(list1[2:4])
print(list1)
f4[1:3]='123'
print(f4)             #--->['xiaoshenyang', '1', '2', '3', 'songxiaobao']