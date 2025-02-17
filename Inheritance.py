# Inheritance
# code reuseability
# child class inheritance constructor, non private attributes and non private methods
# if child class don't have its own constructor then parent class constructor is called

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