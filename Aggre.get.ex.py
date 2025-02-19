# Example of Aggregation and get method
# how to get private attributes of class with get method
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def give_address(self):
        print(self.address.street, self.address.get_city(), self.address.state)
    

 
        
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.__city = city
        self.state = state
    
    def get_city(self):
        return  self.__city 
    

add = Address(767, 'Attok', 'Punjab')
cust = Customer('Bazeed', 'male',add )

cust.give_address()
