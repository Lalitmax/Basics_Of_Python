# input of 2 d in one line and print row wise line 
st=input().split()
n,m=int(st[0]),int(st[1])

b=input().split()
li=[[ int(b[m*i+j]) for j in range(m)] for i in range(n)]
print(li)