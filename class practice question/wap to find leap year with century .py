year = int(input("Enter the year : "))

if(year%100==0):
    if(year%400==0):
        print("{} is a leap year".format(year))
    else:
        print("{} is a not leap year ".format(year))
else:
    if(year%4==0):
        print("{} is a leap year".format(year))
    else:
        print("{} is a not leap year".format(year))