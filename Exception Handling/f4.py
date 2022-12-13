
try:
    f=open('df.txt','r')
except:
    print('File not found')
else:
    print(f.read())
finally:
    print('hello')

