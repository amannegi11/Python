#continue
for i in range(10):
    if i==7:
        continue
    print(i)
    
#break
for i in range(10):
    if i==7:
        break
    print(i)

#DO while loop 
i=0
while True:
    print(i)
    i=i+1
    if i%10==0:
        break
