'''
seek()  设置文件指针 seek(0,2)指针指定到末尾
写入：
    write() 写入内容,只能写入字符串类型
    writelines()  可以写入容器类型数据，容器中的元素要是字符串
读取：
    read()  读取内容，默认从当前指针读取到最后，也可指定读取的长度。
    readline() 只读一行，也可指定读取字节数
    readlines() 读取多行，每行作为一个元素写入列表
截取：
    truncate()  截取文件内容
    默认从文件首行首个字符截断，截断的长度为size字节数。size若为0 就从当前位置截到末尾

'''
var = 'how are you'
var1 = ['aa','bb']
# with open('./name_txt','a+',encoding='utf-8') as fp:
#     #fp.write(var)
#     fp.writelines(var1)

with open('name_txt','r',encoding='utf-8') as fp:
    fp.seek(0)          #设置指针位置
    print(fp.read(10))   #读取字节长度
    print(fp.readline())
    print(fp.readlines(8))
#
# with open('name_txt','r+',encoding='utf-8') as fp:
#     print(fp.truncate(20))    #目标文件就保留一个字符