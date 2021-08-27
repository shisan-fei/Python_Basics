import sys

#向脚本中传入参数
print(sys.argv)       #当前程序路径,list
print(sys.argv[0])    #当前文件名，str

print(sys.path)
print(sys.platform)  #系统
print(sys.version)

for i in range(3):
    sys.stdout.write('小马过河')
    sys.stderr.write('小狗过河')