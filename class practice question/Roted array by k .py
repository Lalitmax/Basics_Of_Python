def roted(arr,n,x):
    new_array=[]
    for i in range(n):
        index=(i+x)%n
        new_array.append(arr[index])
    for i in range(n):
        arr[i]=new_array[i]



arr=[1,2,3,4,5,6]
n=len(arr)
d=2

roted(arr,n,d)
print(arr)
