import zipfile,os,shutil
'''
ZipFile(路径包名,模式压缩还是打包)
shutil.make_archive('all','zip','./')   
    参数1:压缩后的文件名,文件名自带后缀
       2：压缩方式，支持zip和tar.
       3. 压缩内容

'''
# with zipfile.ZipFile('test.zip','w') as myzip:    #将test.txt压缩为test.zip
#     myzip.write('test.txt')

# with zipfile.ZipFile('test.zip','r') as unzip:       #将test.zip解压到当前目录
#     unzip.extractall('./')

#压缩当前目录下所有文件目录

# with zipfile.ZipFile('all.zip','w') as allzip:
#     for i in os.listdir('./'):        #将当前目录下所有文件内容列出
#         #print(i)
#         allzip.write(i)

#用shutil归档压缩
shutil.make_archive('all.zip','zip','./')