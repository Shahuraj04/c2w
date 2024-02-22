x=int(input("Enter No. of units:"))
if (x <100):
    print("NO CHARGE")
elif(100<x<200):
    print("{}Rs. are the charges For ELctricity Bill".format(100+(x*5)))

else:
    print("SO MANY CHARGES")
