# Aggregation: (has a relationship), one class owns the other class. One class is the owner and other is its property.
#Customer -->has a --> Address
#Restuarant --> has a --> Menu

# example 
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def print_address(self):
        print(self.address.city, ' ',self.address.pin, ' ', self.address.state)
    
class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state
        
add = Address('Taxila', 1239, 'Punjab')      
        
cust = Customer('Bilal', 'male', add)


cust.print_address()


# example 2
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def print_address(self):
        print(self.address.city, self.address.pin, self.address.state)

   
    
    
class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

   
        
        
add1 = Address('Isb', 345, 'Pak')      
cust = Customer('Ali', 'male', add1)

cust.print_address()
