import random
'''
random() 返回0-1之间任意数，左闭右开（取不到1）
randrange(开始，结束，步进) ，获取范围内整数.左闭右开结束值取不到
randint()  随机产生范围内整数
choice() 随机获取容器中值
shuffle()  随机打乱列表中值
'''
print(random.random())
print(random.randrange(4,10))

print(random.choice([2,1,4,6,67]))
list = [1,2,3,4]
random.shuffle(list)
print(list)
