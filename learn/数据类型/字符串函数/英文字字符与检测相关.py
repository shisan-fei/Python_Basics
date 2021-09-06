'''
大小写转换
    capitalize()  将第一个英文字母转换为大写
    title()       将字符串中每个单词首字母大写
    upper()       将所有字母转换成大写
    lower()       转换为小写
    swapcase()    大小写相互转换
'''

var = 'hello sankeyou very mach'

print(var.capitalize())
print(var.title())
print(var.upper())
print(var.lower())
print(var.swapcase())


'''
字符检测方法：
    isupper()  检测当前字母是否都为大写  Ture False
    islower()  检测当前字母是否都为小写
    istitle()  检测是否为每个单词首字母大写
    isalnum()  检测是否全由字符组成（中文 英文 数字）
    isalpha()  检测是否由中英文字符组成，不包含数字空格等
    isdigit()  检测是否为纯数字
    isspace()  检测是否为纯空格组成
    startswith('h',n) 检测是否由指定字符开始,指定从第n个元素开始
    endswith('mach',i,n)  检测是否由指定字符结尾,可以指定区间i-n
'''
print(var.isupper())
print(var.islower())
print(var.istitle())
print(var.isalnum())
print(var.isalpha())
print(var.isdigit())
print(var.isspace())
print(var.startswith('h'))
print(var.endswith('mach'))

