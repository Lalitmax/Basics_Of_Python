num = int(input("Enter the number : "))
last = num%10

if last%3==0:
    print("{} is divisible by 3".format(last))
else:
    print("{} is not divisible by 3".format(last))