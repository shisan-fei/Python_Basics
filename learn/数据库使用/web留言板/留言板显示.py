import pymysql
from flask import Flask,render_template,request
app = Flask(__name__)

#定义视图，留言列表
@app.route('/')
def index():
    #获取所有留言板数据
    data = model('select * from lyb')
    #print(data)
    #将数据分配到模板中,return的就是页面显示的
    return render_template('index.html',data=data)
    #return 'Hello'
'''调用render_template，会找到index.html文件，将data作为data写入
    index.html文件在当前目录下的template目录下
    '''
#定义视图，显示留言添加页面
@app.route('/add')
def add():
    #显示添加页面
    return render_template('add.html')

#定义视图函数，接收表单数据，完成数据写入
@app.route('/insert',methods=['POST'])
def insert():
    #接收表单数据
    data = request.form.to_dict()
    print(data)
    #将数据添加到数据库
    #页面跳转到留言列表页
    return '接收表单，写入数据库'
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
    app.run(debug=True,host='127.0.0.1',port='8080')