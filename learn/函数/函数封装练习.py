def jiujiu(d=0):
    '''
    打印99乘法表
    n: 此参数控制正向输出还是反向输出。0时正向  1为反向
    :return:
    '''
    if d == 0:
       rs = range(1,10)    #1-9
    else:
        rs = range(9,0,-1)   #9-1
    for i in rs:
        for n in range(1,i+1):
            print(f'{i}x{n}={i*n}',end=" ")
        print()

jiujiu(0)


def juxing(b=0):
    '''
    打印一个实心矩形或者一个空心矩形
    :param b: 为0时为实心  1时为空心
    :return:
    '''
    print('# # # # # # # # # #')
    for i in range(1,9):
        if b == 0:
            print('# # # # # # # # # #')
            #print(f'#',end=" ")
        elif b == 1:
            print('#                 #')
            #if i % 10 == 0:
                #print()
    print('# # # # # # # # # #')

juxing(1)

