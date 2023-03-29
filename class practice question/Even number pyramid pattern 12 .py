n=int(input("Enter no of rows : "))

for i in range(1,n+1):
    even =20

    for j in range(i):
        if(even%2==0):
            print(even ," ",end="")
        even=even-2
    print()