'''
递归函数就是定义了一个函数，然后在函数内，自己调用了自己这个函数
递归函数内必须要有结束，不然就会一只调用下去，直到调用的层数越来越多，栈溢出
递归函数是一层一层的进入，再一层一层的返回
'''

def digui(num):
    print(num)  # 3 2 1 0
    if num > 0:
        digui(num-1)
    print(num)    # 0 1 2 3

#digui(3)

#计算阶乘1*2*3*4*5*6*7
def jiecheng(sum):
    if sum < 1:
        return 1
    else:
        return sum*jiecheng(sum-1)

#print(jiecheng(7))

#实现斐波那契数列 1 1 2 3 5 8 13 21 34……
def fbnq(n):
    if n==1 or n==2:
        return 1
    else:
        return fbnq(n-1) + fbnq(n-2)

if __name__ == '__main__':
    #digui(3)
    print(jiecheng(7))
    for i in range(1, 7):
        print(fbnq(i), end=' ')

