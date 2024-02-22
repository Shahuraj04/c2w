s=int(input("ENTER START OF RANGE:"))
e=int(input("ENTER END OF RANGE:"))
for i in range(s,e+1):
    if i%7==0 and i%3!=0:
        print(i,end=" ")
print()
