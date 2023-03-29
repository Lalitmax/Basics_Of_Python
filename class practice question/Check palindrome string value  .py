# check palindrome

def checkpalindrome(str):
    check=''
    for i in range(len(str)):
        check+=str[-i-1]
    print(check)
    if check==str:
        return True
    else:
        return False





str=input("Enter the string : ")
if checkpalindrome(str):
    print("true")
else:
    print("false")
