n=int(input("Enter no of rows : "))


for i in range(1,n):
    
    for j in range(i):
        print(" ",end="")

    for k in range(i,n+1):
        print(k,end="")

    print()



for i in range(n,0,-1):
    
    for j in range(i):
        print(" ",end="")

    for k in range(i,n+1):
        print(k,end="")

    print()
