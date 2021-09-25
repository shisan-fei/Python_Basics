
import pymysql
db = pymysql.connect(host='192.168.85.134',
                     #port='3306',
                     user='wlf',
                     password='123456',
                     db='test',
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = db.cursor()
    #sql = 'insert into users values(5,"laowu",26)'
    sql = 'select * from users'
    #sql = 'delete from users where id=5'
    row = cursor.execute(sql)    #执行命令并返回操作的行数
    db.commit()    #在执行sql时，提交。可有可无
    data = cursor.fetchall()    #不是查询语句就没有返回结果
    print(data,row)
except:
    db.rollback()    #若失败就回滚
finally:
    db.close()