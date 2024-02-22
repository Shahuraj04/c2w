for i in range(0,5,1):
    for j in range(0,5-i,1):
        print("",end=" ")
    for k in range(0,i+1,1):
        print("*",end=" ")
    print()
for i in range(0,5,1):
    for j in range(0,i+1,1):
        print("",end=" ")
    for k in range(0,5-i,1):
        print("*",end=" ")
    print()

