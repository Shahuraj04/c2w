def countof(List,element):
    count=0
    for i in List:
        
        if i==element:
            count=count+1
    print(count)
mylist=(33,4,5,4,3,4,5)
selement=4
countof(mylist,selement)
