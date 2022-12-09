class Person:

    def __init__(self,name,gender) -> None:
        self.name=name
        self.gender=gender
    

p1=Person('Aman',"male")
p2=Person('ro','male')
p3=Person('sky','female')

l=[p1,p2,p3]
d={'p1':p1,'p2':p2,'p3':p3}

# print(l)
for i in l :
    print(i.name,i.gender)

for i in d.keys() :
    print(d[i].name,d[i].gender)

s={p1,p2,p3}
for i in s:
    print(i.name)    