d={"hello":1,"lalit":4, "how":3,"are":9,"you":7}

print(d)

# copy  dictionary
d_copy=d.copy()
print(d_copy)

# access any element
print(d["how"])

# create another way

li=[("apple",3),("mango",5),("banana",8),("chilli",10)]
dicnr=dict(li)
print(dicnr)

# CREATE ANOTHER NEW METHOD

dicnr2=dict.fromkeys(["lalit","pandey","yadav"])
print(dicnr2)
dicnr2=dict.fromkeys(["lalit","pandey","yadav"],6)
print(dicnr2)

# i can also create like
d={1:2,3:4,"lalit":[1,23],"dict":{1:2}}
print(d)
print(d)
print(d["lalit"])
print(d.get("dict",9))

# print all the keys

print(d.keys())

# gate all value

print(d.values())

# print all pairs
print(d.items())
# print all the keys
for i in d:
    print(i)

# print with keys

for i in d:
    print(i,d[i])

# print value with for loop

for i in d.values():
    print(i)

# check key avalablr or not 
print("lalit" in d)