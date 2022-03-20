import datetime 
from datetime import date,time,datetime,timedelta

'''
class datetime.date(year, month, day)：参数的意义就不多作解释了，只是有几点要注意一下：
year的范围是[MINYEAR, MAXYEAR]，即[1, 9999]；
month的范围是[1, 12]。（月份是从1开始的，不是从0开始的~_~）；
day的最大值根据给定的year, month参数来决定。例如闰年2月份有29天；
date类定义了一些常用的类方法与类属性，方便我们操作：

date.max、date.min：date对象所能表示的最大、最小日期；
date.resolution：date对象表示日期的最小单位。这里是天。
date.today()：返回一个表示当前本地日期的date对象；
date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；
datetime.fromordinal(ordinal)：将Gregorian日历时间转换为date对象；（Gregorian Calendar ：一种日历表示方法，类似于我国的农历，西方国家使用比较多，此处不详细展开讨论。）

date.year、date.month、date.day：年、月、日；
date.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
date.timetuple()：返回日期对应的time.struct_time对象；
date.toordinal()：返回日期对应的Gregorian Calendar日期；
date.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
data.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
date.isocalendar()：返回格式如(year，month，day)的元组；
date.isoformat()：返回格式如'YYYY-MM-DD’的字符串；
date.strftime(fmt)：自定义格式化字符串。在下面详细讲解。
'''


print(date.today(), date.max)       #2022-03-18 9999-12-31

d = date.today()
print(d.year,d.month,d.day)   #2022 3 18

#time 模块使用
tm = time(23 ,  46 ,  10 )  
print('tm:' , tm)  #    tm: 23:46:10
print('hour: %d, minute: %d, second: %d, microsecond: %d' % (tm.hour, tm.minute, tm.second, tm.microsecond))  #hour: 23, minute: 46, second: 10, microsecond: 0
tm1 = tm.replace(hour = 20)  #将小时换成20
print('tm1:' , tm1)     #tm1: 20:46:10
print('isoformat():' , tm.isoformat())  #isoformat(): 23:46:10  自定义时间格式