import re

#匹配一个ip
pattern = re.compile(r'\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}')
str = '#192.168.1.1'
print(pattern.search(str))  #代表已匹配到的对象和所在位置 
print(pattern.search(str).group(0))  #用.group(0)打印出来    