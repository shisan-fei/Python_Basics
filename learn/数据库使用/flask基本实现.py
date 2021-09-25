'''
利用flask框架：
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')   #访问根时就显示hello word
def hello():
    return 'Hello World'
@app.route('/love')    #访问/love时就显示love you simida
def love():
    return 'love you simida'

if __name__ == '__main__':
    app.run(debug=Flask,host='127.0.0.1',port='8080')
