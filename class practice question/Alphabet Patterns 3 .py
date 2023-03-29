n=int(input("Enter no of rows : "))

for i in range(n-1):
    for j in range(i+1):
        print(chr(65+j)," ",end="")
    print()

for i in range(n-1,-1,-1):
    for j in range(i+1):
        print(chr(65+j)," ",end="")
    print()