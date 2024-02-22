x=int(input("ENTER No. OF MONTH:"))
y=int(input("ENTER Year:"))
if x==1:
    print("JAN is 31-day Month")
elif x==2 and y%4==0:
    print("FEB is 29- day month because its A leap year")
elif x==2 and y%4!=1:
    print("FEB is 28-day Month")
elif x==3:
     print("March is 31-day Month")
elif x==4:
     print("April is 30-day Month")
elif x==5:
     print("May is 31-day Month")
elif x==6:
     print("June is 30-day Month")
elif x==7:
     print("July is 31-day Month")
elif x==8:
     print("Aug is 31-day Month")
elif x==9:
     print("Sep is 30-day Month")
elif x==10:
     print("Oct is 31-day Month")
elif x==11:
     print("Nov is 30-day Month")
elif x==12:
     print("Dec is 31-day Month")
