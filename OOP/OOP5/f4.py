#multiple
class Phone:

    def __init__(self,price,brand,camera) -> None:
        print('Inside Phone class')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print('Buying a phone')

class Product:
    def review(self):
        print('Customer review')
    def buy(self):
        print('Buying a phone1')

# Method resolution order
class Smartphone(Phone,Product):
    pass


s=Smartphone(1000,"negi","64px")
s.buy()