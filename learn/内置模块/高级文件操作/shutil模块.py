'''
shutil:
    copy(a,b)  将a文件复制到b路径
    copy2()    同样是复制，保留源文件权限，时间等元数据
    copyfile() k拷贝文件内容，打开文件，读取文件，写入新文件
    copytree()  拷贝目录,将目录拷贝到指定目录，目标目录必须不存在
    rmtree()    删除目录，目录可以不为空
    move()   移动文件或目录到指定路径
'''
import shutil
import os
#shutil.copy('./test.txt','../')

#os.makedirs('./abc/b/c')    #在当前目录创建目录
#shutil.copytree('./abc','./cba/')

#shutil.rmtree('./cba')          #删除目录

shutil.move('./abc','../')        #移动目录

