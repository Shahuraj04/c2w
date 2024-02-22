x=int(input("Enter Number:"))
for i in range(1,x+1):
    if (i%5==0 and i%10==0):
        print("*",end=" ")
    elif(i%5==0):
        print(i,end=" ")
