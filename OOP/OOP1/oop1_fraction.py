class Fraction:
    # parameterized constructor --> is constructor it needs input while creating objects     
    def __init__(self,x,y):
        self.num=x
        self.den=y
        
    
    # __str__ method will return when you print object
    # def __str__(self):
    #     return f'{self.num}/{self.den}'
    
    def __add__(self,other):
        new_num=self.num*other.den+other.num*self.den
        new_den=self.den*other.den

        return f"{new_num}/{new_den}"

    def __sub__(self,other):
        new_num=self.num*other.den-other.num*self.den
        new_den=self.den*other.den

        return f"{new_num}/{new_den}"

    def __mul__(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den

        return f"{new_num}/{new_den}" 

    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num

        return f"{new_num}/{new_den}"    


f1=Fraction(1,2)
f2=Fraction(2,1)
print(f1.__add__(f2))
print(f2.__add__(f1))
print(f1.__sub__(f2))
print(f1.__mul__(f2))
print(f1.__truediv__(f2))