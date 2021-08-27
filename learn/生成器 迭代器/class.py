class person:      #创建一个类，person
    def __init__(self,str):
        self.name = str

    def hello(self):  #定义一个方法，self（代表自己）。
          print(self.name)


b = person('jhh')   #创建实例，
print(b.name)

b.hello()     #调用方法