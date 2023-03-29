# push zero to end

def pusjzerotoend(arr,n):
    j=0
    for i in range(n):
        if arr[i]>0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j=j+1

arr=[2 ,0 ,0 ,1, 3, 0, 0]
n=len(arr)

pusjzerotoend(arr,n)
print(arr)