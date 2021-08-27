class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        """三个属性，餐厅名和菜单，和就餐过的人数"""
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        '''一个描述餐厅信息的方法。'''
        print('餐厅名：' + self.restaurant_name + '\n' '菜谱：' + self.cuisine_type)

    def open_restaurant(self):
        print('This restaurant is runing' + '\t' + self.restaurant_name)

    def set_num_served(self,num):
        '''让就餐人数递增'''
        self.number_served += num


'''
restaurant = Restaurant('super_eat','AAAA')    #创建实例，使用两个实参调用__init__()
print('餐厅名：', restaurant.restaurant_name)
print('菜谱：',restaurant.cuisine_type)

print('')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_num_served(100)
print(restaurant.number_served)
'''

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['A','B']

    def print_ice_list(self):
        for i in self.flavors:
            print(i)
        #print('ice fenlei: ' + self.flavors)

ice=IceCreamStand('summer','CC')
ice.flavors