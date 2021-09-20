'''
用法总结：
    1.使用try except处理指定异常，若发生的异常不是指定的异常，就无法处理
    2. try except except…… 多分支结构，依次匹配异常，直到找到
    3. 通用异常匹配，Exception。他可以匹配任意的异常
    4. 多分支+通用.这样引发异常会按照从上往下顺序处理匹配。Except放在开头就直接匹配成功
    5. try except else，没有发生异常就执行else下代码
    6. try except else finally。无论是否引发异常，都会触发finally代码块
    7. 使用raise，主动抛出异常，指定输出的异常信息

try下的代码某行触发了异常，那么try下的其他的代码就不执行了
'''
list1 = [1,2,3]
s1 = 'hello'
# int(s1)   #引发ValueError错误

#会用try except处理指定异常，若不是指定的异常，就无法处理
try:
    int(s1)
except ValueError as e:   #指定异常，接异常信息存到变量e
    print(e,type(e))

#多分支处理异常类,指定多个不同的异常类，走向不同异常处理
try:
    int(s1)
    print(list1[4])
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
    print('KeyError',e)
except ValueError as e:
    print('ValueError',e)

#通用异常类 Exception,万能的，可以匹配所有的异常类
try:
    int(s1)
except Exception as e:
    print(e)

#多分支+通用.这样引发异常会按照从上往下顺序处理匹配。Except放在开头就直接匹配成功
try:
    int(s1)
    print(list1[4])
except IndexError as e:
    print('IndexError',e)
except KeyError as e:
    print('KeyError',e)
except Exception as e:
    print('Exception',e)

#try except else，没有发生异常就执行else下代码
try:
    str(s1)
except IndexError as e:
    print('IndexError',e)
else:
    print('try代码块没有引发异常')

# try except else finally。无论是否引发异常，都会触发finally代码块
try:
    str(s1)
except IndexError as e:
    print('IndexError',e)
else:
    print('try代码块没有引发异常')
finally:
    print('无论是否引发异常，都会触发该代码块')

#使用raise，主动抛出异常
try:
    raise Exception('发生错误')    #设置输出的异常信息
except Exception as e:
    print('Exception',e)    #--->Exception 发生错误


#assert断言
assert 2 == 1    #如果后边的表达式错误，就直接抛出异常AssertionError

