# For multiple lines 
'''f=open('j.py','w')
f.write("for i in range(10):\n  print(i)")
f.close()'''


f=open('hello.txt','w')
f.write('hello!\nwho are you?')
f.write('\ni would love to play')

f.close()

f=open('hello.txt','r')
print(f.read())
f.close()