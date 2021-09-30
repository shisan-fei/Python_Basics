'''
正则表达式规则定义
    普通字符
        直接使用字符串匹配
    转义字符
        \w  代表单个字母数字下划线
        \W  单个非字母数字下划线
        \d  单个数字
        \D  单个非数字
        \s  单个空格符
        \S  单个非空格或指标符
    特殊字符
        .  任意单个字符,除了换行符
        *  匹配任意次：.*(任意字符任意次) \d*(任意数字任意次)
        +  代表至少匹配一次,碰到匹配不到的就结束
        ？ 拒绝贪婪，只匹配前边的一次
        {次数} 匹配次数。{2,5} 表示区间，表示匹配2到5次
        [区间] 代表字符范围，如[A_Z] [0-9] [a-z,0-9,-]就相当于\w
        ()  代表子组
        ^$ 代表开头结尾
正则模式
    re.I  不区分大小写

'''
import re
var = 'ilahuy22o  us521imid9a'

print(re.search('\D',var).group())
print(re.search('\s',var).span())
print(re.search('\w\w',var).group())    #两个连续字符
print(re.search('\d\w',var).group())   #组合使用，数字加字符

print(re.findall('.',var))
print(re.search('\d*',var).group())
print(re.findall('\d*',var))

print(re.search('\w+',var).span())     #贪婪模式，匹配任意个匹配到的
print(re.search('\w+?',var).group())   #拒绝贪婪，匹配一个匹配到的

print(re.search('\w((\d{2})(\w+))',var).groups())

