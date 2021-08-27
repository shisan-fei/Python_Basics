# with open('test_file.txt') as num:   #open('test_file.txt')创建一个表示文件的对象
#     nums = num.read()    #读取这个文件对象
#     print(nums.rstrip())

# with open('../../class/test_file.txt') as numb:
#     b= numb.read()
#     print(b.rstrip())

a=''
with open('test_file.txt') as line:
    line2 = line.readlines()      #将文件每一行存入列表，方便在with外使用
#    for lines in line:           #遍历一个文件的每一行
#        print(lines.rstrip(),end=' ')   #输出文件每行
# for lines2 in line2:  
#     print(lines2,end=' ')
for lines3 in line2:
    a += lines3.strip()
print(a[:20])