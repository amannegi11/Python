#constructor example

class Phone:
    def __init__(self,price,brand,camera):
        print('Inside Phone constructor')
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying A phone")

class SmartPhone(Phone):
    ...

s=SmartPhone(2000,'Apple',13)
s.buy()

        