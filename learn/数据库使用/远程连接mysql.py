'''
不同编程语言操作mysql都是使用mysql提供的api
    如果直接使用mysql的api，比较复杂
    python中可以使用包或模块进行mysql操作
        pymysql mysqldb

pymysql
    1. 连接mysql
        db=pymysql.connect(host='',user='',passwd='',db='',charest='',cursorclass=pymysql.cursors.DictCursor)
        cursorclass=pymysql.cursors.DictCursor: 默认结果是元祖，该参数将结果转换为字典
    2. 创建游标对象
        cursor=db.cursor()  执行命令时对游标操作
    3. 准备sql
    4. 用游标对象执行sql
        游标.exec(sql语句)
    5. 提取结果
        游标.fetchall()  显示所有结果
        游标.fetchone()  显示一行结果

    6. 关闭数据库连接
        db.close()  关闭数据库连接
'''
import pymysql
#连接数据库
connection = pymysql.connect(host='192.168.85.134',
                             user='wlf',
                             password='123456',
                             db='test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
#创建游标对象
cursor = connection.cursor()

#写sql
sql = 'select * from users'

#执行sql
cursor.execute(sql)


#提取结果
data = cursor.fetchall()
#data = cursor.fetchone()


#关闭数据库
connection.close()

print(data)