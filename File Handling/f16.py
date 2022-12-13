#deserialization
import json

with open('demo1.json','r') as f:
    d=json.load(f)
    print(d,'\n',type(d))
#when ever you are dealing with complex data type like list dictionary use json method
