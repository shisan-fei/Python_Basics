'''
系统接口模块 os：
    getcwd()  获取当前工作目录，绝对路径.获取的是执行命令的路径
    chdir()   修改当前工作目录
    listdir()  获取当前或指定目录下所有 ls -a，返回一个列表
    创建目录：
        mkdir(’目录路径‘,777)    默认在工作目录创建文件夹 不能递归创建.可指定权限(在linux中)
        makedirs()  递归创建文件夹
    删除目录：
        rmdir()     删除一个空文件夹
        removedirs()  递归删除空目录，linux上不行，因为文件下都有隐藏文件
    删除文件：
        remove()    删除文件
    rename()    修改文件名
    system()     执行系统命令

'''
import os
print(os.getcwd())

#os.chdir('E:\python_script\workbook')
print(os.getcwd())        #--->E:\python_script\workbook

print(os.listdir())
print(os.listdir(path='E:\python_script\workbook'))  #--->['.git', '.idea', 'learn', 'main.py', 'README.md', 'venv']

#os.mkdir('abc')            #创建一个文件加
#os.makedirs('abcd/a/b/c/d')   #创建一个递归目录
#os.rmdir('abc')
#os.removedirs('abcd/a/b/c/d')     #写全路径，从后往前删除
#os.remove('aa')             #删除文件
#os.rename('aa','AA')        #把aa改成AA
print(os.listdir())

print(os.system('python --version'))

