# square print 
li=[1,2,4,3]
new_list=[]

for i in li:
    if i%2==0:
        new_list.append(i**2)
    else:
        new_list.append(i)
print(new_list)

#  in one li line 
new_list_2=[ i**2 if i%2==0 else i for i in li]
print(new_list_2)
