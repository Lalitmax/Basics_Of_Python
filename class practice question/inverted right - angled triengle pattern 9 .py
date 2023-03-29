n=int(input("Enter No rows : "))

for i in range(1,n+1):
    for j in range(n+1,0,-1):
       if j>i:
            print(" ",end="")
       else:
            print("&",end="")
     
    print()