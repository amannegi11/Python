# Problem with working in text mode 
#can not work binary files like images
#not good for other data types like int/float/list/tuples

#working with binary file
# with open('wall.jpg','r') as f:
#     f.read()

with open('wall.jpg','rb') as f:
    with open('wall_copy.jpg','wb') as wf:
        wf.write(f.read())


