class Outer():
    def newinner(func):
        Outer.func = func    #把传入的函数定义为类方法
        return Outer.inner    #返回一个新的类方法

    def inner():
        print('相遇')
        Outer.func()
        print('回家')

@Outer.newinner
def love():
    print('一起玩')

love()