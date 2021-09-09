'''
字典：
    由键值对组成的数据集合，字典中的键不能重复
    字典中的键必须是不可变的数据类型，常见的键是字符串和整型
    定义：
        1. var = {'a':1,'b':2}
        2. dict函数定义：  var = dict(name='wanglf',sex='man',age='22')
        3. 数据类型转换： var = dict(二级容器类型)
                           dict(['a',1],['b',2])
        4.zip函数，dict转类型
            var = dict(zip(list1,list2))
    操作：
        获取：var['key']
        修改：var['key'] = value
        删除：del var['key']
        添加：var['key'] = value
        检测成员：只能检测key
            ‘key’ in var
        获取字典长度，键值对个数 len()
        获取所有的key： keys()
        获取所有value：values()
        获取所有键值对: items()

'''
var = {'a':1,'b':2,'c':3}
var2 = dict(name='wanglf',sex='man',age='22')

print(var['a'])

var['c'] = 4
print(var['c'])

del var['c']
print(var)

var2['from']='china'
print(var2)

print('name' in var2)

print(len(var))

print(var.keys())
print(var2.values())
#编历键值
for k,v in var2.items():
    print(f'{k}={v}',end=" ")
#编历值
for v in var2.values():
    print(v,end="+")
#编历键
for k in var2.keys():
    print(k,end="-")