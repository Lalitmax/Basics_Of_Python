n=int(input("Enter no of rows : "))


for i in range(n):
    for j in range(n-i):
        print(" ",end="")
    
    for k in range(n-i,n+1):
        print(k,end="")
    

    for l in range(1,i+1):
        print(n-l,end="")

    print()



for i in range(n-1,0,-1):
    for j in range(n-i+1):
        print(" ",end="")
    
    for k in range(n-i+1,n+1):
        print(k,end="")
    

    for l in range(1,i):
        print(n-l,end="")

    print()


