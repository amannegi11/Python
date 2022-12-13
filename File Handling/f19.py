#as a dict
class Person:


    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender

p=Person('aman','negi',12,'male')

def show(p):
    if isinstance(p,Person):
        return {"name":p.fname+' '+p.lname ,'age':p.age, 'gender':p.gender}
import json

with open('dict.json','w') as f:
    json.dump(p,f,default=show,indent=4)