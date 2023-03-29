# first method
li=["lalit","rahul","mukesh","nitish"]
new_list=[]
new_list=[[i for i in j ]  for j in li]
print(new_list)

# second method
print()
new_list2=[]
for i in li:
    for j in i:
        new_list2.append(j)
print(new_list2)
print(len(new_list2))