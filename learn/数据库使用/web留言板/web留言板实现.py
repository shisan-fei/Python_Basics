'''
完成一个web留言板：
    访问本地8080端口进入页面跟目录，直接展示留言板全部内容
    点击添加后跳转到/add资源页面，可进行添加操作
    点击删除按钮后可以删除留言
'''
import pymysql,time
from flask import Flask,render_template,request
app = Flask(__name__)

#定义视图，获取数据库中所有信息，将留言表展示在页面
@app.route('/')
def index():
    #获取所有留言板数据
    data = model('select * from lyb')
    #print(data)
    #将数据分配到模板中,return的就是页面显示的
    return render_template('index.html',data=data)
    #return 'Hello'
'''调用render_template，会找到index.html文件，将data作为data写入
    index.html文件在当前目录下的template目录下'''

#定义视图，显示留言添加页面
@app.route('/add')
def add():
    #显示添加页面，add.html就是添加页面
    return render_template('add.html')

#定义视图函数，接收表单数据，完成数据写入功能
@app.route('/insert',methods=['POST'])
def insert():
    #接收表单数据
    data = request.form.to_dict()
    data['date'] = time.strftime('%Y-%m-%d')  # 增加时间这个数据
    #将数据添加到数据库
    sql = f'''insert into lyb values(null,"{data['nikename']}","{data['info']}","{data['date']}")'''
    res = model(sql)     #执行sql，判断sq执行返回结果是否为1，就成功
    if res:
        return '<script>alert("留言成功");location.href="/"</script>'   #弹回到列表页
    else:
        return '<script>alert("留言失败");location.href="/add"</script>'  #返回添加页

#定义视图函数，接收id，完成删除操作功能
@app.route('/delete')
def delete():
    #接收id
    id = request.args.get('id')
    #写sql语句
    sql = 'delete from lyb where id={}'.format(id)
    #执行删除sql
    res = model(sql)
    #判断是否删除成功后跳转
    if res:
        return '<script>alert("留言删除成功");location.href="/"</script>'
    else:
        return '<script>alert("留言删除失败");location.href="/"</script>'

#封装一个mysql操作
def model(sql):
    try:
        db = pymysql.connect(host='192.168.85.134',
                             user='wlf',
                             password='123456',
                             db='wlflt',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        cruose = db.cursor()
        row=cruose.execute(sql)
        db.commit()
        data = cruose.fetchall()
        if data:
            return data
        else:
            return row
    finally:
        db.close()


if  __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=8080)
