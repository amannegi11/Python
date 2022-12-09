class Person:
    def __init__(self):
        self.name="Aman"
        self.gender='Male'

# p is just a reference variable  which stores/contains reference of object location 
# we can create object without Reference 
p=Person()
q=p

print(p.name)
print(q.name)

q.name="negi"
print(q.name)
print(p.name)

