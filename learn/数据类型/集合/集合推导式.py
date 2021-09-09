
#1. 普通推导式

var = {3,2,7,63,6}
newvar = {i for i in var}
print(newvar)

#带有条件表达式的
newvar2 = {i for i in var if i%2==1}
print(newvar2)

#带有多循环的
var2 = {1,1,1,1,1}
newvar3=set()
for i in var:
    for n in var2:
        newvar3.add(i+n)
print(newvar3)

print({i+n for i in var2 for n in var })

#带判断的多条件推导式
print({i+n for i in var2 for n in var if i%1==0 and n%2==0})

