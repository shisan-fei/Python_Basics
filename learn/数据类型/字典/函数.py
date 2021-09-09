'''
len()     字典长度
keys()    字典key
values()  字典值
iterm()   字典kv
iter(dict)    以字典的键为元素迭代器
pop(‘key’)  将字典中指定key的值弹出 ，删除
get('key','设置默认返回值')   获取指定键的值，与直接获取相比优点是若键不存在返回none而不是报错
update() 更新字典,key存在就更新，不存在就添加
setdauft(key,[default])   若存在key就返回v。若不存在就插入值为default键为key，返回default

'''
var = dict(name='wanglf',sex='man',age='22')
print(var.pop('age'))
print(var.get('name'),var.get('hello'),var.get('hh','默认返回值'))

var.update(name='wlf')
var.update({'address':'chine'})
print(var['name'],var)

print(var.setdefault('name','like'))    #name存在就返回v
print(var.setdefault('nn','test'))     #由于没有nn，就插入nn :test
print(var)