
def max_occur(str1):
    # first remove duplicate char
    str2=set(str1)

    # second sort char
    str2=sorted(str2)

    max_occur_char=-1
    max_cout=0
    #  check how many times occure
    for i in str2:
        cnt=str1.count(i)

        if cnt>max_cout:
            max_cout=cnt
            max_occur_char=i
    
    return max_occur_char
            


str1="aabbb"

ans=max_occur(str1)
print(ans)