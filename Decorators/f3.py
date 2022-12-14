

def outer():#global scope
    def inner():#local scope
        print('Inner Function')
    inner()#enclosing scope
    print('outer function')
outer()
print('main program')#builtin scope