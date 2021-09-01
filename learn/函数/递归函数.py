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

digui(3)