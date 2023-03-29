
def sortzeroonetwo(arr,n):
    next=0
    for i in range(n):
        if arr[i]==0:
            temp=arr[i]
            arr[i]=arr[next]
            arr[next]=temp
            next+=1
    
    for j in range(next,n):
        if arr[j]==1:
            temp=arr[j]
            arr[j]=arr[next]
            arr[next]=temp
            next+=1






# taking input
size=int(input("Enter size of list : "))
print("input list ")
list=input().split()

arr=[]

for i in range(size):
    arr.append(int(list[i]))

# calling finction

sortzeroonetwo(arr,size)
print(arr)