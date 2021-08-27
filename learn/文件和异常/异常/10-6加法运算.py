print('please enter two num')
num1=input("num1:")
num2=input('num2:')
try:
    count = int(num1) + int(num2)
except ValueError:
    print('please enter num')
else:
    print(count)

