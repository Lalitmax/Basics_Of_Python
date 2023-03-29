# find pair of sum

def pairsum(arr,n,k):
    cnt=0
    for i in range(n-1):
        for j in range(i+1,n):
            if k==arr[i]+arr[j]:
                cnt+=1
    return cnt



arr=[1, 3, 6, 2, 5, 4, 3, 2 ,4,7]
k=7

n=len(arr)

print(pairsum(arr,n,k))