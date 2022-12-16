#string methods
#string are immutable
A="AmAn"
print(len(A))
print(A.upper())
print(A.lower())
print(A.count('a'))

# strip method removes any white spaces and before and after string 
A=" Ama n 1 1  "
print(A.strip())

# rstrip removes any trailing characters 
A="!!! Hello !!!"
print(A.rstrip("!"))


A="Aman negi"
print(A.replace("Aman","Happy"))


#split()
# The split() method splits the given string at the specified instance and returns the separated strings as list items
A="AM an ne gi"
print(A.split(" "))
A="am an ne gi"
print(A.split("a"))

print(A.capitalize())

#center()
# the center() method aligns the  string to the center as per the parameters given by the user 
A="aman"
print(A.center(50)) 
print(len(A.center(50))) 


A="Rohit sharma is a cricketer"
print(A.find('is'))

