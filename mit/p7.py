for i in range(5,0,-1):
    for j in range(i+1):
        if (i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
