try:
    with open('df.txt','w') as f:
     print(f.write('Hello'))
     print(M)
except Exception as e:
    print(e.with_traceback)
    