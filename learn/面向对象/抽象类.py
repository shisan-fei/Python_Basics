'''
抽象类：
    一个特殊的类
    1. 抽象类不能用，不能直接实例化成为对象
    2. 抽象类中包含抽象方法，抽象方法就是没有实现代码的方法
    3. 抽象类需要子类继承，并重写父类抽象方法。才可以使用。
抽象类，一般应用在程序设计，程序设计中一般要对功能需求进行规划，其中
    有一些需求是明确的并可以完成的，单数有一些是需求不名确的，后不知道怎么实现的
    娜姆就将这些方法定义为抽象方法，只定义方法名，不定义抽象方法。
举例：
    要开发一个新的产品，交给经理
    经理开始规划设计，完成产品开发
    需要不同的技术，需要不同的人完成
    这样的话，老大就自己完成一部分，好友一部分定义了需求，但是没有具体实现，要其他人来实现
    这样就完成了一部分，未完成的就是抽象方法
'''
import abc
#如果要定义为抽象类，那么这个类的mateclass属性必须是metaclass=abc.ABCMeta
class WriteCode(metaclass=abc.ABCMeta):
    #需要抽象的方法，使用装饰器进行装饰
    @abc.abstractmethod
    def write_php(self):
        pass
    def write_java(self):
        print('当前java方法已经实现')
    def wrte_python(self):
        print('python代码已经实现')

#抽象类不能直接实例化对象
# task = WriteCode()
# task.write_php()

#要定义子类继承抽象类，来继承抽象类中的抽象方法
class Deam(WriteCode):
    def write_php(self):     #完成了父类的抽象方法
        print('实现了php代码开发')

task2 = Deam()
task2.write_php()   #现在就可以访问了

'''
抽象类应用：
    例如开发一个框架，这个框架有什么功能
    但是具体用这个框架开发什么产品，并不清楚
    框架就具备一定的功能即可，剩下的就要具体的开发人员，来开发的自己的内容
'''