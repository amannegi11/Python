#Write mutliple lines
L=['hello\n','hi\n','how are you\n','I am fine\n']

f=open('hello.txt','w')
f.writelines(L)
f.close()
