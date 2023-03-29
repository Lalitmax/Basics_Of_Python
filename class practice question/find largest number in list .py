#  find largest number

# size=int(input("how many element you want to enter : "))

li2=input().split()
li=[]
for i in li2:
    li.append(int(i))

le=len(li)
ans=li[0]
for i in range(1,le):
    if ans<li[i]:
        ans=li[i]
   
print(ans)
