n=int(input("Enter the number : "))
rev=0
orig=n

while(n>0):
    rev=rev*10+n%10
    n=n//10
if(orig==rev):
    print("{} is a palindrome number ".format(orig))
else:
    print("{} is  not a palindrome number ".format(orig))