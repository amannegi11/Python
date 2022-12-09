class Phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")
class SmartPhone(Phone):
    def buy(self):
        print('Buying a Smartphone')
        #syntax to call parent ka buy method
        super().buy()

s=SmartPhone(2000,"Apple",13)
s.buy()
