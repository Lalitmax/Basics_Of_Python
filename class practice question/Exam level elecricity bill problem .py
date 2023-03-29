n=int(input())
amt=0
if(n<=100):
    amt=0
if(n>100 and n<=200):
    amt=(n-100)*5
if(n>200):
    amt= 500+(n-200)*10
print("Amount to pay ",amt)
