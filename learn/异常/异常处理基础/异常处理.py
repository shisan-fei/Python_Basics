with open('test', 'a') as test:
    test.write('aaaaaabbbbb' + '\n')

try:  #尝试打开文件，病读取
    with open('test', 'r') as tfile:
        tfiles = tfile.read()
except FileNotFoundError:   #遇到FileNotFoundError异常打印语句。
    print('you find file not exit')
else:   #没有异常
    print(tfiles.rstrip())