#Run time Error(Exceptions)(logical error)

with open('df.txt','w') as f:
    print(f.write('Hello'))



try:
    with open('df.txt1','r') as f:
        print(f.read())
except Exception as e:
    print('file not found',e)
