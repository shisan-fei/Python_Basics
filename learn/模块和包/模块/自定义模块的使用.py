'''
在当前脚本中，要使用一些定义好的功能时，可以带入模块
要使用模块中的内容
    可以导入模块       import 模块
    可以导入模块的内容  from 模块 import 内容
                     from 模块 import 内容 as 新名称    导入模块中的内容，重新起个名字
'''

#使用系统模块
import time
print(time.strftime('%F'))

#使用自定义模块
import MyEx
obj = MyEx.MyException()   #使用模块中的类实例化对象

MyEx.func()  #调用模块中的函数

print(MyEx.__name__)   #--->MyEx

