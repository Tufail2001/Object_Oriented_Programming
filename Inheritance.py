# Inheritance
# code reuseability
# child class inheritance constructor, non private attributes and non private methods
# if child class don't have its own constructor then parent class constructor is called
# But if child class has its constructor then parent class constructor will not be called, it mean variables inside 
# parent class constructor will not be initialized and child class object can't access them because these are not 
# initialized in child class object

class Phone:
    def __init__(self, brand, model, price):
        print('Inside of Constructor of Phone')
        self.brand = brand  
        self.model = model
        self.price = price
    
    def buy(self):
        print('Phone purchased')

class SmartPhone(Phone):
    pass


s= SmartPhone('Apple', 'IPhone 16 Pro Max', 1500)
print(s.brand, s.model, s.price)
s.buy()


#Example 2
class Phone:
    def __init__(self, brand,price, camera):
        print('Inside of Constructor of Phone')
        self.brand = brand
        self.price = price
        self.camera = camera

def SmartPhone(Phone):
    def __init__(self, model,ram, os):
        print('Inside child class')
        self.model = model
        self.ram = ram
        self.os = os

s = SmartPhone('S23 Ultra', 128, 'Andriod')

# child can't access the private member of parent class

class Phone:
    def __init__(self, brand, price, camera):
        self.__brand = brand
        self.price = price
        self.camera = camera

    def show(self):
        print(self.__brand)

class SmartPhone:
    def check(self):
        print(self.__brand)

       
s = SmartPhone('Samsung', 57000, 12)
print(s.price())

