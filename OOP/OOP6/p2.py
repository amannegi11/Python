class Shape:

    def area(self,radius,b=0):
        if b==0:
            return 3.14*radius*radius
        else:
            return radius*b
        

    # def area(self,l,b):
    #     return l*b

c=Shape()
print(c.area(2))
print(c.area(4,1))