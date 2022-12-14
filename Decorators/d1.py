#Decorators
# A decorator in python is a function that receives another function as input and adds some functionality(decoration) 
# to and it and returns it

def my_deco(f):
    def w():
        print('*******')
        f()
        print("*******")
    return w

@my_deco
def hello():
    print('hello')

hello()