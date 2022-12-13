f=open('hello.txt','r')

# while f.readline()!="":
#     print(f.readline(),end="")

# f.close()

while True:

    data=f.readline()
    if data=="":
        break
    else:
        print(data,end="")

f.close()