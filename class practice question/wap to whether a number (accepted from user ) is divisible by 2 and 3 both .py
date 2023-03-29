n = int(input("Enter the number : "))

if(n%3==0 and n%2==0):
    print("{} is divisible by 2 and 3".format(n))
else:
    print("{} is not divisible by 2 and 3 ".format(n))