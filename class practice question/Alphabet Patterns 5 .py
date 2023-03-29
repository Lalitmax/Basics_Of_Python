str=input("Enter your name : ")
l=len(str)

for i in range(l-1):
    for j in range(i+1):
        print(str[j],end="")
    print()


for i in range(l-1,-1,-1):
    for j in range(i+1):
        print(str[j],end="")
    print()