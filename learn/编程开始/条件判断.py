# n=0
# while n<3:
#    age = int(input("please enter a num:"))
#    if age < 20:
#        print('猜小了:')
#    elif age >20:
#        print('猜大了:')
#    elif age == 20:
#        print('猜对了:')
#        break
#    if n>=3:
#        print('超过次数')
#    n += 1
# print('game finash')

#计算1-100相加和
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)

n = 100
sum2 = (1+n) * n/2
print(sum2)

sum3,counter=0,1
while counter<=100:
   counter, sum3=counter+1,sum3+counter

print(sum3)

