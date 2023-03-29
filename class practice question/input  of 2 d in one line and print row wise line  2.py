# input  of 2 d in one line and print row wise line 
str=input().split()
n,m=int(str[0]),int(str[1])

b=str[2:]
li=[[int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(li)