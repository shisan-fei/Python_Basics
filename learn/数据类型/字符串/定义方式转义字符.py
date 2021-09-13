'''
字符串定义
    1. 单引号： ’‘
    2. 双引号： “ ”
    3. 三引号： ’‘’ ‘’‘，“”“ ”“”
    多个类型引号同时出现：引号可以相互嵌套
'''

'''
转移字符
    一个普通字符，通过转义符 "\",实现另一种意义。
    转义符，续行符：
        作为转义符  -- 在转义符后出现的字符会有另一种意义
        作为续行符  -- 行位使用\可以换行继续书写
    \n:换行
    \r：光标的位置，字符串的起点
    \t：水平制表符，就是tab
    \b：退行符把他之前的字符删除
    \\:双斜线 ，将斜杠进行转义，输出一个斜杠
    r'字符串'：字符串内的内容原样输出。
          
'''
#续行符
var = '123' \
    'abc'
print(var)

#转义符
var2 = '东临碣石，\n以观沧海。'
print(var2)
#让字符串原样输出，忽略转义字符.使用r方法或双斜线
var3 = r'东临碣石，\n以观沧海。'

print(var3)