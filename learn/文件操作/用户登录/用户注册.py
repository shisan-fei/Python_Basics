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
