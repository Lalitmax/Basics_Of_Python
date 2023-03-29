year =int(input("Enter the year : "))

if(year%100==0):
    print("{} is a centiury year ".format(year))
else:
    print("{} is a not centiury year ".format(year))