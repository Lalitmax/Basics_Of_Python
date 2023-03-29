ch=input("Enter no of rows : ")

l=len(ch)

for i in range(l):
    for j in range(i+1):
        print(ch[j],end="")
    print()
    