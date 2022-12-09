# Aggregation relationship between classes means one class owns other class
#can not access private variable of other class directly
class Customer:

    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
    
    def edit_pro(self,new_name,new_gender,new_city,new_pin,new_state):
        self.name=new_name
        self.gender=new_gender
        self.address.edit(new_city,new_pin,new_state)
class Address:

    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
    def get_city(self):
        return self.__city
    def edit(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state
# Aggregation is basically sending a class object as a input to other class 
add1=Address('gurgaon',122011,'delhi')    
cust=Customer('aman','male',add1)
cust.print_address()

cust.edit_pro('sk','male','mumbai',1111,'mp')
cust.print_address()