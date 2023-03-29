# sort 0 ,1
def sortzerandone(arr,n):
    j=0
    for i in range(n):
        if arr[i]==0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j +=1
    

arr=[0 ,1 ,1, 0 ,1, 0 ,1]
n=len(arr)

sortzerandone(arr,n)
print(arr)
