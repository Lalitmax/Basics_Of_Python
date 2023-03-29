l=[3,5,12,79,6,1,3,92]
l=set(l)
l=list(l)
h=0
t=0
for i in l:
    if i==0:
        h=i
    if i>h:
        if i>0:
            t=h
            h=i
print(t)