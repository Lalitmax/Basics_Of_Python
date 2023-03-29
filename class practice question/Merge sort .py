# merge sort  
def mergensort(arr1,arr2):
   i=0
   j=0
   new_array=[]
   while(i<len(arr1) and j<len(arr2)):
    if arr1[i]<arr2[j]:
        new_array.append(arr1[i])
        i=i+1
    elif arr1[i]>=arr2[j]:
        new_array.append(arr2[j])
        j=j+1
   while(i<len(arr1)):
    new_array.append(arr1[i])
    i=i+1
   while(j<len(arr2)):
    new_array.append(arr2[j])
    j=j+1
   return new_array

        
       

arr1=[2,5,6,11,12]
arr2=[1,8,9,13,14,15,22]

sorted=mergensort(arr1,arr2)
print(sorted)