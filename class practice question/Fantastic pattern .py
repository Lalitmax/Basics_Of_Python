
n=int(input())

star=n*2

for i in range(1,n+1):
    for j in range(1,star+2):
        if j==i or j==n+1 or j==star+2-i:
            print("*",end="")
        else:
            print(' ',end="")
    print()
   


for i in range(n,0,-1):
    for j in range(1,star+2):
        if j==i or j==n+1 or j==star+2-i:
            print("*",end="")
        else:
            print(' ',end="")
    print()

    
   

    



   


        
   
 