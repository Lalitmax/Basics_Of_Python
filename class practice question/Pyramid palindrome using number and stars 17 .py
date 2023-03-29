n=int(input("Enter no of rows : "))

star=8

for i in range(1,n+1):
    for j in range(star-i):
        print("*",end="")
    
    for k in range(i*2):
        if (k)%2==0:

            print(i,end="")
        else:
            
            
            print("*",end="")

    for j in range(star-i-1):
        print("*",end="")


    print()
