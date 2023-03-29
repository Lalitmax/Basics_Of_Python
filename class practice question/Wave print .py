# print like vawe number 

def findLargest(arr):
    #Your code goes here
    m=len(arr[0])
    n=len(arr)
    new_list=[]
    for i in range(m):
        for j in range(n):
            if i%2==0:
                new_list.append(arr[j][i])
            else:
                new_list.append(arr[-j-1][i])
        
    return new_list



lst=[[1,2,3,4],[6,23,65,7],[7,5,3,2]]

a=findLargest(lst)
print(a)



