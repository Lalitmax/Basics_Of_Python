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
n=len(li)
kst2=li[n-1:n:]+li[0:-1:1]
print(kst2)