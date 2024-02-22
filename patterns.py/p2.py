num=65
for i in range(3):
    for j in range(3-i):
        print(chr(num),end=" ")
        num=num+1
    print()
