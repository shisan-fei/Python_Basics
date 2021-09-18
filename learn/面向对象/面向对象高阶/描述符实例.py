'''
要求分数在0-100之间
    1. 可以在初始化方法中检测，但是过后可以在类的外边通过对象修改成员。并且不符合规则不会检测出
        if score <=100 and score >= 0:
            self.score = score
        else:
            print('分数不符合规则')
    2. 可以定义一个setattr方法检测
        检测给score赋值时的判断，是否符合要求，符合要求的就同意修改
        若此时有多个分数，需要每个进行判断，增加代码量
        此时可以用描述符代理分数属性
    3. 用描述符类代理分数这个属性
        定义一个Score描述符类
        把学生类的score这个成员交给描述符进行代理
        只要在代理的描述符类中对分数进行赋值就好了


'''
#定义一个学生类 记录学号 名字 分数
# class Student():
#
#     def __init__(self,sid,name,score):
#         self.sid = sid
#         self.name = name
#         self.score = score
#         #检测分数范围
#         if score <=100 and score >= 0:
#             self.score = score
#         else:
#             print('指定分数不符合规则')
#
#     def returnMe(self):
#         info= f'''
#         学号：{self.sid}
#         姓名：{self.name}
#         分数：{self.score}
#         '''
#         print(info)
#
#     def __setattr__(self, key, value):
#         #print(key,value)
#         if key == 'score':    #此时判断传入的key为score属性时，判断属性值得范围确定是否同意修改
#             if value <=100 and value>=0:
#                 object.__setattr__(self,key,value)
#             else:
#                 print('修改的分数不符合')
#         else:
#             object.__setattr__(self,key,value)
#
# zsf = Student('001','zsf',100)
# zsf.returnMe()
# zsf.score = -10

#使用描述符类实现
#定义一个描述符类，代理分数管理
class Score():
    __score = 0                     #定义成私有的成员，只能在描述符内调用
    def __get__(self, instance, owner):
        #print(instance,owner)
        return self.__score                #直接获取，instance就是调用描述符的类的对象，owner就是调用它的类
    def __set__(self, instance, value):   #value就是，要修改的值
        #print(instance,value)
        if value >=0 and value <=100:
            self.__score = value
        else:
            print("分数不符合要求")


class Student():
    score = Score()     #将score这个属性的值交给代理完成赋值
    def __init__(self,sid,name,score):
        self.sid = sid
        self.name = name
        self.score = score

    def returnMe(self):
        info= f'''
        学号：{self.sid}
        姓名：{self.name}
        分数：{self.score}
        '''
        print(info)

zsf = Student('001','zsf',100)
zsf.returnMe()
zsf.score = -10
zsf.returnMe()