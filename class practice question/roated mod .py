''' write a program that rotates the element of a list so that the element
at the 
first index moves to the second index. the element in the second index 
moves to the third index,etc and the element in the last index moves to the first 
index '''


# input list 
list=input().split()
li=[]
# append new list splited formet
for i in list:
   li.append(i)

length=len(li)
# convert roated mod 
for i in range(length-1):
    temp=li[length-i-1]
    li[length-i-1]=li[-i-2]
    li[-i-2]=temp

# print list 
print(li)

