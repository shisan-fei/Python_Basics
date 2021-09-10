userlist = []
userpasswd = []
blank_user_list = []  # 黑名单用户
# 读取所有注册信息，并格式化分别写入列表
def read():
    with open('name_list', 'a+', encoding='utf-8') as ra:  # 为了避免文件不存在时报错使用a+打开
        ra.seek(0)
        # print(ra.readlines())
        for i in ra.readlines():  # 取出文件每一行
            r = i.strip()  # 按行读取每个用户数据wlf:123
            userinfo = r.split(':')  # wlf:123--->['wlf', '123']
            userlist.append(userinfo[0])
            userpasswd.append(userinfo[1])
    # 获取黑名单
    with open('blank_user', 'a+', encoding='utf-8') as blabk_users:
        blabk_users.seek(0)
        user = blabk_users.readlines()
        for i in user:
            blank_user_list.append(i.strip())


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
                    inx = userlist.index(username)   #因为用户列表和密码列表中同意用户密码一一对应，获取用户在用户列表的位置
                    if passwd == userpasswd[inx]:     #若输入的密码等于列表中的密码。inx即使用户在列表中的位置，也是密码在列表中的位置。
                        print(f'{userlist[inx]}登录成功')
                        islogin = False
                        break
                    else:
                        login_err -= 1
                        if  login_err != 0:    #判断错误次数，还有机会就输出提示
                            print(f"密码不正确,还有{login_err}机会")
                        else:
                            with open('blank_user', 'a+', encoding='utf-8') as buser:
                                buser.write(f'\n{username}')
                            print("没机会了")  # 设置失败三次后将用户写入黑名单
                            break
        else:
            print("用户不存在")

# 注册功能
def register():
    site = True
    while site:
        username = input('welcome register please enter username：')
        if username in userlist:
            print('用户已经存在')
        else:
            while True:
                passwd = input('please enter password:')
                if len(passwd) >= 3:
                    repasswd = input('please enter password to make suer:')
                    if repasswd == passwd:
                        with open('name_list', 'a+', encoding='utf-8') as pw:
                            pw.write(f'{username}:{passwd}\n')  # 将用户名和密码写入文件，每行换行存储。
                        print('注册成功')
                        site = False
                        break  # 两次输入密码相同就结束循环
                    else:
                        print('两次密码输入不同，重新输入')
                else:
                    print('密码格式不正确')

#判断当前脚本是否作为一个主进程脚本执行
if __name__ == '__main__':
    #这里的代码只用用python解释器直接使用时才执
    #如果当前脚本作为模块被其他文件导入，这个地方的代码不会执行
    #所以这个地方适合写脚本测试，不会影响其他脚本
    read()
    print(userpasswd)
    print(userlist)
    while True:
        vars = '''
        ** 登录（0） 注册（1）**
        '''
        print(vars)
        num = input("请选择功能")
        if  num == '0':
            login()
        elif num == '1':
            register()
        else:
            print('选错了')
        break


