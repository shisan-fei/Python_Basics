'''
集合：
    确定的一组无序数据组合
    确定的：当前集合中的元素不能重复
    由多个数据组合的复合型数据（容器类型数据）
    集合中的数据没有顺序
定义：
    直接使用{}定义
    使用set()进行定义或转换
    使用集合推导式
    集合中存储的一般为Number，str，tuple 冰冻 类型
操作：
    无序
    False在集合中表示为0，所以False和0只能存在一个 Ture代表1
    检测集合中的值： in 和 not in
    获取集合中元素个数 len()
    追加元素 add()
            update(***)
    删除元素: pop()  只能随机删除，有返回值
             remove() 删除指定值，返回值none
             discard()  删除指定值，不存在不报错
             clear()   清空集合
    复制  copy() 集合中只有浅拷贝，不存在深拷贝
冰冻集合：
frozenset((1,2,3))




'''
var = {3,2,4,'asd','haha',True,('a','c')}
print(var)

print(True in var)
print(len(var))

var.add('del')
var.pop()
var.remove('del')
var.discard('555')
#var.clear()
print(var)

var.update('q','e','w')
print(var)