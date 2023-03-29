# triplet sum

def tripletsum(arr,n,x):
    cnt=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if x==arr[i]+arr[j]+arr[k]:
                    cnt=cnt+1
    return cnt






arr=[2 ,-5 ,8 ,-6, 0, 5, 10, 11, -3]
k=10
n=len(arr)

print(tripletsum(arr,n,k))