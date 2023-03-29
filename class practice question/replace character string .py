def replace(str,char1,char2):
    new_string=''

    for i in str:
        if i==char1:
            new_string+=char2
        else:
            new_string+=i
    return new_string


print("lalit kumar yadav pandey max")
str="lalit kumar yadav pandey max"
print("\n what do you want to replace")
print()
chr=input()
rep_chr=input()

tpl=replace(str,chr,rep_chr)
print(tpl)