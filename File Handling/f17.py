#tuple
import json

t=(1,2,3,4,5)

with open('demo2.json','w') as f:
    #can not store as a tuple it will converted into list
    #tuple will always converted into list
    json.dump(t,f)

#dict with list
d={
    'name':"saka",
    'age':12
    }
l=['aman']

with open('demo4.json','w') as f:
    json.dump(d,f,indent=4)
    json.dump(l,f)
