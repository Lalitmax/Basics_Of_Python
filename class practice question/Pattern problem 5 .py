n=int(input("Enter NO of rows : "))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")

    for k in range(n-i,n):
        print(k+1,end="")
    print()
    

