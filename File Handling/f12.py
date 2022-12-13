#seek with write
with open('sample.txt','w') as f:
    f.write('hello')
    f.seek(0)
    f.write('X')
