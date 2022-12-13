#read

f=open('hello.txt','r')
print(f.readlines())

f.close()

f=open('hello.txt','r')

print(f.read())
f.close()

f=open('hello.txt','r')

print(f.read(10))
f.close()