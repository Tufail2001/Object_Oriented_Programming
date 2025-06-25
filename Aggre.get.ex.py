# Example of Aggregation and get method
# how to get private attributes of class with get method
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_steet, new_city, new_state):
        self.name = new_name
        self.address.edit_address(new_steet, new_city, new_state)
    
    def give_address(self):
        print(self.address.street, self.address.get_city(), self.address.state)
    

 
        
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.__city = city
        self.state = state

    def edit_address(self, new_street, new_city, new_state):
        self.street = new_street
        self.__city = new_city
        self.state = new_state
    
    def get_city(self):
        return  self.__city 
    

add = Address(767, 'Attok', 'Punjab')
cust = Customer('Bazeed', 'male' add )

cust.give_address()


cust.edit_profile('Abbass', 912, 'Rwp', 'Punjab')

cust.give_address() 

