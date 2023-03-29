# find unique number 
def findunique(arr,n):
    for i in range(n):
        j=0
        while(j<n):
            if i!=j:
                if arr[i]==arr[j]:
                    break
            j=j+1
        if j==n:
            return arr[i]



n=int(input())
value=input().split()

arr=[]
for i in value:
    arr.append(i)

answer=findunique(arr,n)
print(answer)
