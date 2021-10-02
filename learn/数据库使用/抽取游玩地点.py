import pymysql

#创建一个表来存储id和地名
def make_table():
    sql = '''create table if not exists address_table (
                                            id int(4) not null,
                                            address varchar(30) not null,
                                            primary key (id)
                                            )ENGINE=InnoDB DEFAULT CHARSET=utf8'''
    res = get_address(sql)
    if res:
        print('表创建成功')
        return True
    else:
        print("表创建失败")

#插入数据
def insert():
    sql = 'insert into address_table values (1,"HaShan"),(2,"SaoHaShan"),(3,"DongWuYuan"),(4,"HaiYangGuan")'
    res=get_address(sql)
    if res:
        print('数据插入成功')
        return True
    else:
        print('数据插入失败')

#查询数据
def select(n):
    sql = f'select address from address_table where id = {n}'
    data = get_address(sql)
    if data:
        print('我们去'+data[1][0]['address'])
    else:
        print('数据查询失败')

def get_address(sql):
    try:
        db = pymysql.connect(host='192.168.1.28',
                             user='root',
                             password='123456',
                             db='test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        cur = db.cursor()
        row = cur.execute(sql)
        db.commit()
        data = cur.fetchall()
        return row,data
    except:
        db.rollback()
        print('数据库操作失败')
    finally:
        db.close()

if __name__ == '__main__':
    # if make_table():
    #     insert()
    n = input('请输入数字1-4来选择去哪里：')
    select(n)