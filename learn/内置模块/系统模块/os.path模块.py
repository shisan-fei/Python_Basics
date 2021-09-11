'''
系统模块中的路径模块：
os.path
    os.path.abspath()  将相对路径转换为绝对路径
    os.path.basename()  返回路径中最后一部分
    os.path.dirname()    返回路径最后一部分之前的
    os.path.join()      拼接两个路径
    os.path.split()     拆分路径，结果为os.path.dirname() + os.path.basename()
    os.path.splitext() 拆分路径和文件后缀
    os.path.getsize()   获取文件大小，文件不存在就报错
    os.path.isdir()      检测是否为文件是否为存在   -d
    os.path.isfile()     检测文件知否存在         -f
    os.path.exists()     检测路径是否存在，可以检测文件可以检测目录
    os.path.ismount(a,b)   检测ab两个文件是否指向同一个地方
'''
import os
print(os.path.abspath('./'))

print(os.path.basename('E:\python_script\workbook\learn\内置模块\系统模块'))
print(os.path.basename('E:\\name\wlf'))

print(os.path.dirname('E:\\name\wlf'))

print(os.path.join('E:\python_script\workbook','hahha'))

print(os.path.split('E:\python_script\workbook\hahha'))
print(os.path.splitext('E:\python_script\workbook\hahha.jpg'))

print(os.path.getsize('./系统操作-os.py'))

print(os.path.isdir('E:\python_script\workbook'))

print(os.path.isfile('./系统操作-os.py'))

print(os.path.exists('E:\python_script\workbook\hh'))

print(os.path.ismount('E:\python_script\workbook','../../../workbook'))