
    
def digitCount(mylist,element):
    count=0
    for i in mylist:
        if i == element:
            count+=1
    print("Count of {0} is {1}".format(element,count))
        
def evendigitcount(mylist):
    ecount=0
    for j in mylist:
        if j%2==0:
            ecount+=1
    print("Count of even numbers is {}".format(ecount))
def odddigitcount(mylist):
    ocount=0
    for i in mylist:
       if i%2!=0:
            ocount+=1
    print("Count of odd numbers is {}".format(ocount))

newlist=(1,3,4,6,2,8)

print("1.COUNT OF NUMBER")
print("2.COUNT OF EVEN NUMBERS:")
print("3.COUNT OF ODD NUMBERS:")
n=int(input("ENTER CHOICE:"))
if n == 1:
    element=int(input("ENTER AN ELEMENT:"))
    digitCount(newlist,element)
if n == 2:
    evendigitcount(newlist)
if n == 3:
    odddigitcount(newlist)

