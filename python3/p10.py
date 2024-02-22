x=int(input("Enter Start Of Range: "))
y=int(input("Enter End Of Range: "))
for i in range(x,y+1):
    if(i%4==0 and i%5!=0):
        print(i)
