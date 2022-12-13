#big file
Big=['Aman Negi\n' for i in range(10000)]

with open('Big.txt','w') as f:
    f.writelines(Big)

print(len(Big))

