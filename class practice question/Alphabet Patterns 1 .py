n=int(input("Enter no of rows : "))

for i in range(n):
    for j in range(0,i+1):
        print(chr(65+j)," ",end="")
    print()