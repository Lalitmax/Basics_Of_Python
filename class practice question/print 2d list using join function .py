li=[[1,2,3,4],[5,6,7,8,5],[44,33,22,11]]

sum=[]

for i in range(len(li)):
    s=0
    for j in range(len(li[i])):
        s=s+li[i][j]
    sum.append(s)
print(sum)

