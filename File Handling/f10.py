with open('Big.txt','r') as f:
    
    chunk_size=90
    while len(f.read(chunk_size))>0:
        print(f.read(chunk_size),end="")
        f.read(chunk_size)