str1=input()


Lowercase=0
Upper_case=0

for i in str1:
    if i>="A" and i<="Z":
        Upper_case+=1
    elif i>="a" and i<='z':
        Lowercase+=1
        
print("Lowercase: ",Lowercase)
print("Uppercase: ",Upper_case)