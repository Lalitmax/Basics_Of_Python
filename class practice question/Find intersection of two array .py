# find intersection of two array
import sys
def findintersection(arr1,n1,arr2,n2):
    
    for i in range(n1):
        for j in range(n2):
            if arr1[i]==arr2[j]:

                print(arr1[i],end=" ")
                arr2[j]= sys.maxsize
                break




arr1=[2 ,6 ,1, 2]
arr2=[1, 2, 3, 4 ,2]
n1=len(arr1)
n2=len(arr2)
findintersection(arr1,n1,arr2,n2)