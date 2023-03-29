# list comprehension

li=[2,3,4,5,6,9]
new_list=[]
for i in li:
    new_list.append(i**2)

print(new_list)



# another way 
new_list_2=[ele**2 for ele in li]
print(new_list_2)



# for even square 

new_list_3=[]
new_list_3=[ele**2 for ele in li if ele%2==0]
print(new_list_3)

#  using for loop (print only even no of  square)

new_list_4=[]
for i in li:
    if i%2==0:
        new_list_4.append(i**2)
print(new_list_4)

#  using for loop (print only even and devide by 3 no of  square)

new_list_5=[]
for i in li:
    if i%2==0:
        if i%3==0:
            new_list_5.append(i)
print(new_list_5)

#  using for loop (print only even and devide by 3 no of  square) using single line code

new_list_6=[]
new_list_6=[ele for ele in li if ele%2==0 if ele%3==0]

print(new_list_6)


