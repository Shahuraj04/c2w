s=int(input("START:"))
e=int(input("END:"))
pro=1
for i in range(s,e+1):
    if i%2!=0:
        pro=pro*i
print(pro)

