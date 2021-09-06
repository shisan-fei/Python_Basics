'''
检测：
    in: 检测一个字符串是否存在另一个字符串中
    len() 查看字符串长度
查找：
    str.find(sub[,start[,end]])  获取指定字符在字符串中索引位置未找到就发返回-1
    str.rfind(sub[,start[,end]])  从右向左找
    str.index()  和find相同，找不到后报错
    str.rindex()
统计：
    str.count(sub[,start[,end]])  统计一个字符在字符串出现次数

操作：
    str.split(sub,n)      按照指定分隔符，吧字符串分割成列表. 分割n次
    str.rsplit(sub,n)     从右向左分割，指定n次
    ’连接字符‘.join()   按照指定字符，将容器类型数据连接成字符串。split反向
    str.strip()       去除字符串左右两侧指定字符
    str.lstrip()       只去除左侧
    str.rstrip()       只去除右侧
    str.replace('a','b',n)      替换将a替换为b,替换n次
    str.center(n,"字符")      将字符串补充到指定位数，字符串居中。两边用字符填充
'''

var = 'love love you simida'

print("love" in var)
print(var.find('you',1,-1)) #指定范围查找，返回找到的开始索引号
print(var.rfind('you'))

print(var.count('i'))

var2 = "mysql_root_password"
list = ['user','123','passwd','321']

print(var2.split('_'))       #----->['mysql', 'root', 'password']
print(var2.split("_",1))     #----->['mysql', 'root_password']
print('='.join(list))        #----->user=123=passwd=321

title = "*****算法*****"
print(title.strip("*"))      #----->算法
print(title.lstrip("*"))

print(var.replace('love','like',2))

print(var2.center(40,"*"))