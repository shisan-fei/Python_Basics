'''
什么是异常：
    简单理解就是非正常，没有达到预期目标
    异常是一个事件，并且这个异常事件会影响程序正常运行
分类：
    1. 语法错误导致异常
    2. 逻辑错误导致异常

在程序无法正常运行处理时，就会出现异常，在python中异常时一个对象表示一个错误。
例如：获取一个不存在索引
    Traceback (most recent call last):
    File "E:\python_script\workbook\learn\异常\异常.py", line 10, in <module>
        print(varlist[9])
    IndexError: list index out of range
    IndexError:异常类
    list index out of range ：异常信息

如何处理异常？
    1. 如果错误发生的情况是可以预知的，那么就可以使用流程控制进行预防处理
        比如：两个数字运算，其中一个是数字，运算就会出错。这是可以进行判断预防
    2. 如果错误的发生不可预知，就可以使用try except在错误发生时处理
    语法：
        try:
            可能发生异常的代码
        except:
            如果发生异常 进行的处理
    两者的区别，通过if判断预防时，错误没有发生。通过try except是发生了异常后再处理

'''
varlist = [1,2,3,4,5]
print(varlist[1])

'''假设读取的文件不存在，会发生错误，可以使用两种方式处理
1. 可以在文件读取前先判断当前文件是否存在
2. 也可以使用try…………except……在错误发生时处理
注意： try……except……是在错误发生后进行处理
'''
try:
    with open('./user.txt','r') as fp:
        fp.read()
except:
    print('文件不存在')

print('程序继续执行')

