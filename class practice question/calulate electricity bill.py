# calculate electricity bill
units=int(input("Enter units : "))
bill=0.0
if(units<=200):
    bill=units*6
    print("Amount to pay = ",bill)
elif(units >200 and units<=400):
    bill=200*6 +(units-200)*7
    print("Amount to pay = ",bill)
elif(units>400 and units<=600):
    bill=200*6 +200*7 +(units-400)*8
    print("Amount to pay = ",bill)
else:
    bill = 200*6 +200*7 + 200*8 +(units-600)
    print("Amount to pay = ",bill)