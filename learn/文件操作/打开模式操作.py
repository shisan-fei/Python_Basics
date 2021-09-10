'''
打开
操作：写入 读取
关闭

高级写法：不用专门关闭文件
    with open('路径'，’打开模式‘) as 变量：
          变量.操作()
'''
#追加
# fpa = open('name_txt','a',encoding='utf-8')   #打开文件
# fpa.write('\nhello')

#读取
# fpw = open('name_txt','r',encoding='utf-8')
# print(fpw.read())
# fpw.close()

#高级r+
with open('name_txt','r+',encoding="utf-8") as fprj:
    fprj.seek(20)                            #设置指针位置
    fprj.write("\nr+测试")
    print(fprj.read())

