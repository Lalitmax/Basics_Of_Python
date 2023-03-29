n=int(input("Enter no of rows : "))

for i in range(1,n+1):
    for j in range(n+i):
        if j>(n+i)-i*2:
            print("*",end="")
        else:
            print(" ",end="")
        
    print()