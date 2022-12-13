#Serialization and Deserialization

#serialization process of converting pytho data type to json
#Deserialization process of converting  jsonto python data types

#what is json -->> java script on notation('it is a universal data format (every programming language understand it)')

import json

L=[1,2,3,4,5]

with open('demo.json','w') as f:
    json.dump(L,f)


d={
    'name':'negi',
    'age':'22',
    'gender':'male',
}

with open('demo1.json','w') as f:
    json.dump(d,f,indent=4)
    # for better representation use indent

