'''
包：
    就是一个文件夹，里面有多个python文件
包的结构：
    包(文件夹)
    |-----—__init__.py 包的标志性文件（文件中可以有内容，可以没有）
    |------a.py   #模块，文件
    |------b.py
    |------……………………
    |------子包
            |------
            |------、
    |------|----- __init__.py
    |------|----- a.py
    |------|----- d.py

包的导入：
    直接导入包,用的内容是__init__.py中定义的模块   import package
    导入指定包中指定模块                         from package import aa
    导入文件中所有模块，可以导入指定包所有模块，使用时直接使用模块名即可。   from package import *
    from package.bb import funcbb
'''

#导入包使用
#直接导入包,用的内容是__init__.py中定义的模块
import package

#导入指定包中指定模块
# from package import aa
# aa.funcaa()

# from package.bb import funcbb
# funcbb()

#导入文件中所有模块，可以导入指定包所有模块，使用时直接使用模块名即可。
from package import *
bb.funcbb()   #要在包的__init__文件中定义__all__=['模块名']