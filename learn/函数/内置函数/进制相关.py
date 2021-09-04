'''
bin() 将数值类型转为二进制
int() 转为整型
oct() 转为8进制
hex()  转为16进制
ord()  将字符转为ascii
      ascii 128个字符
      GB2312 汉字编码标准 7445字符
      GBK    兼容Gb2312
      unicode  统一编码字符集
           utf-8 最常用，一个汉字占3字节。不是字符集，是unicode一种编码方案。
'''

print(bin(128))

print(int(0b11000000))   #二进制表示0b……

print(oct(13))

print(hex(15))

print(ord('b'))