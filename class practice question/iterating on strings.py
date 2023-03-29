str="LALIT"

for i in str:
    print(i,end=" ")


#  count letter in string 

count=0
find="L"
for i in str:
    if (i==find):
        count=count+1
print("\n{} times ".format(count),"{} in string".format(find))

# with loop range
count=0
for i in range(len(str)):
    if (str[i]==find):
        count+=1

print("\n{} times ".format(count),"{} in string".format(find))

p="herohonda"

if "hero" in p:
    print("yes it is a substring ")
else:
    print("not it is a not substring ")


if "heroi" in p:
    print("yes it is a substring ")
else:
    print("no it is a not substring ")

