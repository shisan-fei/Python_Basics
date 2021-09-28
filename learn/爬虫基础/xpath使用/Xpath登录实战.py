import requests
from lxml import etree

#封装类进行登录
class csdn():
    logurl = ''     #登录地址
    orderurl=''     #目标访问地址
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    req = None   #请求方法
    token = ''
    def __init__(self):
        #请求对象初始化
        self.req = requests.session()
        if self.getlogin():
            if self.postlogin():
                self.getlogin()


    #登录页面，获取_token
    def getlogin(self):
        res = self.req.get(url=self.logurl,headers=self.headers)
        if res.status_code == 200:
            print('请求成功')
            html = etree.HTML(res.text)
            self.token = html.xpath('//input[@name="_token"]/@value')[0]
            print('token获取成功')
            return True

    #post请求页面获取cookies,登录页面
    def postlogin(self):
        username = ''
        passwd = ''
        data = {
            '_token':self.token,
            'username':username,
            'password':passwd
        }
        #发起post请求
        res = self.req.post(url=self.logurl,headers=self.headers,data=data)
        if res.status_code == 200 or res.status_code == 302:
            print('登录成功')
            return True

        #get请求账户信息
    def getorder(self):
        res = self.req.get(url=self.orderurl,headers=self.headers)
        if res.status_code == 200:
            print('页面请求成功')
            html = etree.HTML(res.text)
            r=html.xpath('//div[@class="avatar-content"]//small/text()')   #页面要找的东西
            print(r)

getcsdn = csdn()
