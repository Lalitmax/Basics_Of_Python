
def binarysearch(arr,key):

   s=0
   e=len(arr)-1
   while(s<=e):
    mid=(s+e)//2

    if arr[mid]==key:
        return mid
    elif arr[mid]<key:
        s=mid+1
    else:
        e=mid-1
    
   return -1

arr=[1 ,3 ,7, 9, 11, 12, 45]
key=7
index=binarysearch(arr,key)
print(index)