# print alternate element 

li=input().split()
new_list=[]

for i in li:
    new_list.append(int(i))

for j in range(0,len(new_list),2):
    print(new_list[j],end= " ")