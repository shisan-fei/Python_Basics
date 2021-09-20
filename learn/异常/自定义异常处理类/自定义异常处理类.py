'''
异常处理，自定义异常处理类：
    在异常出现后，对异常处理。并把异常信息写入日志
    日志：
        日期 异常级别
        异常信息：引发异常类，异常信息，文件及行号。。。
traceback模块
logging模块
'''
# import traceback    #在引发错误后可以获取异常信息
# import logging      #python的日志收集工具
#
# try:
#     int('aa')
# except:
#     #使用traceback获取异常信息，并异常后的代码可以正常执行
#     errormsg = traceback.format_exc()
#     print(errormsg)

#自定义异常处理类
class Myexception():
    __obj = None     #把这个类写成一个单例模式，只实例化一次
    def __new__(cls):
        if not cls.__obj:
            cls.__obj = object.__new__(cls)
        return cls.__obj

    def __init__(self):
        import traceback
        import logging
        #logging基本配置
        logging.basicConfig(
            filename='error.log',     #日志写入的文件
            format='%(asctime)s %(levelname)s \n %(message)s',  #日志格式
            datefmt = '%Y-%m-%d %H:%M:%S'
        )
        logging.error(traceback.format_exc())

#使用自定义异常处理类处理异常
try:
    int('aa')
except:
    print('此处进行异常处理')
    Myexception()




import  time
print(time.strftime('%F'))