#seek and tell function

with open('hello.txt') as f:
    print(f.read(10))
    print(f.tell()) #it will tell next char execution



with open('hello.txt') as f:
    print(f.read(10))
    f.seek(0) # it will again put your cursor in initial stage and start execution 
    print(f.read(10))