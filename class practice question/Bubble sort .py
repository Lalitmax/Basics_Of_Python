# bubble sort 
def selectionsort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


arr=[2 ,13, 4 ,1 ,3 ,6,28, 28]
index=selectionsort(arr)
print(arr)