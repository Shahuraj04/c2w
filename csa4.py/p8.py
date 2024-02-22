s=int(input("START:"))
e=int(input("END:"))
for i in range (s,e+1):
    if i%5==0 and i%3==0:
        print(i)
