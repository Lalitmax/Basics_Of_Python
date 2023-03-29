n=int(input())
a=0
b=1
i=0
temp=False
while(i<=n):
        if a==n:
            temp=True
        c=a+b
        if c==n:
           temp=True
        a=b
        b=c
        i=i+1
if temp:
    print("true")
else:
    print("false")


    
