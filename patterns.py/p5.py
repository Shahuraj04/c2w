n=5
char=65
num=1
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
        
    for j in range(i,n):
        print(" ",end=" ")
    
        
    for j in range(i,n):
        print("*",end=" ")
        
    print()

