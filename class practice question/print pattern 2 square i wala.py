import math
n=int(input())

for i in range(n):
    for j in range(i+1):
        if j==i:
            print(2**i,end="")
            
          
        else:
            print("1",end=" ")
            
            
    print()
    print()