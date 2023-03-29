n=int(input("Enter the numbe: "))
rev=0
while(n>0):
    last_digit=n%10
    rev = rev*10 +last_digit
    n //=10
print("Reverse  = ",rev)