#half pyramid of stars

n=int(input("Enter No rows : "))

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
