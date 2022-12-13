#object as it is
#pickling

# Pickling is the process whereby a Python object hierarchy is converted into a byte stream 

class Person:


    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender

    def NAAM(self):
        return self.name+" "+self.lname

p=Person('Aman',"negi",22,'male')
import pickle
with open('person.pkl','wb') as f:
    pickle.dump(p,f)