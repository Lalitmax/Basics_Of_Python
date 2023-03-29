n=int(input("Enter value of n : "))
length=len(str(n))
sum =0
orig =n
while(n>0):
    last_digit=n%10
    sum =sum+last_digit**length                       # 0 1 153 370 371 
    n=n//10
if(sum==orig):
    print("{} is a Armstrong number= ".format(orig))
else:
    print("{} Not a Armstrong number= ".format(orig))