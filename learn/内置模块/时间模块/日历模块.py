import calendar

'''
monthrange(year,math)   返回指定年份月份数据，月份第一天是周几，该月有几天
'''
print(calendar.monthrange(2121,9))
res = calendar.monthrange(2121,9)

days = res[1]    #本月天数
week = res[0]+1  #月份第一天周几

print('*'*28)
print('一 二  三 四 五  六 七 ')
d=1
while d<=days:
    for i in range(1,8):
        if d > days or (i<week and d==1):
            print(' '*4,end=" ")
        else:
            print('{:0>2d}'.format(d),end=" ")
        #print(d,end=" ")
            d+=1
    print()
print('*'*28)