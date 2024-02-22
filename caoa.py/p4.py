def myindex(mylist,n):
    ind=0
    for i in mylist:
        if n == i:
            ind=mylist.index(i)
    print("number {0} found at index {1}".format(n,ind+1))
newlist = []   
num_elements=int(input("ENTER NO. OF ELEMENTS:"))
for j in range(num_elements):
    element = int(input("Enter element no.{}: ".format(j+1)))
    newlist.append(element)

print("Your list:", newlist)
n=int(input("ELEMENT TO BE FOUND:"))
#newlist=(1,2,4,5)
myindex(newlist,n)



