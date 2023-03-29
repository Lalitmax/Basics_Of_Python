n=int(input())

amt=0
if(n<=100):
    amt=0
    print("Amount to pay : ",amt)
elif(n>100 and n<=200):
    amt=(n-100)*5
    print("Amount to pay : ",amt)
else:
    amt=( (100)*5 +(n-200)*10)
    print("Amount to pay : ",amt)