# join abcd print
a="ab".join("abcd")
print(a)

# print number print

b="ab".join(["1","2","3","4"])
print(b)

# print list 

li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for i in li:
    output=" ".join(str(ele) for ele in i)
    print(output)