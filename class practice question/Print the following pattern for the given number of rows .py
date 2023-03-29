n=int(input("Enter a number : "))

for i in range(n):
    for j in range(n-i):
        if(i%2==0):
            print(1,end="")
        else:
            print(0,end="")
    print()
        