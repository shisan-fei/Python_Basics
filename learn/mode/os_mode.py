import os
import platform
#print(platform.platform())
'''
print(os.name)       #返回系统，nt为windows。
print(os.environ)   #系统环境变量
print(os.path.isabs('/mnt/passwd'))  #判断是否为绝对路径
print(os.path.abspath('date'))   #生成一个绝对路径
print(os.path.basename('\pycharm\pak\kingsoft\pull_stream_me\date'))   #获取文件名
print(os.path.dirname('\pycharm\pak\kingsoft\pull_stream_me\date'))  #获取目录路径
'''

#创建删除目录
'''
os.mkdir('picture')            #创建目录，存在时不能创建
os.makedirs('picture\ aa')     #递归创建目录，存在时不能创建。
os.rmdir('picture')            #删除目录。不为空时，不能删除
'''

#文件操作
'''
os.mknod('a.txt')
os.remove('aa.txt')      #删除文件

file = open('a.txt','w')   #创建一个文件a.txt
file.close()
os.rename('a.txt','b.txt')   #文件重命名，将a.txt改为b.txt



from os.path import exists,splitext,join
print(os.path.exists('a.txt'))       #判断文件是否存在
print(os.path.splitext('hello.txt'))   #分离文件名和后缀名，不判断文件是否存在。
print(os.path.split('/root/passwd'))    #分离目录和文件名，不判断文件是否存在
'''

#遍历目录
for root,dir,file in os.walk("C:\log"):
    print(root)
    print(dir)
    print(file)
    for name in file:
        print(os.path.join(root,name))

