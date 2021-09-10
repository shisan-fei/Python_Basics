#登录
def login():
    islogin = True   #定义变量控制外循环
    login_err=3
    while islogin:
        username = input('请输入登录用户')
        if username in userlist:    #判断用户是否存在
            if username in blank_user_list:
                print('用户已经锁定')
            else:
                while True:
                    passwd = input("请输入密码")
                    inx = username.index(username)
                    if passwd == userpasswd[inx]:     #若输入的密码等于列表中的密码
                        print('登录成功')
                        islogin = False
                        break
                    else:
                        login_err -= 1
                        if  login_err != 0:    #判断错误次数，还有机会就输出提示
                            print(f"密码不正确,还有{login_err}机会")
                        else:
                            print("没机会了")              #设置失败三次后将用户写入黑名单
                            with open('blank_user', 'a+', encoding='utf-8') as buser:
                                buser.write(username)


        else:
            print("用户不存在")






if __name__ == '__main__':
    #register()
    login()

