
def replace(string,ch1,new_ch2):
    new_string=''
    for i in string:
        if ch1==i:
            new_string+=new_ch2+" "
        else:
            new_string+=i+" "

    return new_string


print("Lalit Kumar Yadav And Max")
ch1=input()
ch2=input()

keyw="Lalit Kumar Yadav And Max"

keyw=keyw.split()

rpw=replace(keyw,ch1,ch2)
print(rpw)
