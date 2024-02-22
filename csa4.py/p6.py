s=ord(input("ENTER START OF RANGE:"))
e=ord(input("ENTER END OF RANGE:"))
for i in range(s,e):
    print("ASCII VALUE OF {0} is: {1}".format(chr(i),i))
