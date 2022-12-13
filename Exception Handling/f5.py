#raise exception
class Bank:
    def __init__(self,b) -> None:
        self.b=b

    def withdraw(self,a):
        if a<0:
            raise Exception('amount can not be negative')
        if self.b<a:
            raise Exception('pese nhi h') 
           
        self.b=self.b-a

obj=Bank(10000)
try:
    obj.withdraw(500)
except Exception as e:
    print(e)
else:
    print(obj.b)

