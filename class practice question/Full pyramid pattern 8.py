# Full pyramid
n=int(input("Enter No of rows : "))

for i in range(1,n+1):
    for j in range(n+1-i):
        print(" ",end="")
    
    for k in range((i*2)-1):
        print("*",end="")
    print()