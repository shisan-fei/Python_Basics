#斐波那契数列：从第二个数开始，后一个数是前两个数之和
# a = 0
# b = 1
# a, b = 0 ,1    #将0赋值给a ，1赋值给b
# while b<100:
#     print(b,end=' ')   #输出b，不换行
#     a,b = b, a+b       #b赋值给a：a就是前一个数，a+b就是下一个数（a a+b b）

def fb(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b = b,a+b

fb(10)
