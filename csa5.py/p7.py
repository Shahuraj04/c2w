n=int(input("ROW:"))
num=1
for i in range(n):
    for j in range(n):
        print(num,end=" ")
        num=num+2
    print()
