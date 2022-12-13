class myex(Exception):

    def __init__(self,message):
        print(message)




#raise exception
class Bank:
    def __init__(self,b) -> None:
        self.b=b

    def withdraw(self,a):
        if a<0:
            raise myex('amount can not be negative')
        if self.b<a:
            raise myex('pese nhi h') 
           
        self.b=self.b-a

obj=Bank(10000)
try:
    obj.withdraw(-500)
except myex as e:
    print(e)
else:
    print(obj.b)

