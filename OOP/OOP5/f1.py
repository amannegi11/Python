#single inheritance
class Phone:
    def __init__(self,price,brand,camera) -> None:
        print('Inside phone constructor')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print('Buying a phone')


class Smartphone(Phone):
    pass

Smartphone(1000,"negi","64px").buy()