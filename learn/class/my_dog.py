'''
__init__方法：每当根据类创建实例时都会自动运行
self：self参数为必须，在其他参数之前。
      在调用__init__方法创建实例时自动传入self，
      每个与类相关联的方法调用都要传入self，他是一个指向实例的引用，让实例可以访问类中的方法和属性。
属性：通过实例可以访问的变量（name，age）
'''

class Dog():                    #编写一个类dog
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name=name          #以self为前戳的变量可供类中所有方法引用。获取存储在形参name中的值，将他存在name变量中。
        self.age=age

    def sit(self):
        print(self.name + " " + 'is now sit')

    def roll(self):
        print(self.name + '\t' + 'now roll')


'''根据类创建实例,可创建多个实例。创建实例后就可以调用类中的方法了'''
my_dog = Dog('ale','12')
your_dog = Dog('jack','3')
print('my dog name is :' + my_dog.name)
print('my dog age is :' +  my_dog.age)

print('this is a your dog ,age is :' + your_dog.age)

"""调用方法"""
my_dog.sit()   #调用方法指定实例名称（my_dog）,和调用方法（sit）
my_dog.roll()

your_dog.roll()