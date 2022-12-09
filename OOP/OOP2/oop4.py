class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender





# outside the class -> function
def greet(person):
    print('hi my name is',person.name,'and I am a',person.gender)
    p1=Person('Happy','Negi')
    return p1
    
p=Person("Aman","vk")
g=greet(p)


print(g.name)
print(g.gender)
