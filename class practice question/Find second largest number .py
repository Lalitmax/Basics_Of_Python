# find second largest number

def sec_lar_num(arr,n):
    arr.sort(reverse=True)
    for i in range(n):
        if arr[i]!=arr[i+1]:
            return arr[i+1]


# takink input
size=int(input("Enter size of array : "))
print("iput list ")
list=input().split()
arr=[]
for i in range(size):
    arr.append(int(list[i]))
# calling function
print(sec_lar_num(arr,size))
