'''
字典推导式：

'''
var = dict(name='wanglf',sex='man',age='22')
#字典中键值对位置互换
#普通方法
newvar={}
# for k,v in var.items():
#     newvar[v] = k
# print(newvar)

#推导式
newvar = {v:k for k,v in var.items()}   #需要返回两个值，返回一个值是集合推导式
print(newvar)

var2 = {'a':1,'b':2,'c':3,'d':4}
#将值为偶数的键值互换
newvar2={}
for k,v in var2.items():
    if v % 2 == 0:
        newvar2[v]=k
#print(newvar2)

newvar2={v:k for k,v in var2.items() if v%2==0}
print(newvar2)

