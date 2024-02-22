countp=0
countn=0
countz=0
while(1):
    i=int(input("ENTER THE NUMBER:"))
    if(i>0):
        countp=countp+1
    elif(i<0):
        countn=countn+1
    else:
        countz=countz+1

    print("DO YOU WANNA COUTINUE(YES/NO):")
    choice=input()
    if(choice=="NO"):
        break;

print("POSITIVE NOs:",countp)
print("NEGATIVE NOs:",countn)
print("ZEROS:",countz)
