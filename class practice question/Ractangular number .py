
n=int(input())
s=n*2-1
for i in range(0,n):
    m=n
    for j in range(i):
         print(m,end="")
         m=m-1

    for k in range(s-2*i):
        print(n-i,end="")
    m=n-i+1

    for l in range(i):
        print(m,end="")
        m=m+1
    print()


for i in range(n-2,-1,-1):
    m=n
    for j in range(i):
         print(m,end="")
         m=m-1

    for k in range(s-2*i):
        print(n-i,end="")
    m=n-i+1

    for l in range(i):
        print(m,end="")
        m=m+1
    print()
