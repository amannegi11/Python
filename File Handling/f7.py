#With auto close file after done the task
# it is good idea  to close a file after usage as it will free up resources 

with open('hello.txt','w') as f:
    f.write('Messi is gonna lift the world cup')

with open('hello.txt','r') as f:
    print(f.read())