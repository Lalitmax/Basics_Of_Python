# Inverted Pyramid involving numbers

n=int(input("Enter No rows : "))

for i in range(n):
    for j in range(n-i):
        print(n-i,end="")
    print()