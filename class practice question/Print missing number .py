n=int(input())

list=[]
for i in range(n):
    v=int(input())
    list.append(v)

list.sort()
new_list=[]
for j in range(n):
    new_list.append(j+1)

li=[]
for k in range(n):
    if new_list[k] in  list :
        continue
    else:
        li.append(new_list[k])

print(li)


