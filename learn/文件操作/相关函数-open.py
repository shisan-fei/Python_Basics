'''
打开文件：
    open()
    参数：1.文件路径 url
           相对路径：从某个目录开始相对地址
           绝对路径：从根开始描述
         2.打开方式
            基本模式：w r x a
            w:写入  文件不存在就创建，文件存在就清空文件（覆盖写入）
            r:读取   文件不存在就报错，存在就打开。文件指针在最前边
            x:异或模式 文件不存在就创建，存在就报错。防止覆盖
            a:写入追加  文件不存在就创建，存在就追加。打开后指针在最后
            扩展模式：b +
            b: 二进制
            +： 增强模式，可读可写

         3. encoding 可选，设置字符集  encoding='utf-8'
            若是一个二进制文件，不需要设置字符集

         4. 文件操作组合
            w r a x
            wb rb ab xb
            w+ r+ a+ x+ ：w+和r+都是读写，w+会覆盖，r+会在开头添加
            wb+ rb+ ab+ xb+
        5. seek() 设置当前指针位置
'''
#打开文件
#fpw = open('name_txt','w',encoding='utf-8')
#fpr = open('name_txt','r',encoding="utf-8")
#fpx = open('name_txt','x',encoding='utf-8')
fpa = open('name_txt','a',encoding='utf-8')



#写入内容
fpa.write('\nguofucheng')
#print(fpr.read)

#关闭文件
#fpw.close()
fpa.close()