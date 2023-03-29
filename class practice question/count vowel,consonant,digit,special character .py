
def countvcds(str):
    s=0
    d=0
    c=0
    v=0 
    for char in str:
        if char>='a' and 'z'>=char or char>='A' and 'Z'>=char:
            char=char.lower()
            if char == "a" or  char=='e' or char =='i' or char=='o' or char=='u':
                v+=1
            else:
                c+=1
        
        elif char>='0' and char <='9':
            d+=1
        else:
            s+=1
    return v,c,d,s


str="laliria3m45m@%=-+45hmkdvc83nv8"
v,c,d,s=countvcds(str)
print("vowel=",v,"\nconsonant=",c,"\ndigits=",d,"\nspecial char=",s)