units=int(input("Enter units : "))
bill =0.0
if(units<=100):
    bill=0
    print("Amount to pay = ",bill)
elif(units>100 and units<=200):
    bill = 100*0 +(units-100)*5
    print("Amount to pay = ",bill)
else:
    bill=100*0 +100*5 +(units-200)*10
    print("Amount to pay = ",bill)