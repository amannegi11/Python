#Abstraction
from abc import ABC ,abstractmethod
class BankApp(ABC):

    def database(self):
        print('connected to database')
    
    @abstractmethod
    def seccurity(self):
        ...


class MobileApp(BankApp):
    def mobile_login(self):
        print('login into mobile')


    def seccurity(self):
        print('mobile secirity')
    

m=MobileApp()
m.seccurity()

# you can not make object of abstract class