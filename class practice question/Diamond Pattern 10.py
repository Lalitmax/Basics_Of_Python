# diamond pattern 
n=int(input("Enter NO of rows : "))


for i in range(1,n):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print(" *",end="")
    print()


for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(n-i+1):
        print(" *",end="")
    print()
