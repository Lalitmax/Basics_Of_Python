# time = "good morning "
# name = "lalit"
#  print(type(name))
# c = time +name
# print(c)

# name = "lalit"
# print(name[4])
# name[3]= "r" --> does not work

'''   -->  string slicing <--  '''
# name = "lalit"
# print(name[1:4])  
# print(name[:3])  # -->  is same as name[0:3]
# print(name[2:])  # -->  is same as name[2:4]

# name = "lalit"
# print(name[-1])    # --> last element access you can 
# print(name[-5])    # --> first element access you can 

'''   -->  slicing with skip  <--  '''

name = "lalitmaxboy"
# d = name[1::3]  -->  also access
d = name[1:11:3]
print(d)
