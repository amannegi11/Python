#polymorphism
class Shape:

    def area(self,radius):
        return 3.14*radius*radius

    def area(self,l,b):
        return l*b


c=Shape()
print(c.area(2))
print(c.area(2,2))


    