'''
导入方式的分类：
    绝对导入：使用专门的搜索路径去查找和导入指定到包或模块
        import 模块
        import 包
        import 包.模块
        from 包 import 模块
        from 模块 import 内容
        from 包 import 模块
        from 包.模块 import 内容
    相对导入： 只能在非主程序的模块中使用
    from .包名/模块名 import 模块/内容
    from ..包名/模块名 import 模块/内容
'''

'''
导入包时主要搜索路径：
    1. 当前导入模块的程序所在文件
    2. python的安装目录
    3. python解释器指定的其他第三方模块位置 
'''

#在当前脚本查看包或模块搜索路径
import sys
print(sys.path)
'''
'E:\\python_script\\workbook\\learn\\模块和包\\包', 
'E:\\python_script\\workbook',
'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 
'C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 
'''
#可以自己定义一个路径，加入到搜索路径
sys.path.append('新的路径')
