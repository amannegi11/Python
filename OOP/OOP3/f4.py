class Phone:
    def __init__(self,price,brand,camera):
        print('Inside Phone constructor')
        self.price=price
        self.brand=brand
        self.camera=camera
   
class SmartPhone(Phone):
    def __init__(self,os,ram):
        self.os=os
        self.ram=ram
        print('Inside smartphone Constructor')

s=SmartPhone('Android',4)
