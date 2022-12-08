
a=int(input("Enter the number "))
c=input("Enter oprator")
b=int(input('Enter next number'))
if c=="+":
    ans=a+b
elif c=="-":
    ans=a-b
elif c=="/":
    ans=a/b
else:
    ans=a*b

print(f"{a}{c}{b}={ans}")
