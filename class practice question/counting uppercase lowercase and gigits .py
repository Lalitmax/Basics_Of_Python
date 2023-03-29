st=input()

lowercase=0
uppercase=0
digit_count=0

for i in st:
    if i>='A' and i<="Z":
        uppercase+=1
    elif i>='a' and i<='z':
        lowercase+=1
    elif i>="0" and i<='9':
        
        digit_count+=1
        
d1={}
d2={}
d3={}
d1["Lowercase"]=lowercase
d2["Uppercase"]=uppercase
d3["Digit"]=digit_count

print(d1)
print(d2)
print(d3)
        