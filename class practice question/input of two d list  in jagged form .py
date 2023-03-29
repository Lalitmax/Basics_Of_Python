#  input jagged list 
n=int(input())
li=[]
li=[[int(j) for j in input().split()] for i in range(n)]
print(li)