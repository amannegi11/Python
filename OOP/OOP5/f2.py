# multilevel
class Product:
    def review(self):
        print('Product customer review')

class Phone(Product):

    def __init__(self,price,brand,camera) -> None:
        print('Inside Phone class')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print('Buying a phone')


class Smartphone(Phone):
    pass


s=Smartphone(1000,"negi","64px")