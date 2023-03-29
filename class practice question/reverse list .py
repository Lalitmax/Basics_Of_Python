#  reverse a list 

list=input("Enter a list ").split()

length=len(list)//2
for i in range(length):
    temp=list[i]
    list[i]=list[-i-1]
    list[-i-1]=temp

print(list)

