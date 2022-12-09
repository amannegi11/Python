#Hierarchial
class Phone:

    def __init__(self,price,brand,camera) -> None:
        print('Inside Phone class')
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print('Buying a phone')


class Smartphone(Phone):
    pass

class FeaturePhone(Phone):
    ...


Smartphone(1000,"negi","64px").buy()

FeaturePhone(1000,"negi===","64==px").buy()