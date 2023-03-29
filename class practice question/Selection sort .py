# selection sort 
def selectionsort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp


arr=[5,4,7,1,8]
index=selectionsort(arr)
print(arr)