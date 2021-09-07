'''
1. {'user':'admin','age':20}   将字典中键值对转换成’=‘   --->['user=admin', 'age=20']
2. 将列表所有字母转换为小写
3.x 是0-5之间奇数 y 是0-5之间偶数 返回一个列表，xy两两组合返回一个元祖
4.使用列表推导式实现99乘法表
5.求M N中矩阵和元素乘积
'''

#1
dic = {'user':'admin','age':20}
list1 = [f'{k}={v}'  for k,v in dic.items()]    #对于字典使用items()方法，同时编历出kv
list2 = [n+'='+str(dic[n]) for n in dic]        #只编历字典的k，用dic[k]来获取v
print(list1,list2)
print('&'.join(list1))    #---->user=admin&age=20

#2
zimu=['aADDXda','djhfShjsS','AkSniDiS']
low = [i.lower() for i in zimu]
print(low)

#3
list3 = []
for i in range(6):
    for n in range(6):
        if i % 2 ==0 and n % 2 !=0:
            list3.append((i,n))
print(list3)
list4 = [(i,n) for i in range(6) for n in range(6) if i % 2 ==0 and n % 2 !=0]
print(list4)

#4
jiujiu = [f'{i}*{n}={i*n}' for i in range(1,10) for n in range(1,i+1)]
print(jiujiu)

#5

