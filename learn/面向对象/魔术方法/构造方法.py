'''
__new__ 构造方法：
        触发：当类实例化对象时自动触发，在__init__之前触发
        作用：管理控制对象创建过程
        参数：一个cls接收当前类，其他参数根据初始化方法参数决定
        返回值：必须返回object.__new__(cls)，若没有返回值，实例化对象结果为none
        注意事项：__new__ 方法的参数和 __init__方法参数保持一致，除了第一个参数
        应用场景：设计模式中单例模式（一个类只能被实例化为一个对象）
'''
#定义一个人类
class Person():
    #构造方法
    def __new__(cls, *args, **kwargs):
        '''
        :param args: 接受初始化方法的参数，由Person传入
        :param kwargs:
        '''
        print('触发构造方法')
        print(args)
        print(kwargs)
        #如果在该方法中没有返回如下格式，则对象无法创建
        return object.__new__(cls)

    #初始化方法
    def __init__(self, name, age, sex):
        print('触发初始化方法')
        self.name = name
        self.age = age
        self.sex = sex
    #__call__方法可以将对象当做函数使用，默认执行当前方法
    def __call__(self, *args, **kwargs):
        print('你把对象当做函数调用了')
    #析构方法
    def __del__(self):
        print('触发了析构方法')

zsf = Person('zhangsanf',180,'man')
print(zsf)

zsf()   #使用魔术方法__call__ ,将对象当做函数调用

