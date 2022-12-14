#when a function does not return anything it return None

a=2
def Fun():
    a=1
    print(a)
Fun()
print(a)

#we can access but we can not change the value of global var
a=2
def Fun():
    print(a)
Fun()
print(a)

#we can only change global var value when we define it global var
a=2
def f1():
    global a
    a+=1
    print(a)

f1()
print(a)