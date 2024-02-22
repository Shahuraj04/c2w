def fun(x,y):
    print("START OF FUN")
    while(x<=y):
        yield x
        x+=1
    print("END OF FUNCTION")
for val in fun(1,30):
    print (val)
