n=int(input("Enter No of rows : "))

for i in range(1,n+1):
    for j in range(0,i-1):
        print(" ",end="")
        
    for k in range(i,n+1):
        print(k,end="")
    print()
