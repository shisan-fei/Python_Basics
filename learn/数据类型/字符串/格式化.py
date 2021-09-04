'''
format()  格式化字符串 f

'''
#普通方式
auth='李白 '
var = '君不见 黄河之水天上来，奔流到海不复回。--- {}'.format(auth)
var1 = '{} 黄河之水天上来，奔流到海不复回。--- {}'.format('君不见',auth)
#print(var)
#print(var1)

#索引传参
var2 = '{1} 黄河之水天上来，奔流到海不复回。--- {0}'.format(auth,'君不见')
print(var2)

#关键字传参
var3 = '{a} 黄河之水天上来，奔流到海不复回。--- {作者}'.format(a="君不见",作者=auth)
print(var3)

#容器类型传参
var4 = '少林{0[0]}，武当{0[1]}，丐帮{0[2]}，华山{0[3]}'.format(['方世玉','张三丰','洪七公','令狐冲'])
date = {'a':"君不见",'作者':auth}
var5 = '{a} 黄河之水天上来，奔流到海不复回。--- {作者}'.format(**date)   #以字典方式传入
print(var4)
print(var5)

#f方法
var6 = f'{date["a"]} 黄河之水天上来，奔流到海不复回。--- {auth}'
print(var6)


#限定传入小数位数
var7 = '圆周率：{:.2f}'.format(3.1415926)   #小数后两位
print(var7)