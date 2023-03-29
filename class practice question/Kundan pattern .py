n=int(input())
cnt=1
i=1
while(i<=n):
    j=1
    while(j<=i):
        if (i+j)%2==0:
           print(cnt,end="")
           
        else:
            print("#",end="")
        cnt=cnt+1
            

        j=j+1

    i=i+1
    print()

