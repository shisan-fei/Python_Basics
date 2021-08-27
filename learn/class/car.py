'''这是一个用于表示汽车的类'''
class Car():
    def __init__(self,make,model,year):          #定义一个init方法，方法接收三个形参的值。
        '''初始化描述汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading = 0                    #添加一个里程表属性，初始值为0


    def get_info(self):     #定义方法get_info，用三个属性来创建一个对汽车描述的字符串
        long_name=str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        '''打印一条指出里程的信息'''
        print('this car zoule: ' + str(self.odometer_reading))

    def updata_odometer(self,mileage):      #通过定义一个方法修改汽车里程数
        '''
        将里程数设置成想设置的数
        禁止将里程数调小
        :param mileage: 里程数
        :return:
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print('you can not make  mileage down ')

    def incrment_odometer(self,mails):
        '''将里程数增加多少'''
        if mails >0:
           self.odometer_reading +=mails    #接受以个数字并加到之前的里程数上。
        else:
            print('you can not make  mileage down')



# my_car=Car('BMW', 'X6','2021')             #根据类car创建一个实例
# print('my new car info: ' + my_car.get_info())
#
# my_car.updata_odometer(30)
# my_car.read_odometer()
#
# my_car.incrment_odometer(100)
# my_car.read_odometer()

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        '''描述电池容量'''
        print('battery size are: ' + str(self.battery_size))

    def get_range(self):
        ''' 电池容量对应的行驶里程数'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 260

        message = 'this car can go :' + str(range)
        message += 'miles on a full charge '
        print(message)

    #def upgrade_battery(self):
    #    check 电池容量
    #    if self.battery_size != 85:
    #        self.battery_size = 85




class Elect_car(Car):    #给car创建一个子类Elect_car
    '''电动汽车特点'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)    #super函数将子类和父类关联，调用父类__init__函数，让子类包含父类所有属性（父类叫superclass）
        #self.battery_size=100
        self.battery=Battery()




new_elect_car=Elect_car('yadi','h4','2021-01')      #创建实例，调用子类__init__
#print('my new elect car: ' + new_elect_car.get_info())
new_elect_car.battery.describe_battery()
