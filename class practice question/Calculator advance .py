# make calculator
n=int(input())


while n!=6:
    if n<=5 and n>=1:
        a=int(input())
        b=int(input())
    if n==1:
        print(a+b)
    elif n==2:
        print(a-b)
    elif n==3:
        print(a*b)
    elif n==4:
        print(a/b)
    elif n==5:
        print(a%b)
    elif n>6 and 0<n:
        print("Invalid Operation")
    n=int(input())