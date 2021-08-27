class User():
    def __init__(self,login_attempts):
        self.login_attempts=login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts =0



att_num=User(22)

print(att_num.login_attempts)
print(att_num.increment_login_attempts())