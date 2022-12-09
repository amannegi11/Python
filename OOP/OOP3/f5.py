#child class can not access private members of the class

class Phone:
    def __init__(self,price,brand,camera):
        self.__price=price
        self.brand=brand
        self.camera=camera

    def show(self):
        print(self.__price)
class SmartPhone(Phone):
    def check(self):
        print(self._price)
s=SmartPhone(2000,"Apple",12)
print(s.brand)
s.check() 